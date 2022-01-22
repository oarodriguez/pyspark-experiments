"""Verify the library top-level functionality."""
import pysparkexplore


def test_version():
    """Verify we have updated the package version."""
    assert pysparkexplore.__version__ == "2021.2.0"
