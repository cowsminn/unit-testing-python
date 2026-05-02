import pytest
from src.evaluator import CvEvaluator
from src.validators import validate_education, validate_skills

# Test suite for achieving 100% statement and branch coverage.
# These tests target specific lines of code missed by other test suites,
# typically error-handling branches.

def test_invalid_profile_name_raises_error():
    """
    Covers the `raise ValueError` in CvEvaluator.__init__.
    This ensures that creating an evaluator with a non-existent profile fails.
    """
    with pytest.raises(ValueError, match="Profile 'DATA_SCIENTIST' not found"):
        CvEvaluator("DATA_SCIENTIST")

def test_invalid_education_level_raises_error():
    """
    Covers the `raise ValueError` in validators.validate_education.
    This test is for the 'Miss' in src/validators.py.
    """
    with pytest.raises(ValueError, match="Invalid education level. Must be one of"):
        validate_education("high_school")

def test_invalid_skills_list_raises_error():
    """
    Covers the `raise ValueError` in validators.validate_skills.
    This test is for the other 'Miss' in src/validators.py.
    It checks that the function rejects a list that does not contain only strings.
    """
    with pytest.raises(ValueError, match="Skills must be a list of strings."):
        validate_skills(["python", 123, "sql"])

# Note on the remaining missing lines in evaluator.py:
# The coverage report might still show one line as missed in `_calculate_experience_score`:
# `return 10 # Default case, should not be hit with current logic`
# This is considered "dead code" because the if/elif conditions above it cover all
# possible scenarios for a valid integer. It's impossible to reach this line with
# the current logic. Discovering dead code is a valuable outcome of coverage analysis.
# We can either remove it or leave it as a safeguard, but we don't need to write a test for it.
