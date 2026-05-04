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
