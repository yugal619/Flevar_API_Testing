import pytest
import requests
import json
import logging
from Admin.utils.body_data import body_data
from Admin.utils.url_paths import Path

log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.usefixtures("set_authentication", "testcase_fixture")
class Test025:

    @pytest.fixture(scope='class')
    def testcase_fixture(self, get_body):
        get_body(body_data.get_save_product_category)

    def test_025_save_success(self):
        response = requests.post(self.BASE_URL + Path.product_category, headers=self.header,
                                        data=json.dumps(self.body))

        assert response.status_code == 200, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is True, '[FAILED] Success is False'
        assert response.json()['reason'] == 'Record added successfully',\
            '[FAILED] Record is not added successfully'

    def test_025_save_failure(self):
        response = requests.post(self.BASE_URL + Path.product_category, headers=self.header,
                                 data=json.dumps(self.body))
        assert response.status_code == 422, '[FAILED] Response Error [{}]'.format(response.status_code)
        assert response.json()['success'] is False, '[FAILED] Success is True'
        assert response.json()['reason']['name'][0] == 'The name has already been taken.',\
            '[FAILED] The name has already been taken.'
