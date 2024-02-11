#!/usr/bin/python3

import unittest

class ModelTest(unittest.TestCase):
    def test(self):
        from subprocess import check_output as co

        self.assertIs (
                co(['sh', '-c', 'ls /tmp/correction/corrections_*/corrections/263/**']).decode(),
                True,
        )
        ...

if __name__ == '__main__':
    unittest.main()
