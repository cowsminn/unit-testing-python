from profiles import JOB_PROFILES
from validators import validate_experience, validate_education, validate_skills

class CvEvaluator:
    """
    Analyzes a CV against a specific job profile to provide a detailed rating.
    """

    def __init__(self, profile_name):
        if profile_name not in JOB_PROFILES:
            raise ValueError(f"Profile '{profile_name}' not found. Available profiles: {list(JOB_PROFILES.keys())}")
        self.profile = JOB_PROFILES[profile_name]

    def _calculate_experience_score(self, experience_years):
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

    def _calculate_skill_score(self, candidate_skills):
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

    def _calculate_education_score(self, education_level):
        """Calculates score based on education."""
        validate_education(education_level)
        return self.profile.get("education_bonus", {}).get(education_level, 0)

    def analyze(self, experience_years, education_level, skills):
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

