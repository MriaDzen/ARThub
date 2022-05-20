import string
import telebot
from telebot import types
from config import token
import sqlite3
from Db import get_All_Arts_Artist,get_All_Artist, get_All_Artist_Name, get_Arts_Artist, get_All_Events, Count_Arts_of_Event, makePIC_Artist, get_Arts_OfEvent,get_Pic_of_Arts_OfEvent, User_Poisk, Order_db,get_Artist, User_db, get_Price_ofArt
from yoomoney import Quickpay
from pay import ConnectWith

enter=1
bot = telebot.TeleBot(token)
x=1 # Номер артиста
y=1# Номер картины
z=1# Номер события
num=0 # Название картины для записи в покупках
step_of_reg=0
name_ART='' # Название картины



@bot.message_handler(commands=["start"])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("О нас")
    item2 = types.KeyboardButton("Купить/Посмотреть картины")
    item3 = types.KeyboardButton("История покупок")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, 'Привет', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global enter

    if enter==1:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        if (User_Poisk(us_name)):
            connection = sqlite3.connect('ARThub.bd')
            cursor = connection.cursor()
            user = [(us_id, us_name)]
            cursor.executemany("INSERT INTO Users VALUES(?,?);",user)
            connection.commit()
            enter=2

    global x,y,z,num, step_of_reg, name_ART

    if message.text == '<-' and  x>1 and x<8:
        x=x-1
        bot.send_photo(message.chat.id, makePIC_Artist(1,x))
        bot.send_message(message.chat.id, get_All_Artist(x))
    elif message.text == '->' and x>0 and x<7:
        x=x+1
        bot.send_photo(message.chat.id, makePIC_Artist(1,x))
        bot.send_message(message.chat.id, get_All_Artist(x))
    elif message.text == '->' and x>6:
        x=1
        bot.send_photo(message.chat.id, makePIC_Artist(1,x))
        bot.send_message(message.chat.id, get_All_Artist(x))
    elif message.text == '<-' and x==1:
        x=7
        bot.send_photo(message.chat.id, makePIC_Artist(1,x))
        bot.send_message(message.chat.id, get_All_Artist(x))

    if message.text == '<---' and (y==2 or y==1):
        y = y - 1
        imgArtist = get_Arts_Artist(get_All_Artist_Name(x),y) + ".jpg"
        img = open(imgArtist, 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, get_All_Arts_Artist(get_All_Artist_Name(x), y))
    elif message.text == '<---' and y==0:
        y=2
        imgArtist = get_Arts_Artist(get_All_Artist_Name(x), y) + ".jpg"
        img = open(imgArtist, 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, get_All_Arts_Artist(get_All_Artist_Name(x), y))
    elif message.text == '--->' and (y>-1 and y<2):
        y=y+1
        imgArtist = get_Arts_Artist(get_All_Artist_Name(x), y) + ".jpg"
        img = open(imgArtist, 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, get_All_Arts_Artist(get_All_Artist_Name(x), y))
    elif message.text == '--->' and y==2:
        y=0
        imgArtist = get_Arts_Artist(get_All_Artist_Name(x), y) + ".jpg"
        img = open(imgArtist, 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, get_All_Arts_Artist(get_All_Artist_Name(x), y))

    if message.text == '<--' and (z==3 or z==2):
        z = z - 1
        bot.send_message(message.chat.id, get_All_Events(z))
    elif message.text == '<--' and z==1:
        z=3
        bot.send_message(message.chat.id, get_All_Events(z))
    elif message.text == '-->' and (z==2 or z==1):
        z=z+1
        bot.send_message(message.chat.id, get_All_Events(z))
    elif message.text == '-->' and z==3:
        z=1
        bot.send_message(message.chat.id, get_All_Events(z))

    m=int(''.join(map(str,Count_Arts_of_Event(z)[0])))

    if message.text == '<----' and (num>1 and num<m):
        num = num - 1
        bot.send_photo(message.chat.id, get_Pic_of_Arts_OfEvent(z,num))
        bot.send_message(message.chat.id, get_Arts_OfEvent(z,num))

    elif message.text == '<----' and num == 0:
        num = m-1
        bot.send_photo(message.chat.id, get_Pic_of_Arts_OfEvent(z, num))
        bot.send_message(message.chat.id, get_Arts_OfEvent(z,num))

    elif message.text == '---->' and (num>-1 and num<m-1):
        num = num + 1
        bot.send_photo(message.chat.id, get_Pic_of_Arts_OfEvent(z, num))
        bot.send_message(message.chat.id, get_Arts_OfEvent(z,num))

    elif message.text == '---->' and num==m-1:
        num = 0
        bot.send_photo(message.chat.id, get_Pic_of_Arts_OfEvent(z, num))
        bot.send_message(message.chat.id, get_Arts_OfEvent(z,num))


    if message.text == 'О нас':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)
        img = open('АРТхаб.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, 'Мы творческое пространство. Здесь ты сможешь: посмотреть и купить картины современных деятелей искусства или их копии. \n\nПодписывайся на наш канал в телеграме, чтоб узнать о поступлении и будущих мероприятиях \n\nhttps://t.me/+ImmGlCXUcaYwOWJi', reply_markup=markup)

    if message.text == 'Купить/Посмотреть картины' or message.text =='Вернуться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        item2 = types.KeyboardButton("Последние выставки")
        item3 = types.KeyboardButton("Популярные авторы")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)

    if message.text == 'Последние выставки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton(text="<--")
        item3 = types.KeyboardButton(text="К картинам в выставке")
        item4 = types.KeyboardButton(text="-->")
        item5 = types.KeyboardButton(text="Вернуться")
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(message.chat.id, get_All_Events(z), reply_markup=markup)

    if message.text == 'К картинам в выставке':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton(text="<----")
        item3 = types.KeyboardButton(text="Купить")
        item4 = types.KeyboardButton(text="---->")
        item5 = types.KeyboardButton(text="Вернуться")
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_photo(message.chat.id, get_Pic_of_Arts_OfEvent(z, num))
        bot.send_message(message.chat.id, get_Arts_OfEvent(z,num), reply_markup=markup)

    if message.text == 'Популярные авторы' or message.text == 'Обратно':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton(text="<-")
        item3 = types.KeyboardButton(text="К картинам этого автора")
        item4 = types.KeyboardButton(text="->")
        item5 = types.KeyboardButton(text="Вернуться")
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_photo(message.chat.id, makePIC_Artist(1,x))
        bot.send_message(message.chat.id, get_All_Artist(x), reply_markup=markup)

    if message.text == 'К картинам этого автора':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton(text="<---")
        item3 = types.KeyboardButton(text="Обратно")
        item4 = types.KeyboardButton(text="--->")
        item5 = types.KeyboardButton(text="Купить")
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        imgArtist = get_Arts_Artist(get_All_Artist_Name(x), y) + ".jpg"
        img = open(imgArtist, 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, get_All_Arts_Artist(get_All_Artist_Name(x),y), reply_markup=markup)

    if message.text == 'Глеб Скубачевский' or message.text == 'Ренат волигамся' or message.text == 'Василий Cлонов' or message.text == 'Дмитрий Окружнов и Мария Шарова' or message.text == 'Глеб Скубачевский' or message.text == 'Павел Полянски' or message.text == 'Блинов Михаил' or message.text == 'Дамир Муратов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)
        bot.send_photo(message.chat.id, makePIC_Artist(2, message.text))
        bot.send_message(message.chat.id, get_Artist(message.text), reply_markup=markup)

    if message.text == 'История покупок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)
        bot.send_message(message.chat.id, 'У вас нет покупок!:(', reply_markup=markup)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("О нас")
        item2 = types.KeyboardButton("Купить/Посмотреть картины")
        item3 = types.KeyboardButton("История покупок")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)

    if message.text == 'Купить':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Назад")
        markup.add(item2)
        step_of_reg=1
        bot.send_message(message.chat.id, 'Чтобы оформить заказ запишите свои данные в следущем сообщении через запятую. \n\n ФИО, адрес проживания, номер телефона, название картины\n\nНапример:Дзеник Мария Дмитриевна, Россия город Набережные Челны улица 40 лет Победы дом 53Б, 89600870650, Большая половина', reply_markup=markup)

    if message.text == 'Оплата':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)
        ConnectWith()
        Getsum=get_Price_ofArt(name_ART)
        quickpay = Quickpay(
            receiver="410014340604062",
            quickpay_form="shop",
            targets="Sponsor this project",
            paymentType="SB",
            sum=Getsum,
        )
        bot.send_message(message.chat.id, quickpay.base_url, reply_markup=markup)


    elif step_of_reg==1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Оплата")
        item2 = types.KeyboardButton("Назад")
        markup.add(item1)
        markup.add(item2)
        connection = sqlite3.connect('ARThub.bd')
        cursor = connection.cursor()
        data = message.text.split(',')
        order = [(us_id, data[0], data[1], data[2], data[3])]
        name_ART=data[3]
        cursor.executemany("INSERT INTO OrderR (User_id, User_FIO, Adres, User_Phone, ART_name) VALUES(?,?,?,?,?);", order)
        connection.commit()
        step_of_reg == 0
        bot.send_message(message.chat.id,'Ваши данные успешно внесены в базу, перейдите к оплате, чтобы мы смогли отправить вам картину.', reply_markup=markup)



bot.infinity_polling()
connection = sqlite3.connect('ARThub.bd')
cursor = connection.cursor()



