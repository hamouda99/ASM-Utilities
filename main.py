import os
import telebot

API_KEY =  "5077024786:AAEpTYGCsHm--t1FXU2fJJqfPKHvtVRvhII"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def greet (message):
    bot.reply_to(message, "Bella li")

bot.polling()
