import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will vbe executed at the last")


@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Rushaida", "Ummar", "rushaidha.a.ummar@gmail.com"]


@pytest.fixture(params=[("chrome", "Rush", "Ummar"), ("Edge", "Irsha"), ("IE", "Zahra")])
def crossBrwoser(request):
    return request.param
