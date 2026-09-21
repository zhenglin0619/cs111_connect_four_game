# Connect Four Game

A terminal-based Connect Four game written in Python for Computer Science 111 at Boston University. Play against another person, a random computer player, or a computer player that scores moves with a configurable lookahead.

## Requirements

- Python 3
- No third-party packages

## Start a game

From the repository directory, open the script in Python's interactive mode:

```bash
python3 -i "Connect Four Game.py"
```

At the `>>>` prompt, choose two players with different checkers:

```python
connect_four(Player('X'), Player('O'))
```

Other matchups:

```python
connect_four(Player('X'), RandomPlayer('O'))
connect_four(Player('X'), AIPlayer('O', 'RANDOM', 2))
connect_four(RandomPlayer('X'), RandomPlayer('O'))
```

The script defines the game but does not start one automatically when run normally. Exit interactive Python with `exit()`.

## How to play

The game uses a 6-row, 7-column board. Players take turns placing `X` or `O` in a column numbered `0` through `6`; the checker falls to the lowest open space. The first player to connect four checkers horizontally, vertically, or diagonally wins. A full board without a winner is a tie.

For a human player, type a column number when prompted. Pick a column that still has space.

## Player types

| Player | Behavior |
| --- | --- |
| `Player('X')` | Asks a person to choose each move. |
| `RandomPlayer('O')` | Picks randomly from columns that are not full. |
| `AIPlayer('O', 'LEFT', 2)` | Scores columns using the given lookahead depth and breaks tied scores according to the selected rule. |

`AIPlayer` accepts `LEFT`, `RIGHT`, or `RANDOM` as its tiebreak rule and a nonnegative integer as its lookahead depth. Larger depths take longer to calculate.

## License

Licensed under the [Apache License 2.0](LICENSE).
