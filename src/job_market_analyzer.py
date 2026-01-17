from src.skill_extractor import extract_skills
from collections import Counter


def analyze_job_market(job_descriptions):
    all_skills = []

    for jd in job_descriptions:
        skills = extract_skills(jd)
        all_skills.extend(skills)

    return dict(Counter(all_skills))


# standalone test
if __name__ == "__main__":
    sample_jobs = [
        "Data Analyst with Python, SQL, Power BI",
        "Machine Learning Engineer with Python, TensorFlow",
        "Data Scientist skilled in NLP, Statistics"
    ]

    result = analyze_job_market(sample_jobs)

    print("📊 Job Market Skill Demand:")
    for k, v in result.items():
        print(f"- {k}: {v}")
