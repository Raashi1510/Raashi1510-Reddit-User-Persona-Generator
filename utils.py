import os

def extract_username(url):
    return url.rstrip("/").split("/")[-1]

def save_persona_to_file(username, persona):
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", f"{username}_persona.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(persona)
