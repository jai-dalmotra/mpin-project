## `docs/usage.md`


# Usage Examples

This document shows how to run each Part and the combined test runner.

---

## Part A: Common PIN Checker (4 digits)

```bash
$ python src/PartA_CommonCheck.py
Enter your 4-digit MPIN: 1234
MPIN is COMMONLY USED.
```
## Invalid format example

```bash
$ python src/PartA_CommonCheck.py
Enter your 4-digit MPIN: 12a4
Invalid MPIN format. Must be 4 digits.

```
## Part B: Strength Check with Demographics (4 digits)
```
$ python src/PartB_StrengthWithDemographics.py
Enter 4-digit MPIN: 4829
Your DOB (YYYY-MM-DD): 1990-04-17
Spouse DOB (YYYY-MM-DD): 1988-12-25
Anniversary (YYYY-MM-DD): 2010-06-01
Strength: STRONG

```
## Weak example

```
$ python src/PartB_StrengthWithDemographics.py
Enter 4-digit MPIN: 0417
Your DOB: 1990-04-17
...
Strength: WEAK

```

## Part C: Weakness Reasons (4 digits)

```bash
$ python src/PartC_WeaknessReasons.py
Enter 4-digit MPIN: 0417
Your DOB (YYYY-MM-DD): 1990-04-17
Spouse DOB (YYYY-MM-DD): 1988-12-25
Anniversary (YYYY-MM-DD): 2010-06-01

Strength: WEAK
Reasons: ['DEMOGRAPHIC_DOB_SELF']

```
```bash
$ python src/PartC_WeaknessReasons.py
Enter 4-digit MPIN: 1234
...
Strength: WEAK
Reasons: ['COMMONLY_USED']

```

## Part D: Six‑Digit PIN Strength & Reasons
```
$ python src/PartD_SixDigitPIN.py
Enter 6-digit MPIN: 123456
Your DOB (YYYY-MM-DD): 1990-04-17
...
Strength: WEAK
Reasons: ['COMMONLY_USED']
```
```bash
$ python src/PartD_SixDigitPIN.py
Enter 6-digit MPIN: 482957
...
Strength: STRONG
Reasons: []

```

## Part E (Legacy): Unittest‑Only Suite
```bash
$ python src/PartE_TestCases.py
# Runs > 60 unittest scenarios; useful for quick regression.

```
## CombinedTests.py: Single‑entry Test Runner
- All tests:
  ```bash
  python src/CombinedTests.py --part all
  ```
- Individual Part:
  ```bash
    python src/CombinedTests.py --part A
  python src/CombinedTests.py --part B
  # etc.

  ```
## Convenience Script
```bash
$ bash run_all.sh
=== Part A ===
...interactive...
=== Combined Tests: all parts ===
...unittest summary...

```
- Use run_all.sh for a one‑stop demo of everything.

