# app.py
import streamlit as st
import pandas as pd
from resume_utils import extract_text_from_resume, ats_score
from pathlib import Path

st.set_page_config(page_title="Resume Ranker AI", layout="wide")
st.title("📄 Resume Ranking AI Dashboard")

st.markdown("""
Upload multiple resumes (PDF) and paste a Job Description (JD) below.
This tool will automatically rank resumes based on skill match, experience, education, and achievements.
""")

# JD input
jd_text = st.text_area("📝 Paste Job Description (JD) here", height=200)

# Upload resumes
uploaded_files = st.file_uploader("📤 Upload Resumes (PDF only)", type=["pdf"], accept_multiple_files=True)

# Button to process
if st.button("🔍 Rank Resumes") and jd_text and uploaded_files:
    results = []

    with st.spinner("Processing resumes..."):
        for resume in uploaded_files:
            try:
                text = extract_text_from_resume(resume)
                result = ats_score(jd_text, text)
                result["Filename"] = resume.name
                results.append(result)
            except Exception as e:
                st.error(f"Error with {resume.name}: {e}")

    if results:
        df = pd.DataFrame(results).sort_values(by="Total ATS Score (out of 100)", ascending=False)

        # Leaderboard
        st.subheader("🏆 Resume Leaderboard")
        st.dataframe(df[["Filename", "Total ATS Score (out of 100)", "Skill Match Score (40%)", "Experience Score (20%)"]].reset_index(drop=True))

        # Detailed View
        st.subheader("📋 Detailed Resume Reports")
        for idx, row in df.iterrows():
            with st.expander(f"{row['Filename']} — Score: {row['Total ATS Score (out of 100)']}"):
                st.markdown(f"**Intro:** {row['Candidate Intro Line']}")
                st.markdown(f"**Professional Summary:** {row['Professional Summary']}")
                st.markdown(f"**Work Experience Summary:**\n\n```\n{row['Work Experience Summary']}\n```")
                st.markdown(f"**Skills Found:** {', '.join(row['Skills Found'])}")
                st.markdown(f"**Certifications:** {row['Certifications Found']}")
                st.markdown(f"**Leadership Roles:** {row['Leadership Roles Found']}")
                st.markdown(f"**Hackathons/Achievements:** {row['Hackathon/Achievements Found']}")
                st.markdown(f"**Email:** {row['Email']}")
                st.markdown(f"**Phone:** {row['Phone']}")
    else:
        st.warning("No valid resumes found.")
