---
name: GitHub evidence sourcing
description: >-
  Use when sourcing Silicon Valley AI or other technical candidates after
  LinkedIn public X-ray stopped filtering by title/location: search GitHub for
  recent work evidence first, then validate people.
---
# GitHub evidence sourcing

Use this when LinkedIn public X-ray no longer filters by title/location, and the role is technical (especially Silicon Valley AI/ML). GitHub is an evidence database, not a people database. Do not log into anyone's personal LinkedIn to run this.

## Mindset
1. Start from the technical problem (language, framework, domain), not the job title alone.
2. Search repos and code before people profiles.
3. Require recency (`pushed:>YYYY-MM-DD`, `merged:>YYYY-MM-DD`).
4. Let AI draft Boolean strings; humans own intake (what the market really calls the role) and judging results.
5. Cross-check promising people on public web sources later. Never use the user's personal LinkedIn or personal Chrome session.

## Default workflow
1. Clarify must-have tech signals from the JD (e.g. PyTorch, transformers, CUDA, LLM serving).
2. Run repository search on github.com/search with recency filters.
3. Open active repos → contributors / recent merged PRs → shortlist people who leave real fingerprints.
4. Deduplicate against existing talent library / prior rounds.
5. Score role fit and Active separately; keep Chinese/Mandarin business-evidence rules when the client requires them.
6. Enrich contacts only after shortlist; draft outreach only—never send without the user's approval.

## Copy-paste starters (update the year as needed)
Active Python ML repos:
```
language:python ("pytorch" OR "tensorflow" OR "scikit-learn") pushed:>2025-01-01
```
LLM / Hugging Face work:
```
language:python ("huggingface" OR "transformers" OR "fine-tuning") pushed:>2025-01-01
```
Topic + activity:
```
topic:llm stars:>50 pushed:>2025-01-01
```
Recent merged PRs (then open a canonical repo and read contributors):
```
is:pr is:merged merged:>2025-01-01
```
User location signal (noisy; use late):
```
location:"San Francisco" language:python
```
Fragile LinkedIn public substitute (shelf-life; titles only via advice pages):
```
site:linkedin.com/advice/ intext:"Director of Engineering"
```

## Iterate
Broad → sharpen synonyms → add location only if needed → switch surface (repos vs code vs PRs vs users).

## Deliverable shape
Name, GitHub profile + key repo/PR evidence, inferred focus, public LinkedIn URL if found without signed-in personal session, match notes, Active notes (separate score).

## Sources to refresh from
- https://fullstackrecruiter.net/guides/boolean-and-x-ray-search-for-recruiters/
- https://github.com/ohsusannamarie/GitHub-advanced-search
