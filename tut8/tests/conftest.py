from datetime import datetime

import pytest

from tut8.myapp.student import Student


@pytest.fixture
def dummy_student(request):
    print("making dummy student")
    return Student("sandeep", datetime(1982, 3, 20), "IS", request.param)


@pytest.fixture
def make_dummy_student():
    def make_dummy_student(name, credits):
        return Student(name, datetime(1982, 3, 20), "IS", credits)

    return make_dummy_student

