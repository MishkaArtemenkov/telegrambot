import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

words = []  # хранение в памятиpy


@bot.message_handler(commands=["add"])
def add(message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        return bot.reply_to(message, "Используй: /add слово")
    words.append(text[1])
    bot.reply_to(message, "Добавлено")


@bot.message_handler(commands=["list"])
def list_words(message):
    bot.reply_to(message, "\n".join(words) if words else "Список пуст")


@bot.message_handler(commands=["clear"])
def clear(message):
    words.clear()
    bot.reply_to(message, "Список очищен")


bot.infinity_polling()
