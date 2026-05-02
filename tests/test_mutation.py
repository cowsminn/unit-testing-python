import pytest
from src.evaluator import CvEvaluator
from src.validators import validate_skills, validate_experience


def test_kill_mutant_172_education_exact_match():
    """
    Omoară mutantul ROR [#172] din evaluator.py.
    Testează cazul în care nivelul de educație este EXACT egal cu cel cerut.
    """
    evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
    # Profilul JUNIOR_PYTHON_DEV cere 'bachelor'
    result = evaluator.analyze(
        experience_years=2,  # maximul permis pentru junior
        skills=["Python", "Git", "SQL"],
        education_level='bachelor'
    )
    assert result["final_score"] == 85
    assert result["status"] == "Strongly Recommended"


def test_kill_mutant_174_experience_exact_min_match():
    """
    Omoară mutantul ROR [#174] din evaluator.py.
    Testează cazul în care experiența este EXACT egală cu minimul cerut.
    """
    evaluator = CvEvaluator("SENIOR_JAVA_DEV")
    # Experiența de 5 ani este exact minimul pentru Senior
    result = evaluator.analyze(
        experience_years=5,
        skills=["Java", "Spring", "Docker", "Kubernetes", "AWS", "sql"],  # adaug required lipsă
        education_level='master'
    )
    # Scorul total ar trebui să fie 40 (edu) + 40 (skills) + 20 (exp) = 100
    assert result["final_score"] == 90


def test_kill_mutant_90_experience_validation_zero():
    """
    Omoară mutantul ROR [#90] din validators.py.
    Testează că o valoare de 0 ani este validă și nu ridică o excepție.
    """
    try:
        # Apelăm direct funcția de validare
        validate_experience(0)
    except ValueError:
        pytest.fail("validate_experience(0) a ridicat o excepție în mod neașteptat.")


def test_kill_mutant_65_skills_validation_not_list():
    """
    Omoară mutantul COD [#65] din validators.py.
    Testează că `validate_skills` ridică excepție dacă inputul nu este o listă.
    """
    with pytest.raises(ValueError, match="Skills must be a list of strings."):
        # Apelăm direct funcția de validare cu date invalide
        validate_skills("Python, Git")
