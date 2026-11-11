#!/usr/bin/env python3
"""Read one public LinkedIn profile through Jina Reader. No login, no browser."""

import json
import re
import sys
import urllib.request

BLOCK_TITLES = ("sign up", "log in", "login", "join linkedin", "authwall")


def normalize(url):
    match = re.search(r"https?://([\w.-]+\.linkedin\.com)/(in|pub)/([^/?#]+)", url, re.I)
    if not match:
        raise SystemExit("not a linkedin profile url")
    host, kind, slug = match.group(1).lower(), match.group(2).lower(), match.group(3).strip("/")
    if host == "linkedin.com":
        host = "www.linkedin.com"
    public = f"https://{host}/{kind}/{slug}"
    reader = f"https://r.jina.ai/http://{host}/{kind}/{slug}"
    return public, reader


def fetch(reader_url):
    request = urllib.request.Request(
        reader_url,
        headers={"User-Agent": "Mozilla/5.0", "X-Timeout": "25"},
    )
    with urllib.request.urlopen(request, timeout=40) as response:
        return response.read().decode("utf-8", "replace")


def field(text, label):
    match = re.search(rf"^{re.escape(label)}:\s*(.*)$", text, re.M)
    return match.group(1).strip() if match else ""


def section(text, heading):
    match = re.search(rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    if not match:
        return ""
    body = match.group(1)
    body = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", body)
    body = re.sub(r"[#*>`\[\]]", " ", body)
    body = re.sub(r"\s+", " ", body).strip()
    return body[:1200]


def languages(text):
    block = re.search(r"^## Languages\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    if not block:
        return []
    names = re.findall(r"^###\s+(.+)$", block.group(1), re.M)
    levels = re.findall(r"^####\s+(.+)$", block.group(1), re.M)
    rows = []
    for index, name in enumerate(names):
        level = levels[index].strip() if index < len(levels) else "未显示"
        if "sign in" in name.lower() or name.startswith("**"):
            continue
        rows.append({"language": name.strip(), "level": level})
    return rows


def classify(text):
    title = field(text, "Title").lower()
    final = field(text, "Final URL").lower()
    if "authwall" in final or any(token in title for token in BLOCK_TITLES):
        return "authwall"
    if "error 999" in text.lower() or len(text.strip()) < 400:
        return "blocked"
    if "/in/" in final or "/pub/" in final:
        return "public"
    return "empty"


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: read_public_profile.py <linkedin-profile-url>")
    public, reader = normalize(sys.argv[1])
    text = fetch(reader)
    status = classify(text)
    result = {
        "status": status,
        "public_url": public,
        "reader_url": reader,
        "title": field(text, "Title"),
        "final_url": field(text, "Final URL"),
        "location_line": "",
        "languages": [],
        "experience": "",
        "education": "",
    }
    if status == "public":
        location = re.search(r"^###\s+(.+Contact Info)", text, re.M)
        result["location_line"] = location.group(1).replace(" Contact Info", "").strip() if location else ""
        result["languages"] = languages(text)
        result["experience"] = section(text, "Experience & Education") or section(text, "Experience")
        result["education"] = section(text, "Education")
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
