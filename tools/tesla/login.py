import json
import secrets
import urllib.parse
import webbrowser

import requests

from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

AUTH_URL = "https://auth.tesla.com/oauth2/v3/authorize"
TOKEN_URL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"
AUDIENCE = "https://fleet-api.prd.eu.vn.cloud.tesla.com"

SCOPES = [
    "openid",
    "offline_access",
    "vehicle_device_data",
]


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

    url = AUTH_URL + "?" + urllib.parse.urlencode(params)

    return url


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

    return response.json()


def save_tokens(tokens):

    with open("tools/tesla/tokens.json", "w") as f:
        json.dump(tokens, f, indent=4)


def main():

    url = build_login_url()

    print()
    print("=" * 60)
    print("Tesla Login")
    print("=" * 60)
    print()
    print("1. Open de onderstaande URL.")
    print("2. Log in bij Tesla.")
    print("3. Geef toestemming.")
    print("4. Kopieer ALLEEN de waarde achter code=")
    print()

    print(url)
    print()

#    webbrowser.open(url)

    code = input("Authorization code: ").strip()

    print()
    print("Token ophalen...")
    print()

    tokens = exchange_token(code)

    save_tokens(tokens)

    print("Tokens opgeslagen in tools/tesla/tokens.json")


if __name__ == "__main__":
    main()
