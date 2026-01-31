import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


import streamlit as st

from backend.resume_parser import parse_resume
from backend.jd_parser import parse_job_description
from backend.skill_matcher import calculate_match_score
#from backend.llm_feedback import generate_feedback

def clean_feedback(text):
    if not text:
        return "No AI feedback available."

    lines = text.splitlines()
    useful_lines = [
        line.strip()
        for line in lines
        if len(line.strip()) > 20
    ]

    return "\n".join(useful_lines[:6])

st.set_page_config(
    page_title="Resume Analyzer tool",
    page_icon="📄"
)

st.title("📄 Resume Analyzer tool")

# ---------- UI INPUTS ----------
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

# ---------- ACTION ----------
if st.button("Analyze Resume"):

    if not resume_file or not job_description.strip():
        st.warning("Please upload a resume and paste a job description.")
        st.stop()

    with st.spinner("Analyzing resume..."):

        # Save uploaded resume temporarily
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())

        # Parse resume and JD
        resume_data = parse_resume("temp_resume.pdf", skill_list=None)
        jd_data = parse_job_description(job_description, skill_list=None)

        # Calculate ML-based match score (TF-IDF)
        match_score = calculate_match_score(
            resume_data["text"],
            jd_data["text"]
        )

        # Generate AI feedback using LLM
        #ai_feedback = generate_feedback(
            #resume_data["text"],
            #jd_data["text"],
            #match_score
        #)

    # ---------- OUTPUT ----------
    st.subheader("📊 Match Score")
    st.metric("Resume Match", f"{match_score}%")

    if match_score >= 75:
        st.success("Strong match for this role")
    elif match_score >= 50:
        st.warning("Moderate match – improvements recommended")
    else:
        st.error("Low match – significant improvements needed")
        
        st.subheader("🤖 AI Feedback")
        st.info("AI feedback is available in local mode. "
    "This cloud demo focuses on resume–job match scoring.")
