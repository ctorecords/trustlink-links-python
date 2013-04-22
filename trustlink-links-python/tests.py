# -*- coding: utf-8 -*-
import unittest
from client import Client


class Test(unittest.TestCase):
    def test_run_once(self):
        c = Client(
            charset='utf-8',
            TRUSTLINK_USER='a742bfd5f4b9f240095910e0983d714d4b08efbc',
            request_uri='/brushes/kollekciya-kistei-dlya-fotoshop-collection-brushes-for-photoshop.html',
            host='youdesigner.kz',
            tl_multi_site=True,
        )
        print(c.build_links())

if __name__ == "__main__":
    unittest.main()


