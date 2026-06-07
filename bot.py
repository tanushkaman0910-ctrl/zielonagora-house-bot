import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = """🏡 Перевірка нерухомості

🔹 Таунхауси:
• Зелена Гура + околиці
• до 650 000 zł
• ділянка від 150 м²

🔹 Квартири:
• Оседле Пшиязні
• П'ястовське
• Нове Затишшя
• 3 кімнати
• 60–65 м²
• до 450 000 zł

Це тестове повідомлення. Якщо ти його отримала в Telegram — бот працює! 🎉
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
