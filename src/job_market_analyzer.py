# src/job_market_analyzer.py

from collections import Counter
from skill_extractor import extract_skills


def analyze_job_market(job_descriptions):
    """
    Analyze multiple job descriptions and return
    most in-demand skills in the market
    """
    all_skills = []

    for jd in job_descriptions:
        skills = extract_skills(jd)
        all_skills.extend(skills)

    skill_demand = Counter(all_skills)
    return skill_demand


if __name__ == "__main__":
    job_descriptions = [
        """
        We are hiring a Data Analyst with strong SQL, Python,
        Power BI, Statistics, and Machine Learning experience.
        """,
        """
        Looking for an AI Engineer skilled in Python, Deep Learning,
        TensorFlow, NLP, and Cloud platforms.
        """,
        """
        Data Scientist role requiring Python, SQL, Machine Learning,
        Statistics, and Data Visualization skills.
        """
    ]

    market_demand = analyze_job_market(job_descriptions)

    print("📊 Job Market Skill Demand:")
    for skill, count in market_demand.most_common():
        print(f"- {skill}: {count}")
