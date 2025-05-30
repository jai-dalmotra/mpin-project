# MPIN Security Evaluator

Evaluate the strength of 4‑ and 6‑digit PINs, with optional demographic checks.

## Features
- **Part A**: Common PIN checker (4 digits)  
- **Part B**: Strength (4 digits) with demographic DOB/spouse/anniversary  
- **Part C**: Weakness reasons (`COMMONLY_USED`, `DEMOGRAPHIC_…`)  
- **Part D**: Same as C for 6‑digit PINs  
- **Part E**: 60+ automated unit tests

## Repo Layout
```
.github/ ← CI + templates
common/ ← Shared logic
data/ ← Static PIN list
docs/ ← Architecture & usage
src/ ← Scripts (Parts A–E)
.gitignore ← Ignored files
LICENSE ← MIT License
README.md ← This file
run_all.sh ← Convenience runner
```

## Quickstart

```bash
git clone https://github.com/YourUser/mpin_project.git
cd mpin_project
bash run_all.sh
```
### Run Tests

- **All parts**:
  ```bash
  python src/CombinedTests.py --part all
  ```
- **Single Part (e.g. Part B)**:

  ```bash

  python src/CombinedTests.py --part B
  ```

And update **run_all.sh** instructions accordingly.

---

## 4. File Tree Snapshot
```
mpin_project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── common/
│   ├── __init__.py
│   ├── pin_checker.py
│   └── demographics.py
├── data/
│   └── common_mpin.txt
├── docs/
│   ├── architecture.md
│   └── usage.md
├── src/
│   ├── CombinedTests.py          
│   ├── PartA_CommonCheck.py
│   ├── PartB_StrengthWithDemographics.py
│   ├── PartC_WeaknessReasons.py
│   ├── PartD_SixDigitPIN.py
│   └── PartE_TestCases.py        
├── .gitignore
├── LICENSE
├── README.md
└── run_all.sh
```

