import pytest
import requests
import json
import logging


@pytest.mark.usefixtures("set_authentication")
class Test002:
    def test_002(self):
        logging.warning('This is a --------------- message {} {}'.format(self.header, self.BASE_URL))
        logging.error('This is an error message')
        pass
