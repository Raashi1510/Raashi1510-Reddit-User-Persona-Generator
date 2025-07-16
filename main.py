import argparse
from reddit_scraper import scrape_user_data
from persona_generator import generate_persona
from utils import save_persona_to_file, extract_username

def main():
    parser = argparse.ArgumentParser(description="Reddit User Persona Generator")
    parser.add_argument("--url", type=str, required=True, help="Reddit profile URL")
    args = parser.parse_args()

    username = extract_username(args.url)
    print(f"[INFO] Extracted username: {username}")

    print("[INFO] Scraping Reddit data...")
    user_data = scrape_user_data(username)

    print("[INFO] Generating persona using LLM...")
    persona = generate_persona(username, user_data)

    print("[INFO] Saving persona to file...")
    save_persona_to_file(username, persona)

    print(f"[DONE] Persona generated for u/{username} in output/{username}_persona.txt")

if __name__ == "__main__":
    main()
