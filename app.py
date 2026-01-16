"""
AI Job Market Intelligence System
Main Application File
"""

from src.skill_extractor import extract_skills
from src.job_market_analyzer import analyze_job_market
from src.skill_trend_visualizer import (
    plot_skill_demand_bar,
    plot_skill_demand_pie
)

# -----------------------------
# Sample Job Descriptions
# -----------------------------
job_descriptions = [
    "We are hiring a Data Analyst with strong Python, SQL and Statistics skills",
    "Looking for a Machine Learning Engineer with Python, TensorFlow and Deep Learning experience",
    "Data Scientist required with NLP, Cloud, Python and Machine Learning knowledge",
    "Business Analyst having Power BI, SQL and Data Analysis experience"
]

# -----------------------------
# Main Execution
# -----------------------------
def main():
    print("🚀 AI Job Market Intelligence System Started...\n")

    skill_demand = analyze_job_market(job_descriptions)

    print("📊 Job Market Skill Demand:")
    for skill, count in skill_demand.items():
        print(f"- {skill}: {count}")

    plot_skill_demand_bar(skill_demand)
    plot_skill_demand_pie(skill_demand)


if __name__ == "__main__":
    main()
