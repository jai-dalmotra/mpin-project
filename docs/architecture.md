# Architecture Overview

```
mpin_project/
├── .github/                      # CI workflows & templates
│   └── workflows/
│       └── ci.yml
├── common/                       # Shared business logic
│   ├── __init__.py
│   ├── pin_checker.py            # Loads data/common_mpin.txt and checks pins
│   └── demographics.py           # Parses dates and matches PIN substrings
├── data/                         # Static resources
│   └── common_mpin.txt           # List of top common 4- & 6-digit PINs
├── docs/                         # Documentation
│   ├── architecture.md           # High-level module map
│   └── usage.md                  # CLI usage examples
├── src/                          # Executable scripts & test runner
│   ├── PartA_CommonCheck.py
│   ├── PartB_StrengthWithDemographics.py
│   ├── PartC_WeaknessReasons.py
│   ├── PartD_SixDigitPIN.py
│   ├── PartE_TestCases.py        # Legacy unittest suite (optional)
│   └── CombinedTests.py          # Unified runner for all or per-Part tests
├── .gitignore
├── LICENSE
├── README.md
└── run_all.sh                    # Convenience wrapper

```

### Layers

1. **`common/`**  
   - Encapsulates all core logic so scripts remain thin.  
   - `pin_checker.py` – loads the common‑PIN list.  
   - `demographics.py` – date parsing and matching routines.

2. **`data/`**  
   - Holds `common_mpin.txt`, a simple newline list of weak PINs.  
   - Easy to update or extend without touching code.

3. **`src/`**  
   - **Scripts** (Parts A–D) import from `common/` and expose `main()` for CLI.  
   - **CombinedTests.py** uses `argparse` and `unittest` to run:
     - `--part all` for complete coverage,
     - `--part A|B|C|D` for part‑specific runs.

4. **CI & Automation**  
   - `.github/workflows/ci.yml` now invokes `CombinedTests.py --part all`.  
   - `run_all.sh` runs each interactive script, then full test suite.

---
