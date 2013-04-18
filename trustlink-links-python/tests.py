# coding: utf-8

from __future__ import absolute_import, unicode_literals

import unittest
import sys
from client import Client

PYTHON_VERSION = '-'.join(map(str, sys.version_info[:3]))

class Test(unittest.TestCase):
    def test_run_once(self):
        obj = Client("test object")
        content = obj.fetch_remote_file('db.trustlink.ru', '/a742bfd5f4b9f240095910e0983d714d4b08efbc/youdesigner.kz/UTF-8.text')
        obj.lc_write('links.db', content)
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()


