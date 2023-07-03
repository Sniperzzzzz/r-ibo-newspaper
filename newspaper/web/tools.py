import requests

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '1125149818793230447'
CLIENT_SECRET = 'cR0nAA1TACk-RbpmnAm1aquMzAADQEID'
REDIRECT_URI = 'https://127.0.0.1:8000'

def exchange_code(code):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': 'https://127.0.0.1:8000'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
  r.raise_for_status()
  return r.json()