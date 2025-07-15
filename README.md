## Resume AI Ranker Dashboard

An AI-powered Resume Ranking System that evaluates multiple PDF resumes against a given job description using a standardized ATS-style scoring system.  
Built using Python, Streamlit, and NLP techniques. No OpenAI API key is required.

---

## Features

- Upload one or more resumes (PDF format)
- Input a job description (JD)
- Automatically extracts:
  - Contact Information (Email, Phone)
  - Candidate Introduction Line
  - Professional Summary
  - Work Experience Summary
  - Certifications, Leadership, and Hackathon Achievements
- ATS-style resume scoring:
  - Skill Match (40%)
  - Experience Match (20%)
  - Education (10%)
  - Soft Skills (10%)
  - JD Similarity (20%)
  - Bonus Achievements (up to 10%)
- Leaderboard view to rank resumes
- Export results as CSV
- Simple, clean dashboard built with Streamlit

---

## How It Works

- Uses `pdfplumber` to extract text content from resumes
- Uses regex and keyword-based methods for parsing and scoring
- Uses TF-IDF and cosine similarity to compare resumes with the job description
- Calculates an overall ATS score with clearly weighted components

---

## Project Structure

resume-ai-ranker/
├── app.py # Streamlit application
├── resume_utils.py # Resume extraction and scoring logic
├── resumes/ # Folder containing uploaded PDF resumes
└── README.md # Project documentation

---

## Getting Started
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/resume-ai-ranker.git
cd resume-ai-ranker
Step 2: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Add Resumes
Place all the PDF resumes inside the resumes/ directory.

Step 4: Run the Application
bash
Copy
Edit
streamlit run app.py





Author
Vedant Kate
This project is open-source and can be customized for placement prep, college projects, HR automation, or hackathons.

