"""
This module contains validation functions for the CV evaluator.
"""

VALID_EDUCATION_LEVELS = ['none', 'bachelor', 'master', 'phd']

def validate_experience(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if not isinstance(experience_years, int) or experience_years < 0:
        raise ValueError("Experience years must be a non-negative integer.")

def validate_education(education_level):
    """
    Validates that education_level is one of the allowed values.
    Raises ValueError if the validation fails.
    """
    if education_level not in VALID_EDUCATION_LEVELS:
        raise ValueError(f"Invalid education level. Must be one of {VALID_EDUCATION_LEVELS}.")

def validate_skills(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if not isinstance(skills, list) or not all(isinstance(s, str) for s in skills):
        raise ValueError("Skills must be a list of strings.")
