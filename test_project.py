from project import quizz, difficulty, timer, score


def test_quizz ():
    assert difficulty (4) == "Level : Easy"
    assert score (9) == "Your score is 90%, Excellent 👍🙂"


def test_difficulty ():
    assert difficulty (4) == "Level : Easy"
    assert difficulty (10) == "Level : Medium"
    assert difficulty (20) == "Level : Hard"


def test_timer ():
    assert timer ("Level : Easy") == 5
    assert timer ("Level : Medium") == 7
    assert timer ("Level : Hard") == 10


def test_score ():
    assert score (5) == "Your score is 50%, Not enough 👎🙁"
    assert score (6) == "Your score is 60%, Good job 👍"
    assert score (10) == "Your score is 100%, Excellent 👍🙂"

