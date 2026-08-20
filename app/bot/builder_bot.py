from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from app.bot.keyboards import main_menu


WELCOME_TEXT = """
🚀 Welcome To Telegram Bot Builder

Create and Manage Telegram Bots

Features:

✅ Create Unlimited Bots
✅ Auto Deployment
✅ Subscription System
✅ Payment Gateway
✅ Admin Panel

Choose an option below.
"""


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=main_menu()
    )


async def menu_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "create_bot":
        await query.message.reply_text(
            "🤖 Send Bot Token"
        )

    elif data == "my_bots":
        await query.message.reply_text(
            "📦 Your Bots"
        )

    elif data == "subscription":
        await query.message.reply_text(
            """
💎 Premium Plans

1 Day - ₹10
7 Days - ₹30
28 Days - ₹50
84 Days - ₹100
168 Days - ₹150
365 Days - ₹250
Permanent - ₹499
"""
        )

    elif data == "help":
        await query.message.reply_text(
            "📚 Contact Admin"
        )


def build_application(
    token: str
):
    app = Application.builder().token(
        token
    ).build()

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            menu_callback
        )
    )

    return app