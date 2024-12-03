import sys
from transformers import pipeline

def summarize_text(file_path):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

