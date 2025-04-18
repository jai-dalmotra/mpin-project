#!/usr/bin/env python3
# src/CombinedTests.py

import os, sys
# Prepend the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

"""
Unified test runner. Invoke with:
  python -m src.CombinedTests --part all
"""
import argparse
import unittest

# Imports now succeed because project root is on sys.path when run via -m
from common.pin_checker import is_common_pin
from common.demographics import matches_any_date
from src.PartB_StrengthWithDemographics import evaluate_strength
from src.PartC_WeaknessReasons import evaluate as evaluate_c
from src.PartD_SixDigitPIN import evaluate_6

class TestPartA(unittest.TestCase):
    def test_common_and_uncommon(self):
        self.assertTrue(is_common_pin("1234"))
        self.assertFalse(is_common_pin("4829"))

class TestPartB(unittest.TestCase):
    def setUp(self):
        self.dates = {
            "self": "1990-04-17",
            "spouse": "1988-12-25",
            "anniversary": "2010-06-01"
        }
    def test_strength_weak(self):
        self.assertEqual(evaluate_strength("1234", self.dates), "WEAK")
    def test_strength_strong(self):
        self.assertEqual(evaluate_strength("4829", self.dates), "STRONG")

class TestPartC(unittest.TestCase):
    def setUp(self):
        self.dates = {
            "self": "1990-04-17",
            "spouse": "1988-12-25",
            "anniversary": "2010-06-01"
        }
    def test_reasons_common(self):
        res = evaluate_c("1234", self.dates)
        self.assertIn("COMMONLY_USED", res["reasons"])
        self.assertEqual(res["strength"], "WEAK")
    def test_reasons_dob(self):
        res = evaluate_c("0417", self.dates)
        self.assertIn("DEMOGRAPHIC_DOB_SELF", res["reasons"])

class TestPartD(unittest.TestCase):
    def setUp(self):
        self.dates = {
            "self": "1990-04-17",
            "spouse": "1988-12-25",
            "anniversary": "2010-06-01"
        }
    def test_six_common(self):
        res = evaluate_6("123456", self.dates)
        self.assertIn("COMMONLY_USED", res["reasons"])
    def test_six_strong(self):
        res = evaluate_6("482957", self.dates)
        self.assertEqual(res["strength"], "STRONG")

def load_suite_for_part(part: str) -> unittest.TestSuite:
    """Dynamically load tests for a given part."""
    loader = unittest.TestLoader()
    name_map = {"A": TestPartA, "B": TestPartB, "C": TestPartC, "D": TestPartD}
    if part not in name_map:
        raise ValueError(f"Unknown part: {part}")
    return loader.loadTestsFromTestCase(name_map[part])

def main():
    parser = argparse.ArgumentParser(
        description="Run MPIN project tests (Parts A–D)."
    )
    parser.add_argument(
        "--part",
        choices=["all", "A", "B", "C", "D"],
        default="all",
        help="Which part’s tests to run (default: all)"
    )
    args = parser.parse_args()

    runner = unittest.TextTestRunner(verbosity=2)
    if args.part == "all":
        # Discover any test cases in this file
        suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    else:
        suite = load_suite_for_part(args.part)

    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)

if __name__ == "__main__":
    main()
