import requests
import json
from ticket import get_service_ticket 

DEVICE_URL = "https://example.com/api/v1/devices"


def list_devices():

    ticket = get_service_ticket()
    if ticket is None:
        return

    headers = {
        "Authorization": f"Bearer {ticket}",
        "Content-Type": "application/json"
    }

    response = requests.get(DEVICE_URL, headers=headers)

    if response.status_code != 200:
        print("❌ Hiba az eszközök lekérésekor!")
        print(response.text)
        return

    devices = response.json()

    if "devices" in devices:
        devices = devices["devices"]

    print("\n--- Hálózati eszközök ---")
    for d in devices:
        platform = d.get("platformId")
        ip = d.get("managementIpAddress")
        print(f"Platform: {platform}  |  Management IP: {ip}")


if __name__ == "__main__":
    list_devices()
