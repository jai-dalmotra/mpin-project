# common/__init__.py

"""
common package for MPIN Security Evaluator

Provides core shared logic:
 - PIN common‑list lookup
 - Demographic date matching
"""

__version__ = "1.0.0"

# Expose the key functions at package level
from .pin_checker import load_common_pins, is_common_pin
from .demographics import format_date_parts, matches_any_date

__all__ = [
    "load_common_pins",
    "is_common_pin",
    "format_date_parts",
    "matches_any_date",
    "__version__",
]
