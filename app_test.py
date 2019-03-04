from copy import deepcopy
import unittest
import json

import app

BASE_URL = 'http://127.0.0.1:5000/'

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.backup_items = deepcopy(app.items)  # no references!
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        # reset app.items to initial state
        app.items = self.backup_items

if __name__ == "__main__":
    unittest.main()