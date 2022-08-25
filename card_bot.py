# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# В google colab добавить: !pip install Faker
# для установки необходимо в файл requirements.text добавить строки
# 'PyTelegramBotApi'
# 'faker'

from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='ВВЕДИТЕ СВОЙ ТОКЕН', parse_mode='html')

faker = Faker() 

# объект клавиаутры
card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)

card_type_keybaord.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)

card_type_keybaord.row(
    types.KeyboardButton(text='Maestro'),
    types.KeyboardButton(text='JCB'),
)


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # 
    photo = open('quokka.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(
        chat_id=message.chat.id, 
        text=f'Привет {message.from_user.first_name}! Я квокка QA и я помогу тебе сгенерировать номер тестовой банковской карты 🤗 \nВыбери тип карты:', 
        reply_markup=card_type_keybaord,
    )

 
@bot.message_handler(commands=['help'])
def help_command_handler(message):
    photo = open('1.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    text = 'Привет! Я могу сгенерировать номер тестовой банковской карты 😉. Просто нажми /start'
    bot.send_message(message.chat.id, text, parse_mode='html')
       


@bot.message_handler()
def message_handler(message: types.Message):
    '
    if message.text == 'VISA':
        card_type = 'visa'
    elif message.text == 'Mastercard':
        card_type = 'mastercard'
    elif message.text == 'Maestro':
        card_type = 'maestro'
    elif message.text == 'JCB':
        card_type = 'jcb'
    elif message.text == "Привет":
       bot.send_message(message.chat.id, 'И тебе привет! Если тебе нужен номер тестовой банковской карты, нажми /start', parse_mode='html')
    elif message.text == "Привет!":
       bot.send_message(message.chat.id, 'И тебе привет! Если тебе нужен номер тестовой банковской карты, нажми /start', parse_mode='html')
    elif message.text == "привет":
       bot.send_message(message.chat.id, 'И тебе привет! Если тебе нужен номер тестовой банковской карты, нажми /start', parse_mode='html')               
    else:
        
        
        bot.send_message(
            chat_id=message.chat.id,
            text='Что-то пошло не так 😱 Нажми /start',
        )
        return

  
    card_number = faker.credit_card_number(card_type)
  
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Тестовая карта {card_type}:\n<code>{card_number}</code>'
    )


def main():
    
    bot.infinity_polling()


if __name__ == '__main__':
    main()
