import pdfplumber
import re


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return clean_text(text)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_resume(pdf_path, skill_list=None):
    """
    Parses the resume PDF and returns cleaned resume text.
    Skill extraction is no longer done here.
    """
    resume_text = extract_text_from_pdf(pdf_path)

    return {
        "text": resume_text
    }