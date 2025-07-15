Resume AI Ranker Dashboard
An AI-powered Resume Ranking System that evaluates multiple PDF resumes against a given job description using a standardized ATS-style scoring system.
Built using Python, Streamlit, and NLP techniques. No OpenAI API key is required.

Features
Upload one or more resumes (PDF format)

Input a job description (JD)

Automatically extracts:

Contact Information (Email, Phone)

Candidate Introduction Line

Professional Summary

Work Experience Summary

Certifications, Leadership, and Hackathon Achievements

ATS-style resume scoring:

Skill Match (40%)

Experience Match (20%)

Education (10%)

Soft Skills (10%)

JD Similarity (20%)

Bonus Achievements (up to 10%)

Leaderboard view to rank resumes

Export results as CSV

Simple, clean dashboard built with Streamlit

How It Works
Uses pdfplumber to extract text content from resumes

Uses regex and keyword-based methods for parsing and scoring

Uses TF-IDF and cosine similarity to compare resumes with the job description

Calculates an overall ATS score with clearly weighted components

Project Structure
bash
Copy
Edit
resume-ai-ranker/
├── app.py                # Streamlit application
├── resume_utils.py       # Resume extraction and scoring logic
├── resumes/              # Folder containing uploaded PDF resumes
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
Getting Started
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
Requirements
Python 3.7+

Streamlit

Pandas

Scikit-learn

pdfplumber

Install them using:

bash
Copy
Edit
pip install -r requirements.txt
Output
Sorted leaderboard of resumes based on ATS score

Skill match breakdown

Summary of achievements and work experience

Exportable CSV file with results

Extensions and Ideas
Support for DOCX and text-based resumes

LLM integration for deeper semantic understanding (optional)

Resume suggestions or improvements

Deployment on Streamlit Cloud or Render

Author
Vedant Kate
Feel free to fork, customize, and use for placements, hackathons, or real-world HR use cases.
