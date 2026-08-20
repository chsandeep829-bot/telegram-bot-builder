from telegram import Update

from telegram.ext import ContextTypes

from app.bot.keyboards import (
    main_menu_keyboard,
    plans_keyboard
)


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    await update.message.reply_text(
        (
            "🤖 Telegram Bot Builder\n\n"
            f"Welcome, {user.first_name}!\n\n"
            "Choose an option:"
        ),
        reply_markup=main_menu_keyboard()
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        (
            "📚 Available Commands\n\n"
            "/start\n"
            "/help\n"
            "/account\n"
            "/mybots\n"
            "/addbot\n"
            "/plans\n"
            "/support"
        )
    )


async def account_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    await update.message.reply_text(
        (
            f"👤 Account\n\n"
            f"Name: {user.first_name}\n"
            f"Username: @{user.username}"
        )
    )


async def plans_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        (
            "💳 Subscription Plans\n\n"
            "🔥 1 Day — ₹10\n"
            "🔥 7 Days — ₹30\n"
            "🔥 28 Days — ₹50\n"
            "🔥 84 Days — ₹100\n"
            "🔥 168 Days — ₹150\n"
            "🔥 365 Days — ₹250\n"
            "💎 Permanent — ₹499"
        ),
        reply_markup=plans_keyboard()
    )


async def addbot_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        (
            "🤖 Add Your Telegram Bot\n\n"
            "1. Open @BotFather\n"
            "2. Create a bot\n"
            "3. Copy the token\n"
            "4. Send the token here\n\n"
            "Never send passwords or OTP codes."
        )
    )


async def support_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        (
            "🆘 Support\n\n"
            "Contact administrator."
        )
    )


async def callback_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "add_bot":

        await query.message.reply_text(
            "Send your BotFather token."
        )

    elif data == "my_bots":

        await query.message.reply_text(
            "Your connected bots will appear here."
        )

    elif data == "plans":

        await query.message.reply_text(
            "Choose a subscription plan.",
            reply_markup=plans_keyboard()
        )

    elif data == "account":

        await query.message.reply_text(
            "Account details."
        )

    elif data == "help":

        await query.message.reply_text(
            "Use /help"
        )

    elif data == "support":

        await query.message.reply_text(
            "Support section."
        )