#!/usr/bin/env python3
"""Convert a LinkedIn activity id to UTC time. No network, no login."""
import sys
from datetime import datetime, timezone

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        raise SystemExit("usage: activity_time.py <activity_id>")
    activity_id = int(sys.argv[1])
    moment = datetime.fromtimestamp((activity_id >> 22) / 1000, timezone.utc)
    age_days = (datetime.now(timezone.utc) - moment).days
    if age_days < 0 or moment.year < 2008 or moment.year > datetime.now(timezone.utc).year + 1:
        raise SystemExit("timestamp is not a plausible LinkedIn activity date")
    if age_days <= 30:
        window = "within_30d"
    elif age_days <= 90:
        window = "within_90d"
    else:
        window = "older_than_90d"
    print(f"{moment.isoformat()} age_days={age_days} window={window}")

if __name__ == "__main__":
    main()
