from app import predict_grade


def test_grade_a():
    assert predict_grade(95) == "A"


def test_grade_b():
    assert predict_grade(80) == "B"


def test_grade_c():
    assert predict_grade(60) == "C"


def test_fail_student():
    assert predict_grade(30) == "FAIL"