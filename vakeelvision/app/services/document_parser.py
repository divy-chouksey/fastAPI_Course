import os
from PyPDF2 import PdfReader

def extract_text_pdf(file_path:str)->str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()+"\n"
    return {"text":text.strip(), "page_count": len(reader.pages), "word_count": len(text.split())}



def extract_text_txt(file_path:str)-> str:
    with open(file_path,"r",encoding="utf-8") as f:
        text = f.read()
    return {"text":text.strip(),"word_count": len(text.split()), "page_count": 1}
    


def extract_text(file_path:str) -> str:
    """
    Extracts text from a document"""

    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_pdf(file_path)
    elif ext == ".txt":
        return extract_text_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
