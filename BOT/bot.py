import telebot


bot = telebot.TeleBot('6827693833:AAG--k01B-PsfsMMNtQUBpQE_jTpO5sRWLE')
@bot.message_handler(commands =['info'])
def info(message):
    bot.send_message(message.chat.id, message)
@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, message.text)



bot.polling(none_stop=True)