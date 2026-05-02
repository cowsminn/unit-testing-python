"""
This module contains validation functions for the CV evaluator.
"""

VALID_EDUCATION_LEVELS = ['none', 'bachelor', 'master', 'phd']
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

def validate_experience(experience_years):
    args = [experience_years]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_validate_experience__mutmut_orig, x_validate_experience__mutmut_mutants, args, kwargs, None)

def x_validate_experience__mutmut_orig(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if not isinstance(experience_years, int) or experience_years < 0:
        raise ValueError("Experience years must be a non-negative integer.")

def x_validate_experience__mutmut_1(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if not isinstance(experience_years, int) and experience_years < 0:
        raise ValueError("Experience years must be a non-negative integer.")

def x_validate_experience__mutmut_2(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if isinstance(experience_years, int) or experience_years < 0:
        raise ValueError("Experience years must be a non-negative integer.")

def x_validate_experience__mutmut_3(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if not isinstance(experience_years, int) or experience_years <= 0:
        raise ValueError("Experience years must be a non-negative integer.")

def x_validate_experience__mutmut_4(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if not isinstance(experience_years, int) or experience_years < 1:
        raise ValueError("Experience years must be a non-negative integer.")

def x_validate_experience__mutmut_5(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if not isinstance(experience_years, int) or experience_years < 0:
        raise ValueError(None)

def x_validate_experience__mutmut_6(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if not isinstance(experience_years, int) or experience_years < 0:
        raise ValueError("XXExperience years must be a non-negative integer.XX")

def x_validate_experience__mutmut_7(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if not isinstance(experience_years, int) or experience_years < 0:
        raise ValueError("experience years must be a non-negative integer.")

def x_validate_experience__mutmut_8(experience_years):
    """
    Validates that experience_years is a non-negative integer.
    Raises ValueError if the validation fails.
    """
    if not isinstance(experience_years, int) or experience_years < 0:
        raise ValueError("EXPERIENCE YEARS MUST BE A NON-NEGATIVE INTEGER.")

x_validate_experience__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_validate_experience__mutmut_1': x_validate_experience__mutmut_1, 
    'x_validate_experience__mutmut_2': x_validate_experience__mutmut_2, 
    'x_validate_experience__mutmut_3': x_validate_experience__mutmut_3, 
    'x_validate_experience__mutmut_4': x_validate_experience__mutmut_4, 
    'x_validate_experience__mutmut_5': x_validate_experience__mutmut_5, 
    'x_validate_experience__mutmut_6': x_validate_experience__mutmut_6, 
    'x_validate_experience__mutmut_7': x_validate_experience__mutmut_7, 
    'x_validate_experience__mutmut_8': x_validate_experience__mutmut_8
}
x_validate_experience__mutmut_orig.__name__ = 'x_validate_experience'

def validate_education(education_level):
    args = [education_level]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_validate_education__mutmut_orig, x_validate_education__mutmut_mutants, args, kwargs, None)

def x_validate_education__mutmut_orig(education_level):
    """
    Validates that education_level is one of the allowed values.
    Raises ValueError if the validation fails.
    """
    if education_level not in VALID_EDUCATION_LEVELS:
        raise ValueError(f"Invalid education level. Must be one of {VALID_EDUCATION_LEVELS}.")

def x_validate_education__mutmut_1(education_level):
    """
    Validates that education_level is one of the allowed values.
    Raises ValueError if the validation fails.
    """
    if education_level in VALID_EDUCATION_LEVELS:
        raise ValueError(f"Invalid education level. Must be one of {VALID_EDUCATION_LEVELS}.")

def x_validate_education__mutmut_2(education_level):
    """
    Validates that education_level is one of the allowed values.
    Raises ValueError if the validation fails.
    """
    if education_level not in VALID_EDUCATION_LEVELS:
        raise ValueError(None)

x_validate_education__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_validate_education__mutmut_1': x_validate_education__mutmut_1, 
    'x_validate_education__mutmut_2': x_validate_education__mutmut_2
}
x_validate_education__mutmut_orig.__name__ = 'x_validate_education'

def validate_skills(skills):
    args = [skills]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_validate_skills__mutmut_orig, x_validate_skills__mutmut_mutants, args, kwargs, None)

def x_validate_skills__mutmut_orig(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if not isinstance(skills, list) or not all(isinstance(s, str) for s in skills):
        raise ValueError("Skills must be a list of strings.")

def x_validate_skills__mutmut_1(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if not isinstance(skills, list) and not all(isinstance(s, str) for s in skills):
        raise ValueError("Skills must be a list of strings.")

def x_validate_skills__mutmut_2(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if isinstance(skills, list) or not all(isinstance(s, str) for s in skills):
        raise ValueError("Skills must be a list of strings.")

def x_validate_skills__mutmut_3(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if not isinstance(skills, list) or all(isinstance(s, str) for s in skills):
        raise ValueError("Skills must be a list of strings.")

def x_validate_skills__mutmut_4(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if not isinstance(skills, list) or not all(None):
        raise ValueError("Skills must be a list of strings.")

def x_validate_skills__mutmut_5(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if not isinstance(skills, list) or not all(isinstance(s, str) for s in skills):
        raise ValueError(None)

def x_validate_skills__mutmut_6(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if not isinstance(skills, list) or not all(isinstance(s, str) for s in skills):
        raise ValueError("XXSkills must be a list of strings.XX")

def x_validate_skills__mutmut_7(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if not isinstance(skills, list) or not all(isinstance(s, str) for s in skills):
        raise ValueError("skills must be a list of strings.")

def x_validate_skills__mutmut_8(skills):
    """
    Validates that skills is a list of strings.
    Raises ValueError if the validation fails.
    """
    if not isinstance(skills, list) or not all(isinstance(s, str) for s in skills):
        raise ValueError("SKILLS MUST BE A LIST OF STRINGS.")

x_validate_skills__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_validate_skills__mutmut_1': x_validate_skills__mutmut_1, 
    'x_validate_skills__mutmut_2': x_validate_skills__mutmut_2, 
    'x_validate_skills__mutmut_3': x_validate_skills__mutmut_3, 
    'x_validate_skills__mutmut_4': x_validate_skills__mutmut_4, 
    'x_validate_skills__mutmut_5': x_validate_skills__mutmut_5, 
    'x_validate_skills__mutmut_6': x_validate_skills__mutmut_6, 
    'x_validate_skills__mutmut_7': x_validate_skills__mutmut_7, 
    'x_validate_skills__mutmut_8': x_validate_skills__mutmut_8
}
x_validate_skills__mutmut_orig.__name__ = 'x_validate_skills'
