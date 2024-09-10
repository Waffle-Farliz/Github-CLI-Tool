from github import Github, GithubException
from dotenv import load_dotenv
import sys
import os

load_dotenv()


class Gh:
    g__ = Github(os.getenv("ACCESS_TOKEN"))

    def exception_handler(foo):
        def wrapper(self, *args):
            try:
                foo(self, *args)
            except GithubException as e:
                raise Exception(
                    f"message: {e.message}, status: {e.status}, data: {e.data}"
                )
            except Exception as e:
                raise e

        return wrapper

    @exception_handler
    def get_user(self, username):
        self.user = self.g__.get_user(username)

        print(f"Found user: {self.user.url}")

    @exception_handler
    def get_repositories(self):
        self.repositories = self.user.get_repos()

        for repo in self.repositories:
            print(f"Found a public repository: {repo.url}")
            print("--------")

    @exception_handler
    def get_events(self):
        self.events = self.user.get_public_events()

        for event in self.events:
            print(f"Event Type: {event.type}")
            print(f"Repository: {event.repo.name}")
            print(f"Date and Time: {event.created_at}")
            print("--------")


if __name__ == "__main__":
    git = Gh()

    if len(sys.argv) == 2:
        git.get_user(sys.argv[1])
    else:
        git.get_user("Waffle-Farliz")

    git.get_repositories()
    git.get_events()
