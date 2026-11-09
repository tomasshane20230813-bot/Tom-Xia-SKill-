---
name: Active candidate scoring
description: >-
  Use whenever sourcing or shortlisting candidates for FORESTOWN / Tom Xia:
  score Active job-seeking intent separately from role fit using the public-web
  Active SOP and ACI Finder rules.
---
# Active candidate scoring (FORESTOWN)

Cross-project method for identifying and scoring people who are actively open to opportunities. **Role-fit score and Active score must stay separate** — never mix them into one number, and never call someone Active without dated, first-party evidence.

## Canonical sources (re-read when rules change)
- Notion ACI Finder: `https://app.notion.com/p/40719ef2dc3781759f98e6a9b553ff7f`
- Drive SOP: *Active候选人公开网络识别与评分SOP.docx* (team Drive copy; file id omitted from this archive)
- Optional ACI Finder site: `https://aci-finder-tomxia.tom-xia.chatgpt.site/` — if unreachable, say so; do not invent its output

## Hard rules
1. Score **role fit (0–100)** first from JD / hiring profile alone.
2. Score **Active (0–10)** second from public evidence only.
3. Every Active point needs: short quote, evidence date, source URL, check date, evidence type (fact / inference / insufficient).
4. Prefer first-party signals (person’s own post/status/resume). Company layoffs ≠ person laid off.
5. Do not infer ethnicity, gender, or age from name/photo; never use protected attributes in Active or role scoring.
6. Deduplicate the same behavior across platforms (one event = one score).
7. If no strong personal job-seeking evidence in ~90 days → Active = 0 and label **Active未证实**; keep strong role-fit people in an observation pool, separated from confirmed-Active lists.
8. No outreach in this skill unless the parent task explicitly asks Contact & Outreach to send.

## Search order (public / connected tools)
1. Role-fit search (Apollo/Clay/X-ray/etc.) → shortlist + LinkedIn URL normalize + historical dedup.
2. Active pass per person, strongest channels first:
   - Open to Work / actively seeking / looking for opportunities / available immediately (person’s own words or verified frame)
   - Recent resume/CV hire-me pages (≤90 days)
   - Explicit apply/interest comments on job posts
   - First-person layoff / contract ended / career break seeking
   - GitHub Available for hire + hire-me README; HN “Who wants to be hired?”; Reddit [For Hire]; Wellfound Ready to Interview / Open to Offers; Cord active stream; opt-in layoff lists (e.g. Parachute)
   - Resume-board “last active” + recent resume update together (Dice/Indeed/etc.)
3. Check reverse signals: new job ≤30 days, promotion, “not looking”, deleted seeking post.
4. Apply time decay: 0–30d full; 31–90d usually keep; 3–6m ×0.6 need support; 6–12m ×0.3 alone insufficient; >12m background only.

## Scoring card (sum, then cap contextually to 0–10 band used in FORESTOWN deliverables)
Use the July 2026 SOP point values for evidence (examples):
- +5: clear personal seeking ≤90d; recent job-seeking resume; HN current-month hire-me; Reddit ≤30d [For Hire]; Wellfound Ready to Interview; Cord active; opt-in layoff list; GitHub hire status + hire README together
- +4: GitHub Available for hire alone; explicit “I applied / interested”; personal layoff/contract end; Career Break / Seeking Opportunities; Wellfound Open to Offers; HN 31–90d
- +3–4: resume-board recent activity + update; career-fair resume upload
- +3: bounced work email *plus* resume change (never probe-email); multiple 30–90d job-post interactions; public recruiter job chats
- +2: contractor/freelance *with* availability signals; hire-oriented personal-site update
- +1–2: company/dept layoff only (weak)
- +0.5: single job-post like (never alone for Active)
- 0: ordinary tech activity / GitHub commits

Reverse: −5 new job ≤30d or “not looking”; −3 promotion / seeking post removed or stale; decay old evidence as above.

### Active bands (0–10 deliverable scale)
Map SOP totals into the project’s 0–10 Active field (ACI Finder / Yealink V5 practice):
- **8–10** High probability Active — personal seeking ≤90d or verified Open to Work with date/URL
- **6–8** Strong mid — platform seeking status with dated evidence
- **3–6** Possible — several medium signals combined
- **0–2** Weak / company-only risk
- **0 + Active未证实** — no personal evidence

Legacy SOP bands (≥8 / 5–7.5 / 3–4.5 / <3) may be noted in `active_band` for compatibility.

## Per-candidate output fields
Always include alongside role-fit fields:
- `active_score` (0–10)
- `active_band` (高概率 / 中高 / 可能 / 未证实)
- `active_evidence[]`: {type, quote, evidence_date, url, checked_at, points}
- `active_notes`: reverse signals, decay applied, what still needs phone verify

## Quality checklist
- [ ] Role fit and Active scored separately
- [ ] Each Active add has original URL + dates
- [ ] No double-counting same event
- [ ] No mistaking others’ posts, company hiring posts, or hobby engagement for personal seeking
- [ ] Reverse signals checked
- [ ] Weak evidence kept in observation pool, not labeled confirmed Active

## When sourcing in a round
After building the role shortlist, run this Active pass before delivery. Sort/outreach priority may use Active as a secondary key, but never inflate role-fit because someone is Active.
