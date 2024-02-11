#!/usr/bin/python3

import unittest

class ModelTest(unittest.TestCase):
    def test(self):
        import os
        os.system('ls /tmp/correction/corrections_*')
        ...

if __name__ == '__main__':
    unittest.main()
