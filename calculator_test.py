#!/usr/bin/env python3
"""
These are the unit tests for the calculator library
"""

import unittest
#import sys
#sys.path.insert(0, 'C:/Users/Jai Devani/Desktop/Sample/Calculator')
import calculator_main as calculator

class Test(unittest.TestCase):

    def test_addition(self):
        assert 40.0 == calculator.addition(20, 20)

    def test_subtraction(self):
        assert 2.0 == calculator.subtraction(4, 2)

    def test_multiplication(self):
        assert 16.0 == calculator.multiplication(4, 4)

    def test_division(self):
        assert 25.0 == calculator.division(125, 5)
        assert "The arguments provided are invalid." == calculator.division(0, 0)
        assert "The arguments provided are invalid." == calculator.division(10, 0)
        assert "The arguments provided are invalid." == calculator.division(0, 10)

    def test_sqrt(self):
        assert 4.0 == calculator.square_root(16)
        assert "The arguments provided are invalid." == calculator.square_root(-100)
    def test_factorial(self):
        assert 120.0 == calculator.factorial(5)

    def test_power(self):
        assert 729.0 == calculator.power(9, 3)
        
    def test_modulus(self):
        assert 1.0 == calculator.modulus(4, 3)

    def test_cos(self):
        assert 0.0 == calculator.cos(90)

    def test_sin(self):
        assert 1.0 == calculator.sin(90)

    def test_tan(self):
        assert 1.0 == calculator.tan(45)
    
    def test_log(self):
        assert 1.58 == calculator.log(3, 2)
        assert "The arguments provided are invalid." == calculator.log(10, 0)
        assert "The arguments provided are invalid." == calculator.log(0, 10)
        
    if __name__ == '__main__':
        unittest.main()
