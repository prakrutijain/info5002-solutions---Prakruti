
import logging
import unittest

from ipp.exercises.labmodule05.CalculationsUtil import CalculationsUtil

class CalculationsUtilTest(unittest.TestCase):
	@classmethod

	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing CalculationsUtil class...")
		
	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def testDivideTwoIntegers(self):
		self.assertEqual(0.0, CalculationsUtil.divideTwoNumbers(1, 0))
		self.assertEqual(5.0, CalculationsUtil.divideTwoNumbers(10, 2))
		self.assertEqual(2.0, CalculationsUtil.divideTwoNumbers(10, 5))
		self.assertEqual(1.0, CalculationsUtil.divideTwoNumbers(10, 10))
		pass
	
		# Add other tests if you'd like
	
	def testDivideTwoFloats(self):
		self.assertEqual(0.0, CalculationsUtil.divideTwoNumbers(1.5, 0))
		self.assertEqual(5.5, CalculationsUtil.divideTwoNumbers(11, 2))
		self.assertEqual(2.5, CalculationsUtil.divideTwoNumbers(5, 2))
		self.assertEqual(1.5, CalculationsUtil.divideTwoNumbers(1.5, 1.0))
		pass
		# Add other tests if you'd like
		
	def testFarenheitToCelsiusConversion(self):
		 
        # Test 32F -> 0C
		self.assertEqual(0.0, CalculationsUtil.convertTempFtoC(32))
		# Test 212F -> 100C
		self.assertEqual(100.0, CalculationsUtil.convertTempFtoC(212))
		
		pass
	
	def testCelsiusToFarenheitConversion(self):
		 # Test 0C -> 32F
		self.assertEqual(32.0, CalculationsUtil.convertTempCtoF(0))
		# Test 100C -> 212F
		self.assertEqual(212.0, CalculationsUtil.convertTempCtoF(100))
	
		pass
		
if __name__ == '__main__':
	unittest.main()