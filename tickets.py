import requests
import json 

TICKET_URL = "https://example.com/api/v1/ticket"

USERNAME = "admin"
PASSWORD = "admin123"

def get_service_ticket():

    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.post(TICKET_URL, json=payload)

    if response.status_code != 200:
        print("❌ Hiba a ticket lekérésekor!")
        print(response.text)
        return None

    data = response.json()

    ticket = data.get("serviceTicket") or data.get("token") or data.get("sessionId")

    print("✅ Service ticket sikeresen lekérve:")
    print(ticket)

    return ticket


if __name__ == "__main__":
    get_service_ticket()

