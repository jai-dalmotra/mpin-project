# PartD_SixDigitPIN.py
#
# Identical logic to Part C, but for 6-digit PINs.

#!/usr/bin/env python3
# e.g. src/PartB_StrengthWithDemographics.py

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from common.pin_checker import is_common_pin
from common.demographics import matches_any_date

REASON_COMMON = "COMMONLY_USED"
REASON_DOB_SELF = "DEMOGRAPHIC_DOB_SELF"
REASON_DOB_SPOUSE = "DEMOGRAPHIC_DOB_SPOUSE"
REASON_ANN = "DEMOGRAPHIC_ANNIVERSARY"

def evaluate_6(pin: str, dates: dict) -> dict:
    if is_common_pin(pin):
        reasons = [REASON_COMMON]
    else:
        reasons = []

    matched = matches_any_date(pin, dates, return_keys=True)
    for key in matched:
        if key == "self":
            reasons.append(REASON_DOB_SELF)
        elif key == "spouse":
            reasons.append(REASON_DOB_SPOUSE)
        elif key == "anniversary":
            reasons.append(REASON_ANN)

    strength = "WEAK" if reasons else "STRONG"
    return {"strength": strength, "reasons": reasons}

def main():
    pin = input("Enter 6-digit MPIN: ").strip()
    if len(pin) != 6 or not pin.isdigit():
        print("Invalid format. Must be exactly 6 digits.")
        return

    dob = input("Your DOB (YYYY-MM-DD): ").strip()
    spouse_dob = input("Spouse DOB (YYYY-MM-DD): ").strip()
    anniversary = input("Anniversary (YYYY-MM-DD): ").strip()

    dates = {"self": dob, "spouse": spouse_dob, "anniversary": anniversary}
    result = evaluate_6(pin, dates)
    print(f"Strength: {result['strength']}")
    print("Reasons:", result["reasons"])

if __name__ == "__main__":
    main()
