from openai import OpenAI
import streamlit as st

class ATSAnalyzer:
    def __init__(self):
        self.client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        self.base_prompt = """You are an ATS expert and career coach. Analyze this resume and provide:
        1. Summary of ATS compatibility
        2. Missing and present keywords from job description
        3. Tailored improvement suggestions
        ---
        {job_desc_context}
        ---
        Focus on:
        - Keyword density and placement
        - Experience alignment with job requirements
        - Quantifiable achievements
        - ATS-friendly formatting"""

    def analyze_resume(self, resume_text, job_description=None):
        try:
            job_desc_context = "Job Description Provided:\n" + job_description if job_description else "No job description provided - give general ATS advice."

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.base_prompt.format(job_desc_context=job_desc_context)},
                    {"role": "user", "content": f"RESUME TEXT:\n{resume_text}"}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            return self._parse_response(response.choices[0].message.content)

        except Exception as e:
            return {'error': str(e)}

    def _parse_response(self, raw_text):
        # simple parsing logic, to be expanded during testing
        return {
            'summary': raw_text.split('Summary:')[-1].split('Missing Keywords:')[0].strip(),
            'present_keywords': [],
            'missing_keywords': []
        }