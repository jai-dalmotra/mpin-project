# PartA_CommonCheck.py

from common.pin_checker import is_common_pin

def main():
    mpin = input("Enter your 4-digit MPIN: ").strip()
    if len(mpin) != 4 or not mpin.isdigit():
        print("Invalid MPIN format. Must be 4 digits.")
        return

    if is_common_pin(mpin):
        print("MPIN is COMMONLY USED.")
    else:
        print("MPIN is NOT COMMON.")

if __name__ == "__main__":
    main()
