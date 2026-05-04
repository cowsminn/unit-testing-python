from profiles import JOB_PROFILES
from validators import validate_experience, validate_education, validate_skills
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

class CvEvaluator:
    """
    Analyzes a CV against a specific job profile to provide a detailed rating.
    """

    def __init__(self, profile_name):
        args = [profile_name]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCvEvaluatorǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁCvEvaluatorǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁCvEvaluatorǁ__init____mutmut_orig(self, profile_name):
        if profile_name not in JOB_PROFILES:
            raise ValueError(f"Profile '{profile_name}' not found. Available profiles: {list(JOB_PROFILES.keys())}")
        self.profile = JOB_PROFILES[profile_name]

    def xǁCvEvaluatorǁ__init____mutmut_1(self, profile_name):
        if profile_name in JOB_PROFILES:
            raise ValueError(f"Profile '{profile_name}' not found. Available profiles: {list(JOB_PROFILES.keys())}")
        self.profile = JOB_PROFILES[profile_name]

    def xǁCvEvaluatorǁ__init____mutmut_2(self, profile_name):
        if profile_name not in JOB_PROFILES:
            raise ValueError(None)
        self.profile = JOB_PROFILES[profile_name]

    def xǁCvEvaluatorǁ__init____mutmut_3(self, profile_name):
        if profile_name not in JOB_PROFILES:
            raise ValueError(f"Profile '{profile_name}' not found. Available profiles: {list(None)}")
        self.profile = JOB_PROFILES[profile_name]

    def xǁCvEvaluatorǁ__init____mutmut_4(self, profile_name):
        if profile_name not in JOB_PROFILES:
            raise ValueError(f"Profile '{profile_name}' not found. Available profiles: {list(JOB_PROFILES.keys())}")
        self.profile = None
    
    xǁCvEvaluatorǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCvEvaluatorǁ__init____mutmut_1': xǁCvEvaluatorǁ__init____mutmut_1, 
        'xǁCvEvaluatorǁ__init____mutmut_2': xǁCvEvaluatorǁ__init____mutmut_2, 
        'xǁCvEvaluatorǁ__init____mutmut_3': xǁCvEvaluatorǁ__init____mutmut_3, 
        'xǁCvEvaluatorǁ__init____mutmut_4': xǁCvEvaluatorǁ__init____mutmut_4
    }
    xǁCvEvaluatorǁ__init____mutmut_orig.__name__ = 'xǁCvEvaluatorǁ__init__'

    def _calculate_experience_score(self, experience_years):
        args = [experience_years]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_orig'), object.__getattribute__(self, 'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_mutants'), args, kwargs, self)

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_orig(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_1(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(None)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_2(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = None
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_3(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get(None, 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_4(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", None)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_5(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get(0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_6(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", )
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_7(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("XXmin_experienceXX", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_8(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("MIN_EXPERIENCE", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_9(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 1)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_10(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = None # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_11(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get(None) # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_12(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("XXmax_experienceXX") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_13(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("MAX_EXPERIENCE") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_14(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years <= min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_15(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 1  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_16(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None or experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_17(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_18(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years >= max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_19(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 16 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 30

    def xǁCvEvaluatorǁ_calculate_experience_score__mutmut_20(self, experience_years):
        """Calculates score based on years of experience relative to the profile."""
        validate_experience(experience_years)
        
        min_exp = self.profile.get("min_experience", 0)
        max_exp = self.profile.get("max_experience") # Can be None for senior roles

        if experience_years < min_exp:
            return 0  # Not qualified
        
        if max_exp is not None and experience_years > max_exp:
            return 15 # Overqualified, might be a slight negative
        
        # Ideal fit for the role
        return 31
    
    xǁCvEvaluatorǁ_calculate_experience_score__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_1': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_1, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_2': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_2, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_3': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_3, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_4': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_4, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_5': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_5, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_6': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_6, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_7': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_7, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_8': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_8, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_9': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_9, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_10': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_10, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_11': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_11, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_12': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_12, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_13': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_13, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_14': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_14, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_15': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_15, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_16': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_16, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_17': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_17, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_18': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_18, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_19': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_19, 
        'xǁCvEvaluatorǁ_calculate_experience_score__mutmut_20': xǁCvEvaluatorǁ_calculate_experience_score__mutmut_20
    }
    xǁCvEvaluatorǁ_calculate_experience_score__mutmut_orig.__name__ = 'xǁCvEvaluatorǁ_calculate_experience_score'

    def _calculate_skill_score(self, candidate_skills):
        args = [candidate_skills]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_orig'), object.__getattribute__(self, 'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_mutants'), args, kwargs, self)

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_orig(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_1(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(None)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_2(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = None
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_3(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.upper() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_4(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = None
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_5(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get(None, set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_6(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", None)
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_7(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get(set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_8(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", )
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_9(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("XXrequired_skillsXX", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_10(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("REQUIRED_SKILLS", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_11(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = None

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_12(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get(None, set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_13(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", None)

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_14(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get(set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_15(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", )

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_16(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("XXbonus_skillsXX", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_17(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("BONUS_SKILLS", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_18(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = None
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_19(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required + candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_20(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) >= 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_21(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 1:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_22(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 / len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_23(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return +50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_24(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -51 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_25(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = None # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_26(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 41 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_27(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = None
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_28(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(None)
        score += len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_29(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score = len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_30(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score -= len(matched_bonus) * 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_31(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) / 10
        
        return score

    def xǁCvEvaluatorǁ_calculate_skill_score__mutmut_32(self, candidate_skills):
        """Calculates score based on required and bonus skills."""
        validate_skills(candidate_skills)
            
        candidate_skills_set = {skill.lower() for skill in candidate_skills}
        required = self.profile.get("required_skills", set())
        bonus = self.profile.get("bonus_skills", set())

        # Check for missing essential skills
        missing_required = required - candidate_skills_set
        if len(missing_required) > 0:
            # Heavy penalty for each missing required skill
            return -50 * len(missing_required)

        score = 40 # Base score for having all required skills

        # Add points for bonus skills
        matched_bonus = candidate_skills_set.intersection(bonus)
        score += len(matched_bonus) * 11
        
        return score
    
    xǁCvEvaluatorǁ_calculate_skill_score__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_1': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_1, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_2': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_2, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_3': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_3, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_4': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_4, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_5': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_5, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_6': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_6, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_7': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_7, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_8': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_8, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_9': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_9, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_10': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_10, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_11': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_11, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_12': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_12, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_13': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_13, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_14': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_14, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_15': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_15, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_16': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_16, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_17': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_17, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_18': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_18, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_19': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_19, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_20': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_20, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_21': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_21, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_22': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_22, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_23': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_23, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_24': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_24, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_25': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_25, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_26': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_26, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_27': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_27, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_28': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_28, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_29': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_29, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_30': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_30, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_31': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_31, 
        'xǁCvEvaluatorǁ_calculate_skill_score__mutmut_32': xǁCvEvaluatorǁ_calculate_skill_score__mutmut_32
    }
    xǁCvEvaluatorǁ_calculate_skill_score__mutmut_orig.__name__ = 'xǁCvEvaluatorǁ_calculate_skill_score'

    def _calculate_education_score(self, education_level):
        args = [education_level]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCvEvaluatorǁ_calculate_education_score__mutmut_orig'), object.__getattribute__(self, 'xǁCvEvaluatorǁ_calculate_education_score__mutmut_mutants'), args, kwargs, self)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_orig(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("education_bonus", {}).get(education_level, 0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_1(self, education_level):
        """Calculates score based on education."""
        validate_education(None)
        return self.profile.get("education_bonus", {}).get(education_level, 0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_2(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("education_bonus", {}).get(None, 0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_3(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("education_bonus", {}).get(education_level, None)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_4(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("education_bonus", {}).get(0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_5(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("education_bonus", {}).get(education_level, )

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_6(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get(None, {}).get(education_level, 0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_7(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("education_bonus", None).get(education_level, 0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_8(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get({}).get(education_level, 0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_9(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("education_bonus", ).get(education_level, 0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_10(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("XXeducation_bonusXX", {}).get(education_level, 0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_11(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("EDUCATION_BONUS", {}).get(education_level, 0)

    def xǁCvEvaluatorǁ_calculate_education_score__mutmut_12(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("education_bonus", {}).get(education_level, 1)
    
    xǁCvEvaluatorǁ_calculate_education_score__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCvEvaluatorǁ_calculate_education_score__mutmut_1': xǁCvEvaluatorǁ_calculate_education_score__mutmut_1, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_2': xǁCvEvaluatorǁ_calculate_education_score__mutmut_2, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_3': xǁCvEvaluatorǁ_calculate_education_score__mutmut_3, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_4': xǁCvEvaluatorǁ_calculate_education_score__mutmut_4, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_5': xǁCvEvaluatorǁ_calculate_education_score__mutmut_5, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_6': xǁCvEvaluatorǁ_calculate_education_score__mutmut_6, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_7': xǁCvEvaluatorǁ_calculate_education_score__mutmut_7, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_8': xǁCvEvaluatorǁ_calculate_education_score__mutmut_8, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_9': xǁCvEvaluatorǁ_calculate_education_score__mutmut_9, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_10': xǁCvEvaluatorǁ_calculate_education_score__mutmut_10, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_11': xǁCvEvaluatorǁ_calculate_education_score__mutmut_11, 
        'xǁCvEvaluatorǁ_calculate_education_score__mutmut_12': xǁCvEvaluatorǁ_calculate_education_score__mutmut_12
    }
    xǁCvEvaluatorǁ_calculate_education_score__mutmut_orig.__name__ = 'xǁCvEvaluatorǁ_calculate_education_score'

    def analyze(self, experience_years, education_level, skills):
        args = [experience_years, education_level, skills]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCvEvaluatorǁanalyze__mutmut_orig'), object.__getattribute__(self, 'xǁCvEvaluatorǁanalyze__mutmut_mutants'), args, kwargs, self)

    def xǁCvEvaluatorǁanalyze__mutmut_orig(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_1(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = None
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_2(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(None)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_3(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = None
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_4(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(None)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_5(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = None

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_6(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(None)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_7(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = None
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_8(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score - edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_9(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score - skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_10(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score <= 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_11(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 1:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_12(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = None # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_13(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 1 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_14(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = None
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_15(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "XXNot RecommendedXX"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_16(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "not recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_17(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "NOT RECOMMENDED"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_18(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 41 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_19(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 < final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_20(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score <= 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_21(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 71:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_22(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = None
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_23(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "XXConsiderXX"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_24(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_25(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "CONSIDER"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_26(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score > 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_27(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 71:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_28(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = None

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_29(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "XXStrongly RecommendedXX"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_30(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "strongly recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_31(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "STRONGLY RECOMMENDED"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_32(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "XXfinal_scoreXX": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_33(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "FINAL_SCORE": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_34(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "XXstatusXX": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_35(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "STATUS": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_36(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "XXbreakdownXX": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_37(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "BREAKDOWN": {
                "experience": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_38(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "XXexperienceXX": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_39(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "EXPERIENCE": exp_score,
                "skills": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_40(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "XXskillsXX": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_41(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "SKILLS": skill_score,
                "education": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_42(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "XXeducationXX": edu_score
            }
        }

    def xǁCvEvaluatorǁanalyze__mutmut_43(self, experience_years, education_level, skills):
        """
        Analyzes the CV and returns a final score and a summary.
        """
        exp_score = self._calculate_experience_score(experience_years)
        skill_score = self._calculate_skill_score(skills)
        edu_score = self._calculate_education_score(education_level)

        final_score = exp_score + skill_score + edu_score
        
        # Final adjustments
        if final_score < 0:
            final_score = 0 # Score cannot be negative

        status = "Not Recommended"
        if 40 <= final_score < 70:
            status = "Consider"
        elif final_score >= 70:
            status = "Strongly Recommended"

        return {
            "final_score": final_score,
            "status": status,
            "breakdown": {
                "experience": exp_score,
                "skills": skill_score,
                "EDUCATION": edu_score
            }
        }
    
    xǁCvEvaluatorǁanalyze__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCvEvaluatorǁanalyze__mutmut_1': xǁCvEvaluatorǁanalyze__mutmut_1, 
        'xǁCvEvaluatorǁanalyze__mutmut_2': xǁCvEvaluatorǁanalyze__mutmut_2, 
        'xǁCvEvaluatorǁanalyze__mutmut_3': xǁCvEvaluatorǁanalyze__mutmut_3, 
        'xǁCvEvaluatorǁanalyze__mutmut_4': xǁCvEvaluatorǁanalyze__mutmut_4, 
        'xǁCvEvaluatorǁanalyze__mutmut_5': xǁCvEvaluatorǁanalyze__mutmut_5, 
        'xǁCvEvaluatorǁanalyze__mutmut_6': xǁCvEvaluatorǁanalyze__mutmut_6, 
        'xǁCvEvaluatorǁanalyze__mutmut_7': xǁCvEvaluatorǁanalyze__mutmut_7, 
        'xǁCvEvaluatorǁanalyze__mutmut_8': xǁCvEvaluatorǁanalyze__mutmut_8, 
        'xǁCvEvaluatorǁanalyze__mutmut_9': xǁCvEvaluatorǁanalyze__mutmut_9, 
        'xǁCvEvaluatorǁanalyze__mutmut_10': xǁCvEvaluatorǁanalyze__mutmut_10, 
        'xǁCvEvaluatorǁanalyze__mutmut_11': xǁCvEvaluatorǁanalyze__mutmut_11, 
        'xǁCvEvaluatorǁanalyze__mutmut_12': xǁCvEvaluatorǁanalyze__mutmut_12, 
        'xǁCvEvaluatorǁanalyze__mutmut_13': xǁCvEvaluatorǁanalyze__mutmut_13, 
        'xǁCvEvaluatorǁanalyze__mutmut_14': xǁCvEvaluatorǁanalyze__mutmut_14, 
        'xǁCvEvaluatorǁanalyze__mutmut_15': xǁCvEvaluatorǁanalyze__mutmut_15, 
        'xǁCvEvaluatorǁanalyze__mutmut_16': xǁCvEvaluatorǁanalyze__mutmut_16, 
        'xǁCvEvaluatorǁanalyze__mutmut_17': xǁCvEvaluatorǁanalyze__mutmut_17, 
        'xǁCvEvaluatorǁanalyze__mutmut_18': xǁCvEvaluatorǁanalyze__mutmut_18, 
        'xǁCvEvaluatorǁanalyze__mutmut_19': xǁCvEvaluatorǁanalyze__mutmut_19, 
        'xǁCvEvaluatorǁanalyze__mutmut_20': xǁCvEvaluatorǁanalyze__mutmut_20, 
        'xǁCvEvaluatorǁanalyze__mutmut_21': xǁCvEvaluatorǁanalyze__mutmut_21, 
        'xǁCvEvaluatorǁanalyze__mutmut_22': xǁCvEvaluatorǁanalyze__mutmut_22, 
        'xǁCvEvaluatorǁanalyze__mutmut_23': xǁCvEvaluatorǁanalyze__mutmut_23, 
        'xǁCvEvaluatorǁanalyze__mutmut_24': xǁCvEvaluatorǁanalyze__mutmut_24, 
        'xǁCvEvaluatorǁanalyze__mutmut_25': xǁCvEvaluatorǁanalyze__mutmut_25, 
        'xǁCvEvaluatorǁanalyze__mutmut_26': xǁCvEvaluatorǁanalyze__mutmut_26, 
        'xǁCvEvaluatorǁanalyze__mutmut_27': xǁCvEvaluatorǁanalyze__mutmut_27, 
        'xǁCvEvaluatorǁanalyze__mutmut_28': xǁCvEvaluatorǁanalyze__mutmut_28, 
        'xǁCvEvaluatorǁanalyze__mutmut_29': xǁCvEvaluatorǁanalyze__mutmut_29, 
        'xǁCvEvaluatorǁanalyze__mutmut_30': xǁCvEvaluatorǁanalyze__mutmut_30, 
        'xǁCvEvaluatorǁanalyze__mutmut_31': xǁCvEvaluatorǁanalyze__mutmut_31, 
        'xǁCvEvaluatorǁanalyze__mutmut_32': xǁCvEvaluatorǁanalyze__mutmut_32, 
        'xǁCvEvaluatorǁanalyze__mutmut_33': xǁCvEvaluatorǁanalyze__mutmut_33, 
        'xǁCvEvaluatorǁanalyze__mutmut_34': xǁCvEvaluatorǁanalyze__mutmut_34, 
        'xǁCvEvaluatorǁanalyze__mutmut_35': xǁCvEvaluatorǁanalyze__mutmut_35, 
        'xǁCvEvaluatorǁanalyze__mutmut_36': xǁCvEvaluatorǁanalyze__mutmut_36, 
        'xǁCvEvaluatorǁanalyze__mutmut_37': xǁCvEvaluatorǁanalyze__mutmut_37, 
        'xǁCvEvaluatorǁanalyze__mutmut_38': xǁCvEvaluatorǁanalyze__mutmut_38, 
        'xǁCvEvaluatorǁanalyze__mutmut_39': xǁCvEvaluatorǁanalyze__mutmut_39, 
        'xǁCvEvaluatorǁanalyze__mutmut_40': xǁCvEvaluatorǁanalyze__mutmut_40, 
        'xǁCvEvaluatorǁanalyze__mutmut_41': xǁCvEvaluatorǁanalyze__mutmut_41, 
        'xǁCvEvaluatorǁanalyze__mutmut_42': xǁCvEvaluatorǁanalyze__mutmut_42, 
        'xǁCvEvaluatorǁanalyze__mutmut_43': xǁCvEvaluatorǁanalyze__mutmut_43
    }
    xǁCvEvaluatorǁanalyze__mutmut_orig.__name__ = 'xǁCvEvaluatorǁanalyze'

