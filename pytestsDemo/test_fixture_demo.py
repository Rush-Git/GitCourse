import pytest


@pytest.mark.usefixtures("setup")
class TestExcamples:

    def test_fixtureDemo1(self):
        print("I will be executing the methods in fixture demo")

    def test_fixtureDemo2(self):
        print("I will be executing the methods in fixture demo")

    def test_fixtureDemo3(self):
        print("I will be executing the methods in fixture demo")

    def test_fixtureDemo4(self):
        print("I will be executing the methods in fixture demo")
