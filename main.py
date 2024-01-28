import telebot
bot = telebot.TeleBot('6331719854:AAEF9o8sf1U64jKGCBtMoeY1Gj9YxbNooGw')

@bot.message_handler(commands=['start', 'alo'])
def main(msg):
    knopka = telebot.types.InlineKeyboardMarkup(row_width=1)
    but = telebot.types.InlineKeyboardButton('one', callback_data='one')
    but2 = telebot.types.InlineKeyboardButton('two', callback_data='two')
    knopka.add(but, but2)

    bot.send_message(msg.chat.id, 'выбирай оне или ту', reply_markup=knopka)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'one':
            bot.send_message(call.message.chat.id, 'ааа')
        if call.data == 'two':
            bot.send_message(call.message.chat.id, 'ffffа')


bot.infinity_polling()



















