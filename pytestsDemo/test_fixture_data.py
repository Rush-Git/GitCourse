import pytest
import logging

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def test_editProfile(self, dataload):
        log = self.getlogger()
        log.info(dataload[2])
        log.warning(dataload[1])
