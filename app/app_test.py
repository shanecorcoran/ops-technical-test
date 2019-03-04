from copy import deepcopy
import unittest
import json
import urllib2

import app

BASE_URL = 'http://127.0.0.1:5000/'
METADATA_URL = 'http://127.0.0.1:5000/todo/api/v1.0/myapplication'
HEALTHCHECK_URL = 'http://127.0.0.1:5000/healthcheck'

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.backup_items = deepcopy(app.myapplication)  # no references!
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_myapplication(self):
        response = self.app.get(METADATA_URL)
        self.assertEqual(response.status_code, 200)

    def test_get_healthcheck(self):
        response = self.app.get(HEALTHCHECK_URL)
        self.assertEqual(response.status_code, 200)

    def test_get_root(self):
        response = urllib2.urlopen(BASE_URL)
        self.assertEqual(response.code, 200)

    def tearDown(self):
        # reset app.items to initial state
        app.items = self.backup_items

if __name__ == "__main__":
    unittest.main()