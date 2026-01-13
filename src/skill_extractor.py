"""
Skill Extractor Module
----------------------
This module extracts technical skills from resume text
using keyword-based matching (ATS-friendly approach).
"""

import re

# 🔹 Master skill list (easy to extend later)
SKILL_KEYWORDS = [
    "python", "sql", "excel", "power bi", "tableau",
    "machine learning", "deep learning", "nlp",
    "data analysis", "data analyst", "data scientist",
    "statistics", "tensorflow", "pytorch",
    "scikit-learn", "sklearn",
    "cloud", "aws", "azure", "gcp",
    "big data", "spark", "hadoop"
]


def clean_text(text: str) -> str:
    """Lowercase + remove special characters"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text


def extract_skills(text: str) -> list:
    """
    Extract skills from resume text
    Returns a sorted list of unique skills
    """
    text = clean_text(text)
    found_skills = set()

    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill.title())

    return sorted(found_skills)


# 🔹 Run standalone (testing purpose)
if __name__ == "__main__":
    sample_text = """
    Data Analyst skilled in Python, SQL, Power BI and Machine Learning.
    Experience with NLP and Deep Learning using TensorFlow.
    """

    skills = extract_skills(sample_text)

    print("✅ Extracted Skills:")
    for skill in skills:
        print("-", skill)
