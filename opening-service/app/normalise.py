"""Normalises the moves, from the PGN format to a more db friendly format
Example:

Input:
1. e4 e5 2. Nf3 Nc6 3. Bb5

Output:
e4 e5 Nf3 Nc6 Bb5
"""

import re


def normalise_pgn(pgn: str) -> str:
    if not pgn or not pgn.strip():
        return ""

    without_move_numbers = re.sub(
        r"\d+\.(?:\.\.)?\s*",
        "",
        pgn,
    )

    return " ".join(without_move_numbers.split())


def ply_count(moves: str) -> int:
    if not moves:
        return 0

    return len(moves.split())