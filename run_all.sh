#!/usr/bin/env bash
set -e

echo "=== Part A (manual run) ==="
python src/PartA_CommonCheck.py || true

echo "=== Part B (manual run) ==="
python src/PartB_StrengthWithDemographics.py || true

echo "=== Part C (manual run) ==="
python src/PartC_WeaknessReasons.py || true

echo "=== Part D (manual run) ==="
python src/PartD_SixDigitPIN.py || true

echo "=== Combined Tests: all parts ==="
python src/CombinedTests.py --part all
