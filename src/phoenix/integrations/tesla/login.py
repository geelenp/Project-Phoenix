"""
Project Phoenix

Tesla OAuth login utility.
"""

import json
import secrets
import time
import urllib.parse

import requests

from .config import (
    AUTH_URL,
    AUDIENCE,
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI,
    SCOPES,
    TOKEN_URL,
    TOKENS_FILE,
)


def build_login_url():

    state = secrets.token_urlsafe(16)

    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "state": state,
        "audience": AUDIENCE,
    }

    return AUTH_URL + "?" + urllib.parse.urlencode(params)


def exchange_token(code):

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "audience": AUDIENCE,
        "scope": " ".join(SCOPES),
    }

    response = requests.post(
        TOKEN_URL,
        data=payload,
        timeout=30,
    )

    response.raise_for_status()

    tokens = response.json()

    #
    # Store absolute expiration time.
    #

    tokens["expires_at"] = int(time.time()) + tokens["expires_in"]

    return tokens


def save_tokens(tokens):

    with open(TOKENS_FILE, "w") as f:
        json.dump(tokens, f, indent=4)


def main():

    print()
    print("=" * 60)
    print("Tesla Login")
    print("=" * 60)
    print()

    print("1. Open this URL in your browser.")
    print("2. Log in with Tesla.")
    print("3. Approve the application.")
    print("4. Copy only the value after code=")
    print()

    print(build_login_url())
    print()

    code = input("Authorization code: ").strip()

    print()
    print("Requesting tokens...")
    print()

    tokens = exchange_token(code)

    save_tokens(tokens)

    print(f"Tokens saved to {TOKENS_FILE}")


if __name__ == "__main__":
    main()
