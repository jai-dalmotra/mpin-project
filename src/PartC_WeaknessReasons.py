# PartC_WeaknessReasons.py
#
# Extends Part B to return reasons for weakness:
# COMMONLY_USED, DEMOGRAPHIC_DOB_SELF,
# DEMOGRAPHIC_DOB_SPOUSE, DEMOGRAPHIC_ANNIVERSARY.

from common.pin_checker import is_common_pin
from common.demographics import matches_any_date

REASON_COMMON = "COMMONLY_USED"
REASON_DOB_SELF = "DEMOGRAPHIC_DOB_SELF"
REASON_DOB_SPOUSE = "DEMOGRAPHIC_DOB_SPOUSE"
REASON_ANN = "DEMOGRAPHIC_ANNIVERSARY"

def evaluate(pin: str, dates: dict) -> dict:
    """
    Returns a dict with:
      - 'strength': "WEAK"/"STRONG"
      - 'reasons': list of reason codes (empty if STRONG)
    """
    reasons = []
    if is_common_pin(pin):
        reasons.append(REASON_COMMON)
    # matches_any_date now returns which keys matched
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
    pin = input("Enter 4-digit MPIN: ").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("Invalid format. Must be exactly 4 digits.")
        return

    dob = input("Your DOB (YYYY-MM-DD): ").strip()
    spouse_dob = input("Spouse DOB (YYYY-MM-DD): ").strip()
    anniversary = input("Anniversary (YYYY-MM-DD): ").strip()

    dates = {"self": dob, "spouse": spouse_dob, "anniversary": anniversary}
    result = evaluate(pin, dates)
    print(f"Strength: {result['strength']}")
    print("Reasons:", result["reasons"])

if __name__ == "__main__":
    main()
