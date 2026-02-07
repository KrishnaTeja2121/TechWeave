import subprocess

out = subprocess.run(
    ["ollama", "run", "mistral"],
    input="Summarize Hacker News in one sentence.",
    text=True,
    capture_output=True
)

print(out.stdout)
