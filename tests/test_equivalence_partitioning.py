import pytest
from evaluator import CvEvaluator

# Test suite for Equivalence Partitioning using pytest classes and parametrization
# for a more granular and organized approach.

class TestExperiencePartitioning:
    """Tests focused solely on the experience component."""

    @pytest.mark.parametrize("years, expected_score", [
        (1, 30),   # Class: Ideal fit for Junior
        (3, 15),   # Class: Overqualified for Junior
    ])
    def test_junior_experience_classes(self, years, expected_score):
        """Tests valid experience classes for the JUNIOR_PYTHON_DEV profile."""
        evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
        score = evaluator._calculate_experience_score(years)
        assert score == expected_score

    @pytest.mark.parametrize("years, expected_score", [
        (4, 0),    # Class: Not qualified for Senior
        (10, 30),  # Class: Ideal fit for Senior
    ])
    def test_senior_experience_classes(self, years, expected_score):
        """Tests valid experience classes for the SENIOR_JAVA_DEV profile."""
        evaluator = CvEvaluator("SENIOR_JAVA_DEV")
        score = evaluator._calculate_experience_score(years)
        assert score == expected_score

    @pytest.mark.parametrize("invalid_input", [-1, -10, "two", 5.5, None, []])
    def test_invalid_experience_class(self, invalid_input):
        """Tests the invalid equivalence class for experience (wrong type or negative)."""
        evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
        with pytest.raises(ValueError):
            evaluator._calculate_experience_score(invalid_input)


class TestSkillsPartitioning:
    """Tests focused solely on the skills component."""

    @pytest.mark.parametrize("skills, expected_score", [
        (["python", "sql"], 40),                                  # Class: All required, no bonus
        (["python", "sql", "git"], 50),                           # Class: All required, one bonus
        (["python", "sql", "git", "docker"], 60),                 # Class: All required, all bonus
        (["python"], -50),                                        # Class: Missing one required
        ([], -100),                                               # Class: Missing all required
        (["java", "c++"], -100),                                  # Class: Irrelevant skills
    ])
    def test_skill_classes(self, skills, expected_score):
        """Tests various valid classes of skill sets for JUNIOR_PYTHON_DEV."""
        evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
        score = evaluator._calculate_skill_score(skills)
        assert score == expected_score

    @pytest.mark.parametrize("invalid_input", [
        "python",      # Not a list
        ["python", 1], # List contains non-string
        None,
        {"skill": "python"}
    ])
    def test_invalid_skills_class(self, invalid_input):
        """Tests the invalid equivalence class for skills (wrong type)."""
        evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
        with pytest.raises(ValueError):
            evaluator._calculate_skill_score(invalid_input)


class TestEducationPartitioning:
    """Tests focused solely on the education component."""

    @pytest.mark.parametrize("level, expected_score", [
        ("bachelor", 5),   # Class: Bachelor
        ("master", 10),  # Class: Master
        ("phd", 15),     # Class: PhD (gets 15 for Senior profile)
        ("none", 0),     # Class: None
    ])
    def test_education_classes(self, level, expected_score):
        """Tests valid equivalence classes for education level."""
        # Using SENIOR profile as it has a score for phd
        evaluator = CvEvaluator("SENIOR_JAVA_DEV")
        score = evaluator._calculate_education_score(level)
        assert score == expected_score

    @pytest.mark.parametrize("invalid_input", ["high_school", "college", 123, None, []])
    def test_invalid_education_class(self, invalid_input):
        """Tests the invalid equivalence class for education (not a valid level)."""
        evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
        with pytest.raises(ValueError):
            evaluator._calculate_education_score(invalid_input)


class TestMidPythonDevPartitioning:
    """Equivalence partitioning tests for the MID_PYTHON_DEV profile.
    This profile adds a third experience range (min=2, max=5) and
    requires 3 skills (python, sql, git), with higher education bonuses.
    """

    @pytest.mark.parametrize("years, expected_score", [
        (1,  0),   # Class: Underqualified (below min=2)
        (3,  30),  # Class: Ideal fit (2 <= years <= 5)
        (7,  15),  # Class: Overqualified (above max=5)
    ])
    def test_mid_experience_classes(self, years, expected_score):
        """Tests the 3 valid experience equivalence classes for MID_PYTHON_DEV."""
        evaluator = CvEvaluator("MID_PYTHON_DEV")
        score = evaluator._calculate_experience_score(years)
        assert score == expected_score

    @pytest.mark.parametrize("skills, expected_score", [
        (["python", "sql", "git"], 40),                          # Class: All required, no bonus
        (["python", "sql", "git", "docker"], 50),                # Class: All required, one bonus
        (["python", "sql", "git", "docker", "django", "fastapi"], 70),  # All required + all bonus
        (["python", "sql"], -50),                                # Class: Missing one required (git)
        ([], -150),                                              # Class: Missing all 3 required
    ])
    def test_mid_skill_classes(self, skills, expected_score):
        """Tests skill equivalence classes for MID_PYTHON_DEV (3 required skills)."""
        evaluator = CvEvaluator("MID_PYTHON_DEV")
        score = evaluator._calculate_skill_score(skills)
        assert score == expected_score

    @pytest.mark.parametrize("level, expected_score", [
        ("none",     0),   # Class: No education bonus
        ("bachelor", 10),  # Class: Bachelor (higher bonus than Junior)
        ("master",   15),  # Class: Master
        ("phd",      15),  # Class: PhD (same as Master for this profile)
    ])
    def test_mid_education_classes(self, level, expected_score):
        """Tests education equivalence classes for MID_PYTHON_DEV."""
        evaluator = CvEvaluator("MID_PYTHON_DEV")
        score = evaluator._calculate_education_score(level)
        assert score == expected_score
