from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Uncomment to test this function directly
# transcript = "Your full transcript goes here..."
# summary = summarize_text(transcript)
# print("Summary:", summary)
