import telebot

from config import KEYS, TOKEN
from extensions import CountArguments, APIWorker, CompareCurrencies

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу введите данные в следующем порядке: имя валюты, в какую валюту перевести, количество\n" \
           " переводимой валюты\n" \
           "Чтобы посмотреть доступные валюты используйте команду /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:\n"
    for key in KEYS.keys():
        text = '\n'.join((text, key,))
        # text += f'{key}\n'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise CountArguments('ERROR: Неверное количество параметров')
        quote, base, amount = values

        total_base = APIWorker.get_price(quote, base, amount)

        response = f'Цена {amount} {quote} в {base} - {total_base:.3f} '
        bot.send_message(message.chat.id, response)
    except CountArguments as e:
        bot.send_message(message.chat.id, e)
    except CompareCurrencies as e:
        bot.send_message(message.chat.id, e)
    except KeyError as e:
        bot.send_message(message.chat.id, f'ERROR: Бот не знает такой валюты: {e}')


bot.polling(none_stop=True)