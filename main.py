import os

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "6276834546:AAF9oLNJm1nLxu2MgU4mcFmT-MGatC4_4nQ"

bot = telebot.TeleBot(BOT_TOKEN)


def content_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Lunch", callback_data="lunch"),
               InlineKeyboardButton("Dinner",callback_data="dinner"),
               InlineKeyboardButton("Activities", callback_data="activities"),
               InlineKeyboardButton("Special", callback_data="special"),
               InlineKeyboardButton("Present", callback_data="present")
               )
    return markup


def start_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Enter", callback_data="enter"),
               InlineKeyboardButton("Exit",callback_data="exit")
               )
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "lunch":
        bot.send_message(call.message.chat.id, "lunch")
    elif call.data == "dinner":
        bot.send_message(call.message.chat.id, "dinner")
    elif call.data == "activities":
        bot.send_message(call.message.chat.id, "activities")
    elif call.data == "special":
        bot.send_message(call.message.chat.id, "special")
    elif call.data == "present":
        bot.send_message(call.message.chat.id, "present")
    elif call.data == "enter":
        bot.send_message(call.message.chat.id, "What would you like to find out??", reply_markup=content_markup())
    elif call.data == "exit":
        bot.send_message(call.message.chat.id, "THERE IS NO EXIT")


@bot.message_handler(commands=['start'])
def message_handler(message):
    welcome_text = "Hi bb, welcome to the bot that will let you know how you will spend your 27th birthday (:"
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown")
    bot.send_message(message.chat.id, "Happy Birthday to my b", reply_markup=start_markup())

# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     welcome_text = "Hi bb, welcome to the bot that will let you know how you will spend your 27th birthday (:"
#     bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown")
#     options_text = "Please enter /birthday to move on"
#     bot.send_message(message.chat.id, options_text, parse_mode="Markdown")
#     bot.send_message(message.chat.id, text='Keyboard example', reply_markup=keyboard)
#
#
# @bot.message_handler(commands=['birthday'])
# def birthday_handler():
#     array_of_values = ('What do you want to know?', '/Lunch', '/Dinner', '/Presents', '/Special')
#     bot.send_message(message.chat.id, text="\n".join(array_of_values))
#
#


@bot.message_handler(commands=['Lunch'])
def lunch_handler(message):
    options_text = "secrettttt lunch"
    bot.send_message(message.chat.id, options_text, parse_mode="Markdown")
#
#
# @bot.message_handler(commands=['Dinner'])
# def dinner_handler(message):
#     options_text = "secrettttt dinner"
#     bot.send_message(message.chat.id, options_text, parse_mode="Markdown")
#
#
# @bot.message_handler(commands=['Presents'])
# def presents_handler(message):
#     options_text = "secrettttt present"
#     bot.send_message(message.chat.id, options_text, parse_mode="Markdown")
#
#
# @bot.message_handler(commands=['Special'])
# def presents_handler(message):
#     options_text = "https://open.spotify.com/track/3Hz3tTQwOdM6XkA0ALB2G9?si=83b4a763f71841cb"
#     bot.send_message(message.chat.id, options_text, parse_mode="Markdown")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    # dp = updater.dispatcher

    # on different commands - answer in Telegram
    # dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))
    # dp.add_handler(CommandHandler("piracy", piracy))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    # dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
