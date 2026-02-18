from config import MODEL

def summarize_text(text: str):
    """
    """
    prompt = f"Summarize this in 3 lines:\n{text}"
    response = MODEL.generate_content(prompt)
    return response.text