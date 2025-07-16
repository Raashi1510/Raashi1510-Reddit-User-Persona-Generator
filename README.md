Reddit User Persona Generator 🧑‍💻📊
Scrape a Reddit user’s posts/comments, analyze them with Google Gemini AI, and generate a detailed persona report (personality, interests, communication style, and values).

✨ Features
✅ Scrapes latest Reddit posts & comments
✅ Analyzes using Gemini AI (powered by Google)
✅ Generates structured persona with key traits & citations
✅ Saves results in output/[username]_persona.txt

🚀 Quick Start
1. Prerequisites
Python 3.10+

A Google Gemini API Key (Get it here)

A Reddit API Key (Get it here)

2. Installation
bash
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator
pip install -r requirements.txt
3. Configure API Keys
Create a .env file:

env
REDDIT_CLIENT_ID="your_reddit_client_id"  
REDDIT_CLIENT_SECRET="your_reddit_client_secret"  
GEMINI_API_KEY="your_google_gemini_api_key"  
4. Run the Script
bash
python main.py --url "https://www.reddit.com/user/kojied/"
Output: output/kojied_persona.txt

⚙️ Customization
Adjust Scraping Limits
Modify reddit_scraper.py to change the number of posts/comments fetched:

python
for post in redditor.submissions.new(limit=10):  # Change from 20 → 10
for comment in redditor.comments.new(limit=10):  # Change from 20 → 10
Switch Gemini Model
Edit persona_generator.py to use a different model (if hitting rate limits):

python
model = genai.GenerativeModel("gemini-1.5-flash")  # Faster, lower cost
⚠️ Troubleshooting
1. "429 Quota Exceeded" Error
Solution:

Wait a few minutes before retrying.

Reduce posts/comments in reddit_scraper.py.

Use gemini-1.5-flash instead of gemini-1.5-pro.

Upgrade to a paid plan.

2. "404 Model Not Found" Error
Solution:

bash
pip install --upgrade google-generativeai  # Update the library
Then verify available models:

bash
python list_models.py  # (See repo for script)
3. Reddit API Errors
Ensure your Reddit API keys are correct.

Check if the user exists (https://reddit.com/user/[username]).

📂 Project Structure
text
reddit-persona-generator/
├── .env.example          # Template for API keys  
├── main.py              # CLI entry point  
├── reddit_scraper.py    # Fetches Reddit data  
├── persona_generator.py # Analyzes with Gemini  
├── utils.py             # Helper functions  
├── output/              # Generated personas  
└── requirements.txt     # Python dependencies  
📜 License
MIT © [Your Name]

🔗 Useful Links
Google Gemini API Docs

Reddit API Guide
