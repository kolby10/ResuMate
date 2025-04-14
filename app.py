import streamlit as st
from resume_parser import ResumeParser
from openai_client import ATSAnalyzer

# main function, runs the streamlit app
def main():
    # configures the Streamlit page settings
    st.set_page_config(
        page_title="ResuMate", # browser tab title
        page_icon="📄", # favicon
        layout="wide", # makes page layout wider than Streamlit default
        initial_sidebar_state="expanded" # sets sidebar to be open by default
    )

    # applies custom CSS styling, for improved UI
    st.markdown("""
    <style>
    .job-desc-box {
        border: 1px solid #4f8bf9;
        border-radius: 5px;
        padding: 1rem;
        margin-top: 1rem;
    }
    .stTextArea textarea {
        min-height: 150px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar UI with branding and app information
    with st.sidebar:
        st.image("https://icons.veryicon.com/png/o/miscellaneous/general-icon-library/resume-7.png", width=100)
        st.header("About ResuMate")
        st.markdown("""
        **New Feature!** Now analyzes your resume against specific job descriptions.
        - Keyword matching
        - Role-specific optimization
        - Experience prioritization
        """)
        st.markdown("---")
        st.caption("v1.1 | Job Description Analysis Added")
        st.markdown("---")
        st.caption("Created by Kolby Fannin.")
        st.caption("For source code, citations, and more, visit kolbyfannin.com/ResuMate")
        st.markdown("---")
        st.caption("Powered by OpenAI.")
        st.caption("Visit openai.com/policies/row-privacy-policy for information on how your data is used to power this service")

    # main i/o
    st.title("ResuMate: Job-Tailored Resume Optimizer")

    # Resume upload input
    with st.container():
        st.subheader("1. Upload Your Resume")
        uploaded_file = st.file_uploader(
            "Choose a PDF or DOCX file",
            type=["pdf", "docx"],
            label_visibility="collapsed"
        )

    # job description input, set as optional
    with st.container():
        st.markdown("---")
        st.subheader("2. Add Target Job Description (Optional)")
        st.caption("Paste a job posting below for tailored recommendations")
        job_description = st.text_area(
            "Job description:",
            height=250,
            placeholder="Paste job description here...",
            label_visibility="collapsed"
        )

    # starts analysis if resume is uploaded
    if uploaded_file:
        with st.spinner("🔍 Analyzing your resume - this takes about 20 seconds..."):
            try:
                # extracts text from the uploaded resume file
                text = ResumeParser.extract_text(
                    uploaded_file,
                    uploaded_file.type
                )[:12000]  # reduced to accommodate job desc + ChatGPT token limits

                # utilizes OpenAI api
                analyzer = ATSAnalyzer()
                # sees if a job description was provided
                # if so, trims to first 3k chars to stay within ChatGPT token limits
                jd_text = job_description[:3000] if job_description else None

                # sends resume and/or job description text to OpenAI API
                feedback = analyzer.analyze_resume(
                    resume_text=text,
                    job_description=jd_text
                )

                # displayed when analysis is completed
                st.success("Analysis Complete!")

                # 'tabs' separates OpenAI API response for better readability
                tabs = st.tabs(["Summary Report", "Keyword Analysis", "Raw Text"])

                # content block for first tab, 'summary report'
                with tabs[0]:
                    st.subheader("Tailored Recommendations")
                    st.markdown(feedback.get('summary', ''))

                # content block for second tab
                with tabs[1]:
                    st.subheader("Keyword Matching")
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.markdown("**Present Keywords**")
                        st.markdown("\n".join([f"- {kw}" for kw in feedback.get('present_keywords', [])]))
                    with col_b:
                        st.markdown("**Missing Keywords**")
                        st.markdown("\n".join([f"- {kw}" for kw in feedback.get('missing_keywords', [])]))

                with tabs[2]:
                    st.subheader("Extracted Resume Text")
                    st.code(text, language='text')

                # prepare and offer downloadable analysis report
                report_content = f"ResuMate Analysis Report\n\n{feedback.get('summary', '')}"
                st.download_button(
                    label= "Download Full Report",
                    data=report_content,
                    file_name="resumate_analysis_report.txt"
                )


            except Exception as e:
                st.error(f"Analysis Failed: {str(e)}")
                st.exception(e)

# run the app
if __name__ == "__main__":
    main()