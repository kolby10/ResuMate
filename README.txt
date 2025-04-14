// What does ResuMate do?

ResuMate allows users to tailor their resumes to work better with
Applicant Tracking System (ATS) programs. This encourages a users resume
to get past automated systems and into the hands of recruiters.

* ResuMate v1.1 allows the input of job descriptions to tailor a users resume
around their desired position.

// Why does this matter?

Sufiyan I. claimed on his LinkedIn post that "Up to 75% of resumes are rejected by ATS before a human ever sees them"
ResuMate makes sure your hard work gets seen.

// How does it work?

1. Upload your resume (PDF or Word)
2. Input a job description for your targeted position (optional)
3. Receive customized recommendations to optimize your application

// Program Breakdown

User Interface is handled through Streamlit
- Handles resume uploads
- Provides fields for entering job descriptions
- Displays AI API results across multiple tabs
- Allows downloading of reports

Document Processing
- Uses PyPDF2 to extract texts from PDF resumes
- Employs python-docx for processing Word documents
- Trims extracted content (both from Resume upload + from optional job description) to meet AI processing limits

AI Analysis Engine
- Uses OpenAI's API for intelligent text analysis
- Implements the ATSAnalyzer class to compare resume content against job requirements
- Returns customized recommendations based on identified gaps

Results Generation
- Creates summary reports with actionable feedback
- Produces keyword analysis highlighting both present and missing terms
- Provides verification of extracted text content
- Formats a downloadable report for user reference

// Technology Stack

Core Framework
- Python with Streamlit for responsive web UI

File Parsing
- PyPDF2 for PDF document parsing
- python-docx for Word document parsing

AI Analysis
- OpenAI API (GPT Model) for intelligent content recommendations

Utilities
- io for in-memory file handling
- python-dotenv for secure environment variable management

// Link to live demo

ResuMate is currently available for live demo on request.

// How to run ResuMate locally

- Install Dependencies
pip install -r requirements.txt

- Create a config.py file in project root, add
OPENAI_API_KEY=your_api_key_here
(Visit OpenAI to obtain your personal API key)

- Run the App via terminal
streamlit run app.py

// Documentation
Streamlit - https://docs.streamlit.io/
Python-Docx - https://python-docx.readthedocs.io/en/latest/
PyPDF2 - https://github.com/py-pdf/pypdf
OpenAI API - https://platform.openai.com/docs
Streamlit File Upload Guide - https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
Resume Icon - https://www.veryicon.com/
https://github.com/OmkarPathak/pyresparser
https://github.com/deepakpadhi986/AI-Resume-Analyzer
https://github.com/ArthurDelamare/Job-Matcher