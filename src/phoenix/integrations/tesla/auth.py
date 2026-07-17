"""
Project Phoenix

Tesla authentication.
"""

import json
import time

import requests

from .config import (
    CLIENT_ID,
    CLIENT_SECRET,
    TOKEN_URL,
    AUDIENCE,
    SCOPES,
    TOKENS_FILE,
)


def load_tokens():

    with open(TOKENS_FILE) as f:
        return json.load(f)


def save_tokens(tokens):

    with open(TOKENS_FILE, "w") as f:
        json.dump(tokens, f, indent=4)


def token_expired(tokens):

    return time.time() >= tokens["expires_at"]


def refresh_access_token(tokens):

    payload = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": tokens["refresh_token"],
        "audience": AUDIENCE,
        "scope": " ".join(SCOPES),
    }

    response = requests.post(
        TOKEN_URL,
        data=payload,
        timeout=30,
    )

    response.raise_for_status()

    new_tokens = response.json()

    #
    # Tesla may not always return a new refresh token.
    #

    if "refresh_token" not in new_tokens:
        new_tokens["refresh_token"] = tokens["refresh_token"]

    new_tokens["expires_at"] = (
        int(time.time()) + new_tokens["expires_in"]
    )

    save_tokens(new_tokens)

    return new_tokens


def get_access_token():

    tokens = load_tokens()

    if token_expired(tokens):
        tokens = refresh_access_token(tokens)

    return tokens["access_token"]
