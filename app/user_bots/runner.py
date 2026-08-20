import asyncio

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)


class UserBotRunner:

    def __init__(
        self,
        bot_id: int,
        token: str
    ):
        self.bot_id = bot_id
        self.token = token
        self.application = None
        self.task = None

    async def start_command(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ):
        await update.message.reply_text(
            "👋 Welcome!\n\n"
            "This bot was created using "
            "Telegram Bot Builder."
        )

    async def help_command(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ):
        await update.message.reply_text(
            "/start\n/help\n/about"
        )

    async def about_command(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ):
        await update.message.reply_text(
            "Built using Telegram Bot Builder."
        )

    async def start(self):

        self.application = (
            Application.builder()
            .token(self.token)
            .build()
        )

        self.application.add_handler(
            CommandHandler(
                "start",
                self.start_command
            )
        )

        self.application.add_handler(
            CommandHandler(
                "help",
                self.help_command
            )
        )

        self.application.add_handler(
            CommandHandler(
                "about",
                self.about_command
            )
        )

        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()

    async def stop(self):

        if not self.application:
            return

        await self.application.updater.stop()
        await self.application.stop()
        await self.application.shutdown()