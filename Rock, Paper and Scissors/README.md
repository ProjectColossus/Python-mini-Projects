# Rock, Paper, Scissors

A command-line Rock, Paper, Scissors game against the computer — play as many 
rounds as you want, with live win/loss/tie tracking. Part of my Python Mini 
Projects series, applying fundamentals from my 
[30 Days of Python](https://github.com/ProjectColossus/30-days-of-python) log.


## How It Works

1. Choose your move: `r` (rock), `p` (paper), `s` (scissors), or `q` to quit
2. The computer picks randomly
3. Standard rules decide the round:
   - Rock beats Scissors
   - Paper beats Rock
   - Scissors beats Paper
4. Your running win/loss/tie count is shown before every round
5. Keep playing until you quit with `q`

## Run It

```bash
python RockPaperScissors.py
```

## Concepts Covered

| Concept | Where it shows up |
|---|---|
| **Loops (`while True`)** | Outer loop keeps the game running across rounds; inner loop re-prompts until valid input is given |
| **Input validation** | Inner loop rejects anything other than `r`, `p`, `s`, or `q` before continuing |
| **The `random` module** | `random.randint(1, 3)` generates the computer's move |
| **The `sys` module** | `sys.exit()` cleanly ends the program on quit |
| **State tracking with variables** | `wins`, `losses`, `ties` counters persist and update across the loop |
| **Conditional logic** | Nested `if`/`elif` chains determine round outcomes and control the input loop |
| **String formatting** | `%s` old-style formatting used to print the running score |

## Code Walkthrough

**Outer `while True` loop** — runs the whole game session. Each pass is one 
round: get input, get computer's move, compare, update score, repeat.

**Inner `while True` loop** — dedicated purely to getting *valid* input. It 
keeps prompting until the player enters `r`, `p`, `s`, or `q`, so invalid 
input never breaks the game (unlike a naive single-prompt approach).

**Score tracking** — `wins`, `losses`, and `ties` are plain integer counters 
initialized once outside the loop and incremented inside it, printed at the 
top of each round so the player always sees where they stand.

## Sample Output

```
ROCK, PAPER, SCISSORS
0 wins, 0 losses, 0 ties
Rocks(r),papers(p),Scissors(s) or quit(q): r
ROCK versus...
SCISSOR
you lose
1 wins, 1 losses, 0 ties
Rocks(r),papers(p),Scissors(s) or quit(q): q

```
*Part of my [Python Mini Projects](.) series — practical, small-scale 
applications of fundamentals covered in 30 Days of Python.*
