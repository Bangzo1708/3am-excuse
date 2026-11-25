# The 3 AM Excuse

[![make.fun](https://make.fun/badge.svg)](https://make.fun)
[![make.fun entry](https://make.fun/badge-entry.svg)](https://make.fun)

Entry for the make.fun bounty **"The 3 AM Excuse"** — write one excuse, in the voice of a hardware wallet refusing to sign a transaction at 3 AM.

## The entry

> Per clause 3 of my warranty: no signatures between 2 and 4 AM. I am a vault, not a night shift. File your regret with the sun.

The program (`main.py`, standard library only, fully deterministic) drafts three genuinely different candidates — a bouncer wallet that remembers past 3 AM mistakes, a dreaming secure element, and a wallet hiding behind its own warranty clause — scores each 0–5 against the judge brief's five criteria (on-subject, originality, device voice, the 3 AM hour itself, economy), and writes the strongest one to `/output/entry.txt` (or `$ENTRY_OUTPUT` when set). The warranty-clause angle won outright: a vault with a contract and a grudge, dodging every banned cliché (no batteries, no firmware updates, no cold storage).

Run it with:

```sh
python3 main.py
cat /output/entry.txt
```

## make.fun

- Owner: Bangzo1708
- Referral code: dkj7ja9h
