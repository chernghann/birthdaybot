import logging

from telegram.ext import Updater, CommandHandler, MessageHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

BOT_TOKEN = "6276834546:AAF9oLNJm1nLxu2MgU4mcFmT-MGatC4_4nQ"

import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
#     keyboard = [
#         [
#             InlineKeyboardButton("Lunch", callback_data="Niche Savoureuse 128 Lor 1 Toa Payoh, #01-833, Blk, Singapore 310128 followed by a visit to HDB Hub at Toapayoh"),
#             InlineKeyboardButton("Dinner", callback_data="Arbora 109 Mount Faber Road Faber Peak Singapore Singapore (099203) "),
#         ],
#         [InlineKeyboardButton("Activity", callback_data="Terrarium Workshop (Funan) Address: Funan, 107 North Bridge Road, #04-11, Singapore 179105 ")],
#     ]
    
    keyboard = [
        [
            InlineKeyboardButton("Lunch", callback_data="Lunch"),
            InlineKeyboardButton("Dinner", callback_data="Dinner"),
        ],
        [InlineKeyboardButton("Activity", callback_data="Activity")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Happy Birthday bb!!! Please choose:", reply_markup=reply_markup)


def startdd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Lunch", callback_data="Lunch"),
            InlineKeyboardButton("Dinner", callback_data="Dinner"),
        ],
        [InlineKeyboardButton("Activity", callback_data="Activity")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Happy Birthday bb!!! Please choose:", reply_markup=reply_markup)
    

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    if query.data == "Lunch": 
        await query.edit_message_text(text=f"Niche Savoureuse @ ToaPayoh followed by a visit to HDB Hub")
        startdd(update, context)
    elif query.data == "Dinner":
        await query.edit_message_text(text=f"Arbora @ Mount Faber")
        startdd(update, context)
    elif query.data == "Activity":
        await query.edit_message_text(text=f"Terrarium Workshop @ FUNAN")
        startdd(update, context)
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))
    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
