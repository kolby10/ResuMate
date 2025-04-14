import io
from PyPDF2 import PdfReader
from docx import Document

class ResumeParser:
    @staticmethod
    def extract_text(file_buffer, file_type):
        """Extract text from PDF or DOCX files"""
        try:
            if file_type == "application/pdf":
                return ResumeParser._extract_from_pdf(file_buffer)
            elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                return ResumeParser._extract_from_docx(file_buffer)
            else:
                raise ValueError("Unsupported file format")
        except Exception as e:
            raise RuntimeError(f"Text extraction failed: {str(e)}")

    @staticmethod
    def _extract_from_pdf(file_buffer):
        pdf = PdfReader(io.BytesIO(file_buffer.read()))
        return "\n".join([page.extract_text() for page in pdf.pages])

    @staticmethod
    def _extract_from_docx(file_buffer):
        doc = Document(io.BytesIO(file_buffer.read()))
        return "\n".join([para.text for para in doc.paragraphs])