import sys
sys.path += ["../"]

import mingus.extra.tablature as tablature
import unittest

class test_Tablature(unittest.TestCase):
	
	def setUp(self):
		pass


def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_Tablature)
