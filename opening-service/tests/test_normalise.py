import pytest

from app.normalise import normalise_pgn, ply_count


@pytest.mark.parametrize(
    ("pgn", "expected"),
    [
        (
            "1. e4 e5 2. Nf3 Nc6 3. Bb5",
            "e4 e5 Nf3 Nc6 Bb5",
        ),
        (
            "1. O-O O-O-O 2. e8=Q+ Qh7#",
            "O-O O-O-O e8=Q+ Qh7#",
        ),
        (
            "  1. e4   e5  2. Nf3  ",
            "e4 e5 Nf3",
        ),
        (
            "",
            "",
        ),
        (
            "   ",
            "",
        ),
    ],
)
def test_normalise_pgn(pgn, expected):
    assert normalise_pgn(pgn) == expected


def test_ply_count():
      assert ply_count("e4 e5 Nf3 Nc6 Bb5") == 5
      assert ply_count("") == 0