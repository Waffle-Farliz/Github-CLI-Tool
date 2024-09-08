from github import Github
from dotenv import load_dotenv
import sys
import os

load_dotenv()

g = Github(os.getenv("ACCESS_TOKEN"))

username = sys.argv[1]

user = g.get_user(username)


events = user.get_public_events()

for event in events:
    print(f"Event Type: {event.type}")
    print(f"Repository: {event.repo.name}")
    print(f"Date and Time: {event.created_at}")
    print("--------")
