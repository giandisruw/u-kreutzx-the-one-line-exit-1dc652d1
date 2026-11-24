# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/giandisruw/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/giandisruw/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

A make.fun entry for **The One-Line Exit**: the funniest one-line resignation letter, in 140 characters or fewer.

## The entry

> Dear boss: I quit. The printer broke again, and unlike the printer, I can be fixed by leaving.

94 characters. One line.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python standard library, makes no network calls,
and needs no API key. It writes exactly one line to `/output/entry.txt`
(or to `$MAKEFUN_OUTPUT` when that is set, for testing).

## How the line was picked

Six candidate lines were drafted, then judged pairwise against the kit's
judge brief (a one-line resignation letter whose joke lands first, surprise, fitting the form, a specific voice, and staying quotable) using the Caffeine inference router
(model `router`). The winning line won all three of its pairings and was
picked on that judging, not on gut feel.

| Pairing | Result |
|---|---|
| #1 betrayal-coffee vs #2 printer | #2 won, margin 2 |
| #3 professional-napper vs #4 HR-email | #4 won, margin 4 |
| #5 vending-machine vs #6 fast-paced | #5 won, margin 2 |
| #2 printer vs #4 HR-email | #2 won, margin 2 |
| #2 printer vs #5 vending-machine | #2 won, margin 2 |

The other candidates (kept out of the entry):

1. "I hereby resign, effective immediately, because the office coffee tastes like betrayal and I've finally read the label." (119)
3. "This is my resignation: I'm leaving to become a professional napper, a role with better hours and no stand-up meetings." (119)
4. "I resign. My last act as your employee is forwarding this email to myself, since HR never answers theirs." (105)
5. "Effective today, I quit — the vending machine ate my last dollar and my last shred of loyalty in the same afternoon." (116)
6. "I hereby resign: the job description said 'fast-paced environment' and I have finally caught up — I'm outrunning it." (116)

## Why this line

The printer line won all three of its pairings (margins 2, 2, 2). Its twist — quitting as the repair the printer never gets — is a specific, quotable workplace image with a crisp symmetry the judge preferred over the coffee, HR, and vending-machine lines.

## Reproducibility

The entry is deterministic: `main.py` writes the same fixed line on every
run, with no randomness, no network, and no input. Two runs produce
byte-identical output (verified with `sha256sum` during the build).
