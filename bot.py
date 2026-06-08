import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

SENT_FILE = "sent_links.txt"

CHECK_HOURS = [10, 12, 14, 18]

OTODOM_URL = (
    "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/zielona-gora"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    )
}


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
        },
    )


def load_sent_links():
    if not os.path.exists(SENT_FILE):
        return set()

    with open(SENT_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f)


def save_sent_link(link):
    with open(SENT_FILE, "a", encoding="utf-8") as f:
        f.write(link + "\n")
def check_otodom():
    sent_links = load_sent_links()

    response = requests.get(OTODOM_URL, headers=HEADERS)

    soup = BeautifulSoup(response.text, "lxml")

    links = soup.find_all("a", href=True)
    print("Кількість посилань:", len(links))


    for link in links:
        href = link["href"]

        if "/pl/oferta/" not in href:
            continue

        if href.startswith("/"):
            href = "https://www.otodom.pl" + href

        if href in sent_links:
            continue

        message = (
            "🏠 Знайдено нове оголошення на OtoDom:\n\n"
            f"{href}"
        )

        send_telegram(message)
        save_sent_link(href)

        sent_links.add(href)
        if __name__ == "__main__":
            check_otodom()
