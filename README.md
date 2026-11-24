# Say What Actually Broke

[![Say What Actually Broke](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/cervus-snoopy/misty-blunt-error-4m8q/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/cervus-snoopy/misty-blunt-error-4m8q/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

A Python program that writes one brutally honest, funny error line about a disk eaten by its own logs.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Writes exactly one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
with no trailing newline and mode `0644`.

## Verify

```sh
python3 -c "import pathlib; p = pathlib.Path('/output/entry.txt'); t = p.read_text(encoding='utf-8'); assert 1 <= len(t) <= 200 and '\n' not in t and t.strip(); print(len(t), 'chars, OK')"
```
