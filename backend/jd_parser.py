import re


def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_job_description(jd_text, skill_list=None):
    """
    Parses and cleans job description text.
    """
    return {
        "text": clean_text(jd_text)
    }