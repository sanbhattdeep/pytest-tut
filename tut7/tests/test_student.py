from datetime import datetime

import pytest

from tut7.myapp.student import Student, get_topper


def test_get_topper(make_dummy_student):
    students = [make_dummy_student("Sandeep", 21),
                make_dummy_student("Deepika", 19),
                make_dummy_student("Latha", 22)
                ]

    topper = get_topper(students)

    assert topper == students[2]




def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 20