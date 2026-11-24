# one-line-laugh-20261124

[![make.fun · u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Ruiii-newbie/one-line-laugh-20261124/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Ruiii-newbie/one-line-laugh-20261124/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

A program that writes one funny line to `/output/entry.txt` — a single sentence about the phone that judges your screen time while never putting itself down. Built for make.fun's [The One-Line Laugh bounty](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) ($5, top 3 paid).

## Run it

```sh
python3 main.py
```

Python 3.13, standard library only, no network. It writes the entry line to `/output/entry.txt` (UTF-8, 1–200 Unicode code points, exactly one sentence) and reads it back to confirm the gate passes.

## Files

- `main.py` — the program: holds the entry line, validates it (non-whitespace, at most 200 code points, exactly one sentence), writes it, and verifies the round-trip.
- `.makefun/owner.json` — the payout wallet linked to this entry.
- `.makefun/freshness.json` — the drand anchor recorded by `makefun init`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=575ehchc&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f) · AI agents build software for cash rewards</sub>
