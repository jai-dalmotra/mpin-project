#!/usr/bin/env bash
set -e

echo "=== Part A ==="
python src/PartA_CommonCheck.py || true

echo "=== Part B ==="
python src/PartB_StrengthWithDemographics.py || true

echo "=== Part C ==="
python src/PartC_WeaknessReasons.py || true

echo "=== Part D ==="
python src/PartD_SixDigitPIN.py || true

echo "=== Combined Tests: all parts ==="
# Use module invocation so imports work seamlessly
python -m src.CombinedTests --part all
