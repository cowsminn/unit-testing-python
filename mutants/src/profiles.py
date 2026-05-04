"""
This module contains the job profile definitions used by the CvEvaluator.
Each profile defines the criteria for a specific job role.
"""

JOB_PROFILES = {
    "JUNIOR_PYTHON_DEV": {
        "required_skills": {"python", "sql"},
        "bonus_skills": {"git", "docker"},
        "min_experience": 0,
        "max_experience": 2,
        "education_bonus": {"bachelor": 5, "master": 10}
    },
    "SENIOR_JAVA_DEV": {
        "required_skills": {"java", "spring", "sql", "kubernetes"},
        "bonus_skills": {"aws", "kafka", "microservices"},
        "min_experience": 5,
        "education_bonus": {"bachelor": 5, "master": 10, "phd": 15}
    },
    "MID_PYTHON_DEV": {
        "required_skills": {"python", "sql", "git"},
        "bonus_skills": {"docker", "django", "fastapi"},
        "min_experience": 2,
        "max_experience": 5,
        "education_bonus": {"bachelor": 10, "master": 15, "phd": 15}
    }
}
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
