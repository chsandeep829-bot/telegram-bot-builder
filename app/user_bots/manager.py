import asyncio

from app.user_bots.registry import bot_registry


class BotManager:

    def __init__(self):
        self.running_bots = {}

    async def start_bot(
        self,
        bot_id: int,
        token: str
    ):
        try:

            if bot_id in self.running_bots:
                return {
                    "success": False,
                    "message": "Already running"
                }

            from telegram.ext import (
                Application,
                CommandHandler
            )

            application = (
                Application.builder()
                .token(token)
                .build()
            )

            async def start(
                update,
                context
            ):
                await update.message.reply_text(
                    "🤖 Bot Running Successfully"
                )

            application.add_handler(
                CommandHandler(
                    "start",
                    start
                )
            )

            task = asyncio.create_task(
                application.run_polling()
            )

            self.running_bots[
                bot_id
            ] = {
                "task": task,
                "app": application
            }

            bot_registry.register(
                bot_id,
                token
            )

            return {
                "success": True,
                "message": "Bot Started"
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    async def stop_bot(
        self,
        bot_id: int
    ):
        try:

            if bot_id not in self.running_bots:
                return {
                    "success": False,
                    "message": "Bot Not Running"
                }

            app = self.running_bots[
                bot_id
            ]["app"]

            await app.stop()

            del self.running_bots[
                bot_id
            ]

            bot_registry.remove(
                bot_id
            )

            return {
                "success": True,
                "message": "Bot Stopped"
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def list_running_bots(
        self
    ):
        return list(
            self.running_bots.keys()
        )

    def is_running(
        self,
        bot_id: int
    ):
        return (
            bot_id
            in self.running_bots
        )


bot_manager = BotManager()