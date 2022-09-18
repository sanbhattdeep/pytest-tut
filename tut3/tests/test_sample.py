import sys

import pytest

from tut3.myapp.sample import add


@pytest.mark.skip(reason="Just like that")
def test_add_num():
    assert add(1, 2) == 3


@pytest.mark.skipif(sys.version_info > (3, 8), reason="python version is > 3.8")
def test_add_str():
    assert add("a", "b") == "ab"


@pytest.mark.xfail(sys.platform == "linux", reason="dont run on linux")
def test_add_list():
    assert add([1], [2]) == [1, 2]
    raise Exception
