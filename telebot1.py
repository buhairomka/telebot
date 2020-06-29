import telebot
import requests

TOKEN="1242377977:AAFTSQV6xu6lCWOgG6TagrJo-A1dYk6LT_A"

bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(chat_id=message.chat.id, text='этот бот будет отвечать тебе только на 2 комманды: \n'
                                                   '\'мое имя\' и \'мой ник\'')

# @bot.message_handler()
# def names(message):
#     print(message.chat.id)
#     print(message.text)
#     if message.text=='мое имя':
#         bot.send_message(chat_id=message.chat.id, text=message.from_user.first_name)
#     elif message.text=='мой ник':
#         bot.send_message(chat_id=message.chat.id, text=message.from_user.username)
#     else:
#         bot.send_message(chat_id=message.chat.id, text="are you debil?")

@bot.message_handler()
def replyToNikita(message):
    print(message.chat.id)
    print(message.text)
    if message.chat.id==390236447:
        bot.send_message(chat_id=563113185,text=message.text)
    if message.chat.id==563113185:
        bot.send_message(chat_id=390236447,text=message.text)

me=390236447
nik=563113185

if __name__ == '__main__':
    bot.polling(none_stop=True)