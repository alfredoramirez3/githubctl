import os

from dotenv import load_dotenv

load_dotenv()

print(os.getenv('GITHUB_TOKEN'))
print(os.environ.get("GITHUB_TOKEN"))
