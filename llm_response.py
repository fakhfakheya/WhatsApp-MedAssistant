import subprocess

def llm_response(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama2:7b"],
            input=prompt.encode(),
            capture_output=True,
            timeout=120  # temps suffisant pour que le modèle réponde
        )
        output = result.stdout.decode().strip()
        if not output:
            return "⚠️ LLM n’a rien renvoyé."
        return output
    except subprocess.TimeoutExpired:
        return "⚠️ Timeout : le modèle a mis trop de temps à répondre."
    except Exception as e:
        return f"⚠️ Exception : {e}"
