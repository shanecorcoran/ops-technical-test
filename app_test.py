from copy import deepcopy
import unittest
import json

import app

BASE_URL = 'http://127.0.0.1:5000/todo/api/v1.0/myapplication'
HEALTHCHECK_URL = 'http://127.0.0.1:5000/healthcheck'

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.backup_items = deepcopy(app.myapplication)  # no references!
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_myapplication(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        return data

    def test_get_healthcheck(self):
        response = self.app.get(HEALTHCHECK_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(len(data['myapplication']), 1)

    def tearDown(self):
        # reset app.items to initial state
        app.items = self.backup_items

if __name__ == "__main__":
    unittest.main()