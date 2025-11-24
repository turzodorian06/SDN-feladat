import requests
import json

# API végpont a tickethez – ezt írd át a sajátodra
TICKET_URL = "https://example.com/api/v1/ticket"

# Ha kell, akkor ide írd be a felhasználónevet / jelszót
USERNAME = "admin"
PASSWORD = "admin123"

def get_service_ticket():
    """
    Lekéri az adminisztrációhoz szükséges service ticket-et.
    """
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

    # A legtöbb API így adja vissza (ha máshogy, átírom)
    ticket = data.get("serviceTicket") or data.get("token") or data.get("sessionId")

    print("✅ Service ticket sikeresen lekérve:")
    print(ticket)

    return ticket


# Ha közvetlenül futtatják
if __name__ == "__main__":
    get_service_ticket()
