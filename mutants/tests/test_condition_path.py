import pytest
from evaluator import CvEvaluator
from validators import validate_experience

# Test suite for Condition and Path Coverage.
# We aim to test all sub-conditions within complex 'if' statements
# and ensure we traverse different execution paths.

# --- 1. Testing the compound condition in validate_experience ---
# The condition is: `if not isinstance(experience_years, int) or experience_years < 0:`

def test_validate_experience_path_1_not_an_integer():
    """
    Tests the first part of the 'or' condition.
    - `not isinstance(experience_years, int)` -> True
    - The condition short-circuits and the whole expression is True.
    - Expected result: Raises ValueError.
    """
    with pytest.raises(ValueError, match="Experience years must be a non-negative integer."):
        validate_experience("five")

def test_validate_experience_path_2_negative_integer():
    """
    Tests the second part of the 'or' condition.
    - `not isinstance(experience_years, int)` -> False
    - `experience_years < 0` -> True
    - The whole expression is True.
    - Expected result: Raises ValueError.
    """
    with pytest.raises(ValueError, match="Experience years must be a non-negative integer."):
        validate_experience(-5)

def test_validate_experience_path_3_valid_integer():
    """
    Tests the path where the condition is false.
    - `not isinstance(experience_years, int)` -> False
    - `experience_years < 0` -> False
    - The whole expression is False.
    - Expected result: No exception is raised.
    """
    try:
        validate_experience(10)
    except ValueError:
        pytest.fail("validate_experience() raised ValueError unexpectedly!")

# --- 2. Testing the compound condition in _calculate_experience_score ---
# The condition is: `if max_exp is not None and experience_years > max_exp:`

def test_experience_score_path_1_max_exp_is_none():
    """
    Tests the path for a profile with no max_experience (e.g., Senior).
    - `max_exp is not None` -> False
    - The condition short-circuits and the 'if' block is skipped.
    - We test with high experience to ensure it doesn't incorrectly get a low score.
    """
    evaluator = CvEvaluator("SENIOR_JAVA_DEV") # This profile has max_experience = None
    # For a senior, 10 years should be an ideal fit.
    score = evaluator._calculate_experience_score(10)
    assert score == 30 # Should be ideal fit, not overqualified

def test_experience_score_path_2_is_overqualified():
    """
    Tests the path for a profile where the candidate is overqualified.
    - `max_exp is not None` -> True (for JUNIOR_PYTHON_DEV)
    - `experience_years > max_exp` -> True
    - The 'if' block is executed.
    """
    evaluator = CvEvaluator("JUNIOR_PYTHON_DEV") # This profile has max_experience = 2
    score = evaluator._calculate_experience_score(5) # 5 > 2
    assert score == 15 # Overqualified score

def test_experience_score_path_3_is_ideal_fit():
    """
    Tests the path for a profile where the candidate is an ideal fit.
    - `max_exp is not None` -> True (for JUNIOR_PYTHON_DEV)
    - `experience_years > max_exp` -> False
    - The 'if' block is skipped.
    """
    evaluator = CvEvaluator("JUNIOR_PYTHON_DEV") # This profile has max_experience = 2
    score = evaluator._calculate_experience_score(1) # 1 is not > 2
    assert score == 30 # Ideal fit score

# --- 3. Testing paths in the final 'analyze' method ---
# We want to test the different paths for the 'status' calculation.

def test_analyze_path_status_not_recommended():
    """
    Tests the path that results in a 'Not Recommended' status.
    This happens when the final score is less than 40.
    """
    evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
    # To get a score < 40, we can have missing required skills.
    # Exp: 1 year (30) + Edu: 'none' (0) + Skills: missing 'sql' (-50) = -20 -> final 0
    analysis = evaluator.analyze(experience_years=1, education_level='none', skills=['python'])
    assert analysis["final_score"] == 0
    assert analysis["status"] == "Not Recommended"

def test_analyze_path_status_consider():
    """
    Tests the path that results in a 'Consider' status.
    This happens when the score is between 40 and 69.
    """
    evaluator = CvEvaluator("SENIOR_JAVA_DEV")
    # To get a score in this range:
    # Profile: SENIOR_JAVA_DEV
    # Exp: 4 years (not qualified) -> 0 points
    # Edu: 'bachelor' -> 5 points
    # Skills: All required + 2 bonus -> 40 + 20 = 60 points
    # Total = 65
    analysis = evaluator.analyze(
        experience_years=4,
        education_level='bachelor',
        skills=['java', 'spring', 'sql', 'kubernetes', 'aws', 'kafka']
    )
    assert analysis["final_score"] == 65
    assert analysis["status"] == "Consider"

def test_analyze_path_status_strongly_recommended():
    """
    Tests the path that results in a 'Strongly Recommended' status.
    This happens when the score is 70 or more.
    """
    evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
    # Exp: 1 year (30) + Edu: 'none' (0) + Skills: all required (40) = 70
    analysis = evaluator.analyze(experience_years=1, education_level='none', skills=['python', 'sql'])
    assert analysis["final_score"] == 70
    assert analysis["status"] == "Strongly Recommended"


# =============================================================================
# Basis Path Testing / Testare pe Circuite Independente (McCabe)
#
# Funcție analizată: CvEvaluator._calculate_experience_score()
#
# Graf de Control al Fluxului (CFG):
#
#   N1 (intrare: validate, get min_exp, max_exp)
#    |
#    v
#   N2 <-- Decizie: experience_years < min_exp?
#   / \
# (T) (F)
#  |    \
# N3    N4 <-- Decizie: max_exp is not None?  (prima condiție din AND)
#  |    / \
#  |  (T) (F)
#  |   |    \
#  |  N5    N7 <-- return 30 (max_exp is None, short-circuit)
#  |  / \    |
#  |(T) (F)  |
#  | |    \  |
#  |N6    N7 <-- return 30 (potrivire ideală)
#  | |    |
#  v v    v
#   N8 (ieșire)
#
# N3 = return 0  (neeligibil)
# N6 = return 15 (supracalificat)
#
# Număr de noduri:  N = 8
# Număr de arce:    E = 10
#   (N1→N2, N2→N3, N2→N4, N3→N8, N4→N5, N4→N7,
#    N5→N6, N5→N7, N6→N8, N7→N8)
#
# Complexitate ciclomatică: V(G) = E - N + 2 = 10 - 8 + 2 = 4
#
# Circuite independente (4 căi liniar independente):
#   P1: N1 → N2(T) → N3 → N8
#   P2: N1 → N2(F) → N4(T) → N5(T) → N6 → N8
#   P3: N1 → N2(F) → N4(F) → N7 → N8   (short-circuit)
#   P4: N1 → N2(F) → N4(T) → N5(F) → N7 → N8
# =============================================================================

def test_circuit_P1_candidate_underqualified():
    """
    P1: N1 → N2(True) → N3 → N8
    Candidatul nu atinge minimul de experiență cerut.
    SENIOR_JAVA_DEV cere min=5 ani; 4 ani < 5 → return 0.
    """
    evaluator = CvEvaluator("SENIOR_JAVA_DEV")
    score = evaluator._calculate_experience_score(4)
    assert score == 0


def test_circuit_P2_candidate_overqualified():
    """
    P2: N1 → N2(False) → N4(True) → N5(True) → N6 → N8
    max_exp este definit ȘI candidatul îl depășește.
    JUNIOR_PYTHON_DEV: min=0, max=2; 5 > 2 → return 15.
    """
    evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
    score = evaluator._calculate_experience_score(5)
    assert score == 15


def test_circuit_P3_no_max_experience_short_circuit():
    """
    P3: N1 → N2(False) → N4(False) → N7 → N8
    max_exp este None — a doua condiție din AND nu se evaluează (short-circuit).
    SENIOR_JAVA_DEV nu definește max_experience → max_exp=None → return 30.
    """
    evaluator = CvEvaluator("SENIOR_JAVA_DEV")
    score = evaluator._calculate_experience_score(10)
    assert score == 30


def test_circuit_P4_candidate_ideal_fit_with_max_defined():
    """
    P4: N1 → N2(False) → N4(True) → N5(False) → N7 → N8
    max_exp este definit DAR candidatul nu îl depășește.
    JUNIOR_PYTHON_DEV: min=0, max=2; 1 <= 2 → return 30.
    """
    evaluator = CvEvaluator("JUNIOR_PYTHON_DEV")
    score = evaluator._calculate_experience_score(1)
    assert score == 30
