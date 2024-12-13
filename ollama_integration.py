import subprocess

def run_ollama(prompt, model="llama3:latest"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8"  # Ensure encoding is explicitly set
        )
        if result.returncode != 0:
            print("Error:", result.stderr)
            return None
        return result.stdout.strip()
    except Exception as e:
        print("Error during LLaMA subprocess call:", e)
        return None
