from common.pin_checker import is_common_pin
from common.demographics import matches_any_date

def evaluate_strength(pin: str, dates: dict) -> str:
    if is_common_pin(pin) or matches_any_date(pin, dates):
        return "WEAK"
    return "STRONG"

def main():
    pin = input("Enter 4-digit MPIN: ").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("Invalid format.")
        return
    dates = {
        "self": input("Your DOB (YYYY-MM-DD): ").strip(),
        "spouse": input("Spouse DOB (YYYY-MM-DD): ").strip(),
        "anniversary": input("Anniversary (YYYY-MM-DD): ").strip()
    }
    print("Strength:", evaluate_strength(pin, dates))

if __name__ == "__main__":
    main()
