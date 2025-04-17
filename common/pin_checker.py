# common/pin_checker.py

def load_common_pins():
    with open("data/common_mpin.txt", "r") as f:
        return set(line.strip() for line in f if line.strip())

COMMON_PINS = load_common_pins()

def is_common_pin(pin: str) -> bool:
    """Return True if pin is in the top common-PIN list."""
    return pin in COMMON_PINS
