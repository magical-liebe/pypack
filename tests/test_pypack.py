"""Test for pypack."""

import pypack


def test_version() -> None:
    """Check version."""
    assert pypack.__version__ == "0.1.0"
