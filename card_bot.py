# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# В google colab добавить: !pip install Faker
# для установки необходимо в файл requirements.text добавить строки
# 'PyTelegramBotApi'
# 'faker'

from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='ВВЕДИТЕ СВОЙ ТОКЕН', parse_mode='html') # создание бота

faker = Faker() # утилита для генерации номеров кредитных карт

# объект клавиаутры
card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)
# первый ряд кнопок
card_type_keybaord.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)
# второй ряд кнопок
card_type_keybaord.row(
    types.KeyboardButton(text='Maestro'),
    types.KeyboardButton(text='JCB'),
)


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    photo = open('quokka.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text=f'Привет {message.from_user.first_name}! Я квокка QA и я помогу тебе сгенерировать номер тестовой банковской карты 🤗 \nВыбери тип карты:', # текст сообщения
        reply_markup=card_type_keybaord,
    )

# обработчик команды '/help'  
@bot.message_handler(commands=['help'])
def help_command_handler(message):
    photo = open('1.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    text = 'Привет! Я могу сгенерировать номер тестовой банковской карты 😉. Просто нажми /start'
    bot.send_message(message.chat.id, text, parse_mode='html')
       

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # проверяем текст сообщения на совпадение с текстом какой либо из кнопок
    # в зависимости от типа карты присваем занчение переменной 'card_type'
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
        # если текст не совпал ни с одной из кнопок 
        # выводим ошибку
        bot.send_message(
            chat_id=message.chat.id,
            text='Что-то пошло не так 😱 Нажми /start',
        )
        return

    # получаем номер тестовой карты выбранного типа
    # card_type может принимать одно из зачений ['maestro', 'mastercard', 'visa13', 'visa16', 'visa19',
    # 'amex', 'discover', 'diners', 'jcb15', 'jcb16']
    card_number = faker.credit_card_number(card_type)
    # и выводим пользователю
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Тестовая карта {card_type}:\n<code>{card_number}</code>'
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
