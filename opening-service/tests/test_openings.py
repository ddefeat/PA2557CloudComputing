import pytest

from app.db import open_pool, close_pool, get_opening_by_id, get_openings

CORRECT_OPENINGS_IDS = [1, 2, 3, 4]
WRONG_OPENINGS_IDS = [-1, 0, 67326127386,
                      "ruy-lopez is not an opening or is it??",
                      "Sacrifice the king is the best defence"]

# Note: Db needs to run for the tests to work
# Set up connection
open_pool()

def test_correct_openings_by_id_not_returning_error():
    resp = []
    for _id in CORRECT_OPENINGS_IDS:
        resp.append(get_opening_by_id(_id))
    assert resp[0] == [(1, 'Amar Opening', '1. Nh3', 'Nh3')]
    assert resp[1] == [(2, 'Amar Opening: Paris Gambit', '1. Nh3 d5 2. g3 e5 3. f4', 'Nh3 d5 g3 e5 f4')]
    assert resp[2] == [(3, 'Amar Opening: Paris Gambit, Gent Gambit', '1. Nh3 d5 2. g3 e5 3. f4 Bxh3 4. Bxh3 exf4 5. O-O fxg3 6. hxg3', 'Nh3 d5 g3 e5 f4 Bxh3 Bxh3 exf4 O-O fxg3 hxg3')]
    assert resp[3] == [(4, 'Amsterdam Attack', '1. e3 e5 2. c4 d6 3. Nc3 Nc6 4. b3 Nf6', 'e3 e5 c4 d6 Nc3 Nc6 b3 Nf6')]

def test_incorrect_openings_by_id():
    resp = []
    for _id in WRONG_OPENINGS_IDS:
        resp.append(get_opening_by_id(_id))
    for r in resp:
        assert r == []