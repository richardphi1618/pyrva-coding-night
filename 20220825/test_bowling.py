import pytest
import bowling


@pytest.mark.xfail
@pytest.mark.parametrize(
    ["rolls", "score"],
    [
        ("X X X X X X X X X XXX", 300),
        ("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5", 150),
        ("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-", 90),
    ],
    ids=["strikes", "spares", "no-marks"],
)
def test_can_correctly_calculate_score(rolls, score):
    assert bowling.score(rolls) == score


@pytest.mark.parametrize(
    ["rolls", "frames"],
    [
        ("X X X X X X X X X XXX", 10),
        ("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5", 10),
        ("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-", 10),
    ],
    ids=["strikes", "spares", "no-marks"],
)
def test_correct_number_of_frames(rolls, frames):
    assert len(bowling.get_frames(rolls)) == frames


@pytest.mark.xfail
def test_can_calculate_simple_score():
    example = "2-"
    result = bowling.score(example)
    assert result == 2


@pytest.mark.xfail
def test_can_calculate_one_throw():
    throw = "3"
    assert bowling.score(throw) == 3


@pytest.mark.parametrize("rolls, score", [("45", 9), ("5-", 5), ("5/", 10), ("X", 10)])
def test_score_single_frame(rolls, score):
    assert bowling.score(rolls) == score


def test_can_calculate_a_zero_score():
    assert bowling.score("") == 0
