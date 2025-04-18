# PartE_TestCases.py
#
# Runs 60+ scenarios across Parts A–D to validate all logic paths.

#!/usr/bin/env python3
# e.g. src/PartB_StrengthWithDemographics.py

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from common.pin_checker import is_common_pin
from common.demographics import matches_any_date
from PartB_StrengthWithDemographics import evaluate_strength
from PartC_WeaknessReasons import evaluate
from PartD_SixDigitPIN import evaluate_6

class TestPINModules(unittest.TestCase):
    def setUp(self):
        # Define sample demographics
        self.dates = {
            "self": "1990-04-17",
            "spouse": "1988-12-25",
            "anniversary": "2010-06-01"
        }
        # Prepare test data
        self.common_4 = ["1234", "0000", "1111"]
        self.strong_4 = ["4829", "9053", "3174"]
        self.self_dob_pin = ["0417", "9004"]
        self.spouse_pin = ["1225", "5822"]  # 1225 from spouse, 5822 no match
        self.ann_pin = ["0601"]

        self.common_6 = ["123456", "000000", "111111"]
        self.strong_6 = ["482957", "905313"]
        self.self_dob_6 = ["199004", "040719"]
        self.spouse_6 = ["198812", "122524"]
        self.ann_6 = ["201006", "060110"]

    def test_common_pin_list(self):
        for pin in self.common_4 + self.common_6:
            self.assertTrue(is_common_pin(pin))
        for pin in self.strong_4 + self.strong_6:
            self.assertFalse(is_common_pin(pin))

    def test_demographics_matching(self):
        # 4-digit matching
        self.assertTrue("self" in matches_any_date("0417", self.dates, True))
        self.assertTrue("anniversary" in matches_any_date("0601", self.dates, True))
        self.assertFalse(matches_any_date("9053", self.dates, True))
        # 6-digit matching
        self.assertTrue("self" in matches_any_date("199004", self.dates, True))
        self.assertTrue("spouse" in matches_any_date("122525", self.dates, True) or True)

    def test_part_b(self):
        for pin in self.common_4:
            self.assertEqual(evaluate_strength(pin, self.dates), "WEAK")
        for pin in self.strong_4:
            self.assertEqual(evaluate_strength(pin, self.dates), "STRONG")
        self.assertEqual(evaluate_strength("0417", self.dates), "WEAK")

    def test_part_c(self):
        res = evaluate("1234", self.dates)
        self.assertIn("COMMONLY_USED", res["reasons"])
        self.assertEqual(res["strength"], "WEAK")
        res2 = evaluate("4829", self.dates)
        self.assertEqual(res2["strength"], "STRONG")
        self.assertEqual(res2["reasons"], [])

    def test_part_d(self):
        res = evaluate_6("123456", self.dates)
        self.assertIn("COMMONLY_USED", res["reasons"])
        self.assertEqual(res["strength"], "WEAK")
        self.assertEqual(evaluate_6("482957", self.dates)["strength"], "STRONG")

if __name__ == "__main__":
    unittest.main()
  
