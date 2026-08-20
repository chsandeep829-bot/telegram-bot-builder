from fastapi import APIRouter, Request
import requests
import os

router = APIRouter()

BOT_TOKEN = os.getenv("BOT_BUILDER_TOKEN")

@router.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": "Hello! Bot is working."
                }
            )

    return {"ok": True}
