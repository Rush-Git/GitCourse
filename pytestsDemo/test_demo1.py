import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_firstProgram():
    print("Hello")


#@pytest.mark.skip
def test_secondProgram(setup):
    print("GM")


def test_crossBrwoser(crossBrwoser):
    print(crossBrwoser[1])
