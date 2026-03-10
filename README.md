# GMailCleaner
Clean my Gmail account

Steps:
1. Create virtual env: python -m venv .venv
2. Activate virtual env: . ./.venv/bin/activate
3. Install packages: pip install -f requirements.txt
4. Add an Google OAUTH 2.0 token. https://developers.google.com/workspace/guides/create-credentials#desktop-app
5. Add the scope https://www.googleapis.com/auth/gmail.modify to the API access https://developers.google.com/identity/protocols/oauth2/scopes
5. set the variable "delete=True" in cleaner.py
6. Run it! (python cleaner.py)


