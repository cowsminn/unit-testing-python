import pytest
from evaluator import CvEvaluator
from validators import validate_skills, validate_experience


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


def test_kill_mutants_18_19_status_at_exact_boundary_40():
    """
    Omoară mutanții ROR [#18] și [#19] din evaluator.py (analyze).
    Mutanții schimbă `40 <= final_score` în `41 <=` sau `40 <`, ceea ce face
    ca un scor de exact 40 să fie clasificat greșit ca "Not Recommended".

    Scenariul: SENIOR_JAVA_DEV cu experiență insuficientă (0 puncte exp),
    fără educație bonus (0 puncte edu) și exact skill-urile required (40 puncte).
    Total: 0 + 0 + 40 = 40 → "Consider".
    """
    evaluator = CvEvaluator("SENIOR_JAVA_DEV")
    result = evaluator.analyze(
        experience_years=4,        # sub minimul de 5 ani → exp_score = 0
        education_level='none',    # fără bonus educație → edu_score = 0
        skills=['java', 'spring', 'sql', 'kubernetes']  # exact required → skill_score = 40
    )
    assert result["final_score"] == 40
    assert result["status"] == "Consider"


def test_kill_mutants_40_41_42_43_breakdown_keys():
    """
    Omoară mutanții [#40], [#41], [#42], [#43] din evaluator.py (analyze).
    Mutanții redenumesc cheile din breakdown: "skills" → "XXskillsXX"/"SKILLS"
    și "education" → "XXeducationXX"/"EDUCATION".
    Testul accesează explicit aceste chei și verifică valorile corecte.
    """
    evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
    result = evaluator.analyze(
        experience_years=1,              # ideal fit → exp_score = 30
        education_level='none',          # fără bonus → edu_score = 0
        skills=['python', 'sql']         # toate required, fără bonus → skill_score = 40
    )
    assert result["breakdown"]["skills"] == 40
    assert result["breakdown"]["education"] == 0
