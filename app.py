import streamlit as st
import sys
import os

# 🔧 Fix import path (VERY IMPORTANT)
sys.path.append(os.path.abspath("src"))

from skill_extractor import extract_skills
from job_market_analyzer import analyze_job_market
from skill_trend_visualizer import plot_skill_trends

# -----------------------------
# Streamlit App Config
# -----------------------------
st.set_page_config(
    page_title="AI Job Market Intelligence System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Job Market Intelligence System")
st.markdown(
    "Analyze job descriptions, extract in-demand skills, and visualize job market trends using AI."
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("📂 Upload Job Descriptions")
uploaded_files = st.sidebar.file_uploader(
    "Upload job description text files",
    type=["txt"],
    accept_multiple_files=True
)

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_files:
    all_text = ""

    for file in uploaded_files:
        text = file.read().decode("utf-8")
        all_text += text + "\n"

    # 🔹 Skill Extraction
    st.subheader("🧠 Extracted Skills")
    skills = extract_skills(all_text)

    if skills:
        st.success(f"Total Skills Found: {len(skills)}")
        st.write(", ".join(skills))
    else:
        st.warning("No skills detected.")

    # 🔹 Job Market Analysis
    st.subheader("📊 Job Market Skill Demand")
    skill_demand = analyze_job_market(all_text)

    if skill_demand:
        for skill, count in skill_demand.items():
            st.write(f"**{skill}** : {count}")

        # 🔹 Visualization
        st.subheader("📈 Skill Trend Visualization")
        plot_skill_trends(skill_demand)
        st.pyplot()
    else:
        st.warning("Not enough data to analyze trends.")

else:
    st.info("👈 Upload one or more job description `.txt` files to begin analysis.")
