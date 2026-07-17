import requests

from config import CLIENT_ID, CLIENT_SECRET

TOKEN_URL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"
API_URL = "https://fleet-api.prd.eu.vn.cloud.tesla.com/api/1/partner_accounts"

AUDIENCE = "https://fleet-api.prd.eu.vn.cloud.tesla.com"


def get_partner_token():

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": AUDIENCE,
        "scope": "openid vehicle_device_data",
    }

    response = requests.post(
        TOKEN_URL,
        data=payload,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()["access_token"]


def load_csr():

    with open(
        "tools/tesla/keys/com.tesla.3p.csr",
        "r",
    ) as f:

        return f.read()


def register_partner(token):

    payload = {
        "domain": "ftt-forensics.be",
        "csr": load_csr(),
    }

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=30,
    )

    print("Status:", response.status_code)
    print()
    print(response.text)


def main():

    token = get_partner_token()
    register_partner(token)


if __name__ == "__main__":
    main()
