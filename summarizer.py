import subprocess

def summarize(text):
    prompt = f"""
Summarize the following in 2 short sentences.
Tell me why this matters to a software engineer.
If it is low value, say so clearly.

Text:
{text}
"""

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        capture_output=True,
        text=True
    )

    return result.stdout.strip()


