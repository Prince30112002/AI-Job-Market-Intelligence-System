# app.py
# Entry point of AI Job Market Intelligence System

from src.skill_extractor import extract_skills_from_text
from src.job_market_analyzer import analyze_job_market
from src.skill_trend_visualizer import (
    plot_skill_demand_bar,
    plot_skill_demand_pie
)

# -----------------------------
# Sample Input Data
# -----------------------------
sample_job_descriptions = [
    "We are looking for a Data Analyst with strong Python, SQL, and Statistics skills.",
    "Machine Learning Engineer required with Python, ML, Deep Learning, and TensorFlow.",
    "Data Scientist role requiring Python, SQL, NLP, and Machine Learning experience."
]

# -----------------------------
# Main App Logic
# -----------------------------
def main():
    print("🚀 AI Job Market Intelligence System Started\n")

    # Analyze job market
    skill_demand = analyze_job_market(sample_job_descriptions)

    print("📊 Job Market Skill Demand:\n")
    for skill, count in skill_demand.items():
        print(f"- {skill}: {count}")

    # Visualizations
    plot_skill_demand_bar(skill_demand)
    plot_skill_demand_pie(skill_demand)


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    main()
