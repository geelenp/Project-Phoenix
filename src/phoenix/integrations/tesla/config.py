"""
Project Phoenix

Tesla configuration.
"""

from pathlib import Path

CLIENT_ID = "4c886d7b-0681-4164-968e-7f71bd34389d"
CLIENT_SECRET = "ta-secret.37IBlt2nQRPSOFqB"

BASE_DIR = Path(__file__).parent

TOKENS_FILE = BASE_DIR / "tokens.json"

REDIRECT_URI = "http://localhost:5000/callback"

AUTH_URL = "https://auth.tesla.com/oauth2/v3/authorize"

TOKEN_URL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"

AUDIENCE = "https://fleet-api.prd.eu.vn.cloud.tesla.com"

BASE_URL = "https://fleet-api.prd.eu.vn.cloud.tesla.com/api/1"

SCOPES = [
    "openid",
    "offline_access",
    "vehicle_device_data",
]
