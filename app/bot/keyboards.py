from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


def main_menu_keyboard():

    keyboard = [
        [
            InlineKeyboardButton(
                "➕ Add Bot",
                callback_data="add_bot"
            )
        ],
        [
            InlineKeyboardButton(
                "🤖 My Bots",
                callback_data="my_bots"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 Subscription",
                callback_data="plans"
            )
        ],
        [
            InlineKeyboardButton(
                "👤 My Account",
                callback_data="account"
            )
        ],
        [
            InlineKeyboardButton(
                "📚 Help",
                callback_data="help"
            )
        ],
        [
            InlineKeyboardButton(
                "🆘 Support",
                callback_data="support"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def plans_keyboard():

    keyboard = [
        [
            InlineKeyboardButton(
                "🔥 1 Day ₹10",
                callback_data="plan_1"
            )
        ],
        [
            InlineKeyboardButton(
                "🔥 7 Days ₹30",
                callback_data="plan_7"
            )
        ],
        [
            InlineKeyboardButton(
                "🔥 28 Days ₹50",
                callback_data="plan_28"
            )
        ],
        [
            InlineKeyboardButton(
                "🔥 84 Days ₹100",
                callback_data="plan_84"
            )
        ],
        [
            InlineKeyboardButton(
                "🔥 168 Days ₹150",
                callback_data="plan_168"
            )
        ],
        [
            InlineKeyboardButton(
                "🔥 365 Days ₹250",
                callback_data="plan_365"
            )
        ],
        [
            InlineKeyboardButton(
                "💎 Permanent ₹499",
                callback_data="plan_permanent"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)