#!/usr/bin/env python

import unittest

if __name__ == "__main__":
    """Run all unit tests in the tests directory"""
    testSuite = unittest.defaultTestLoader.discover("./")
    unittest.TextTestRunner().run(testSuite)
