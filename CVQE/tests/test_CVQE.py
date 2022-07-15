"""
Unit and regression test for the CVQE package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import CVQE


def test_CVQE_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "CVQE" in sys.modules
