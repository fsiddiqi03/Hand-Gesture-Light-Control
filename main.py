import json
import requests



USERNAME = 'WsfVEVewL-anLIY2bNfxBP5QNFIIt2aK52htFMGA'
BRIDGE_IP = '10.0.0.239'
LIGHT_ID = 1

url = f"https://{BRIDGE_IP}/api/{USERNAME}/lights/{LIGHT_ID}/state"

payload = json.dumps({
    "on": True
})


headers = {
    "Content-Type": "application/json"
}

response = requests.put(url, headers=headers, data=payload, verify=False)
print(response.text)