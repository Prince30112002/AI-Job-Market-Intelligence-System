import matplotlib.pyplot as plt

# Skill demand data (output from job_market_analyzer)
skill_demand = {
    "Python": 3,
    "Machine Learning": 2,
    "SQL": 2,
    "Statistics": 2,
    "Data Analyst": 1,
    "Power BI": 1,
    "Cloud": 1,
    "Deep Learning": 1,
    "NLP": 1,
    "TensorFlow": 1,
    "Data Scientist": 1
}

def plot_skill_demand_bar(skill_data):
    skills = list(skill_data.keys())
    demand = list(skill_data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(skills, demand)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Skills")
    plt.ylabel("Demand Count")
    plt.title("📊 Job Market Skill Demand Trend")
    plt.tight_layout()
    plt.show()

def plot_skill_demand_pie(skill_data):
    plt.figure(figsize=(8, 8))
    plt.pie(
        skill_data.values(),
        labels=skill_data.keys(),
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title("🥧 Skill Demand Distribution")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_skill_demand_bar(skill_demand)
    plot_skill_demand_pie(skill_demand)
