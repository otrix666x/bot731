import telebot
from telebot import types
import sqlite3
import time
import config, keyboard
import random
import requests
from pyqiwip2p import QiwiP2P
from pyqiwip2p.types import QiwiCustomer, QiwiDatetime
p2p = QiwiP2P(auth_key=config.qiwi_key)

bot = telebot.TeleBot(config.token)


ref_link = 'https://telegram.me/{}?start={}'

@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('bot.db')
    q = connect.cursor()
    q.execute(""" CREATE TABLE IF NOT EXISTS info(
        id TEXT, balance TEXT
    ) """)
    q.execute(""" CREATE TABLE IF NOT EXISTS check_pay(
        id TEXT, bill TEXT
    ) """)
    connect.commit()
    userid = message.chat.id

    row = q.execute("SELECT * FROM INFO where id is " + str(userid)).fetchone()
    if row is None:
        bal = 0
        q.execute("INSERT INTO info(id, balance) VALUES ('%s', '%s')"%(userid, bal))
        connect.commit()
    bot.send_message(message.chat.id,"Приветствую дорогой друг, выбери страну 🌍",reply_markup=keyboard.choose_county)

@bot.message_handler(commands=['admin'])
def adm(message):
    if message.chat.id == config.admin or message.chat.id == config.admin1:
        bot.send_message(message.chat.id, "👋", reply_markup=keyboard.choose_county)
        bot.send_message(message.chat.id, "Привет админ", reply_markup=keyboard.admin_but)

    
    else:
        bot.send_message(message.chat.id, "для вас эта команда не доступна")


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "🔈Сделать рассылку🔈":
        send = bot.send_message(message.chat.id, "Введите текст для рассылки")
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.register_next_step_handler(send, spam)
    if message.text == "💥кол-во пользователей💥":
        connect = sqlite3.connect('bot.db')
        q = connect.cursor()
        all_user_count = q.execute(f'SELECT COUNT(id) FROM info').fetchone()[0]
        bot.send_message(message.chat.id, f"Количество пользователей {all_user_count}")
    
    if message.text == "⚡️Сменить баланс⚡️":
        send = bot.send_message(message.chat.id, "Введите айди пользователя")
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.register_next_step_handler(send, next_step)


@bot.callback_query_handler(func=lambda call: True)

def answer(call):
    if call.data == "ukr":
        visit = random.randint(3000,9000)
        sell = random.randint(1000,4000)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🤗Добро пожаловать в DORC🚪 Marketplace\n\n"\
            f"🧑‍💻Ваш id: {call.message.chat.id}\n\n"\
                "За последние сутки:\n"\
                    f"👫нас посетило: {visit} покупателей\n"\
                        f"🛒товаров продано: {sell}", reply_markup=keyboard.main)



    if call.data == "rus":
        visit = random.randint(3000,9000)
        sell = random.randint(1000,4000)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🤗Добро пожаловать в DORC🚪 Marketplace\n\n"\
            f"🧑‍💻Ваш id: {call.message.chat.id}\n\n"\
                "За последние сутки:\n"\
                    f"👫нас посетило: {visit} покупателей\n"\
                        f"🛒товаров продано: {sell}", reply_markup=keyboard.main_ru)
    

    if call.data == "prof_ukr":
        link = ref_link.format(config.bot_name, call.message.chat.id)
        connect = sqlite3.connect('bot.db')
        q = connect.cursor()
        bal = q.execute(f"SELECT balance FROM info where id = '{call.message.chat.id}'").fetchone()[0]
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = f"{call.message.chat.first_name}, это ваш кабинет👨‍💻\n\n"\
            f"💰Ваш баланс: {bal}грн\n"\
                f"📦Количество покупок: 0\n\n"\
                    f"🔗Ваша реферальная ссылка {link}", reply_markup=keyboard.prof_ukrbut)
    
    if call.data == "prof_ru":
        link = ref_link.format(config.bot_name, call.message.chat.id)
        connect = sqlite3.connect('bot.db')
        q = connect.cursor()
        bal = q.execute(f"SELECT balance FROM info where id = '{call.message.chat.id}'").fetchone()[0]
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = f"{call.message.chat.first_name}, это ваш кабинет👨‍💻\n\n"\
            f"💰Ваш баланс: {bal}руб\n"\
                f"📦Количество покупок: 0\n\n"\
                    f"🔗Ваша реферальная ссылка {link}", reply_markup=keyboard.prof_rubut)
    
    if call.data == "Пополнить баланс":
        bot.send_message(call.message.chat.id, "Выбирите тип пополнения", reply_markup=keyboard.add_balance)

    if call.data == "Пополнить_ukr":
        bot.send_message(call.message.chat.id, "Выбирите тип пополнения", reply_markup=keyboard.add_balance_ukr)
    
    if call.data == "app":
        bot.send_message(call.message.chat.id, "Выбирите тип пополнения", reply_markup=keyboard.add_balance)
    


    

    

    
    if call.data == "qiwi":
        send = bot.send_message(call.message.chat.id, "Введите сумму пополнения")
        bot.clear_step_handler_by_chat_id(call.message.chat.id)
        bot.register_next_step_handler(send, app_balance)
    
    if call.data == "card":
        send = bot.send_message(call.message.chat.id, "Введите сумму пополнения")
        bot.clear_step_handler_by_chat_id(call.message.chat.id)
        bot.register_next_step_handler(send, app_balance)
    
    if call.data == "btc":
        send = bot.send_message(call.message.chat.id, "Введите сумму пополнения, минимальная сумма 1000р")
        bot.clear_step_handler_by_chat_id(call.message.chat.id)
        bot.register_next_step_handler(send, app_btc)
    
    if call.data == "job":
        key1 = types.InlineKeyboardMarkup()
        key1.row(types.InlineKeyboardButton("💰Получить работу", url=f"{config.operator}"))
        key1.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        bot.send_photo(call.message.chat.id, "https://i.imgur.com/MtMzGOH.jpg", caption="В дружный коллектив требуются:\n\n"\
            "Желаете зарабатывать, реализовывать свои амбиции и готовы подойти к работе с полной ответственностью?\n\n"\
                "Если ответ - ДА, то тебе точно к нам!\n\n"\
                    "📊 Готовы предложить заработок от 20 000 рублей в неделю! Самому ответственному трудоголику карьерный рост.\n\n"\
                        "🔒 Проведем полный инструктаж по анонимной и безопасной работе в данной сфере.\n\n"\
                            "Скорее пиши, ждем тебя! ✊", reply_markup=key1)
    if call.data == "chat":
        bot.send_photo(call.message.chat.id,"https://i.imgur.com/pIgp1lg.jpg", caption="Преимущества нашего чата:\n"\
            "- Только клиенты\n"\
                "- Розыгрыши, акции\n"\
                    "- Скидки\n"\
                        "- Рулетки\n"\
                            "- Эксклюзивная поддержка клиентов 24\7\n"\
                                "- Никакого спама/рекламы\n\n"\
                                    "⚠️ Доступ в Закрытый Чат имеют только Клиенты нашего Магазина совершившие 1 и более покупки (ссылка выдается вместе с заказом)", reply_markup=keyboard.delete)

    if call.data == "inf":
        key2 = types.InlineKeyboardMarkup()
        key2.row(types.InlineKeyboardButton("🗣Оставить комментарий", url="https://t.me/DORC4ShopNews"))
        key2.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        bot.send_photo(call.message.chat.id,"https://i.imgur.com/Ae7zQby.jpg", caption="🔥 Понравился товар? 🔥\n\n"\
            "Есть предложение как улучшить наш сервис?\n\n"\
                "✊ Воспользуйтесь кнопкой ниже, чтобы оставить комментарий о нас.\n\n"\
                    "📜 Отзывы о нашей работе можно посмотреть в официальном канале.\n\n"\
                        "❗️ Дамы и господа, дабы соблюдать анонимность, закрывайте профиль перед написанием отзыва.", reply_markup=key2)
    if call.data == "delete":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    if call.data == "city_urk":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш город", reply_markup=keyboard.city_urk)
    
    if call.data == "Київ":
        
        city = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.kiev_rayon)

    if call.data == "Дніпро":
        city = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.depr_rayon)
    
    if call.data == "Харків":
        
        city = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.har_rayon)

    if call.data == "Одеса":
      
        city = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.odessa_rayon)

    if call.data == "Львів":
       
        city = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.lviv_rayon)

    if call.data == "Кропивницький":
        
        city = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.kir_rayon)

    if call.data == "Миколаїв":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.nik_rayon)
    
    if call.data == "Запоріжжя":
       
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.zapor_rayon)
    
    if call.data == "back2":
        
       
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш город", reply_markup=keyboard.city_urk)

    if call.data == "back1":
       
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Вы находитесь в главном меню", reply_markup=keyboard.main)
    
        
    if call.data == "Голосіївський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Дарницкий":
       
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Дніпровський":
       
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Оболонський":
     
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Подольский":
       
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Солом'янський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Шевченківський":
       
        rayon = call.data
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Індустріальний":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Центральний":
       
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Самарський":
       
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Київський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Московський":
       
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Малиновський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Приморський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Суворовський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Галицький":
       
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Личаківський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Сихівський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Кіровський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Олександрівський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Комунарський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    if call.data == "Дніпровський":
        
        rayon = call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выбирите товар из списка", reply_markup=keyboard.tovar_list)
    
    if call.data == "back3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Вы находитесь в главном меню", reply_markup=keyboard.main_ru)
    
    if call.data == "city_ru":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш город", reply_markup=keyboard.ru_city)
    
    if call.data == "Москва":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.msc_rayon)
    
    if call.data == "Санкт-Петербург":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.spb_rayon)

    if call.data == "Екатеринбург":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.ekb_rayon)

    if call.data == "Барнаул":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.brnl_rayon)

    if call.data == "Томск":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.tomsk_rayon)

    if call.data == "Тюмень":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.tumen_rayon)

    
    if call.data == "Нижний Новгород":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.nijniy_rayon)

    if call.data == "Самара":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.samara_rayon)

    if call.data == "Омск":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.omsk_rayon)

    if call.data == "Саратов":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.sarat_rayon)

    if call.data == "Краснодар":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.krsndr_rayon)

    if call.data == "Красноярск":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.krsn_rayon)

    if call.data == "Воронеж":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.voron_rayon)

    if call.data == "Волгоград":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.volg_rayon)

    if call.data == "Уфа":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.ufa_rayon)

    if call.data == "Ростов-на-Дону":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.rostov_rayon)

    if call.data == "Иркутск":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.irk_rayon)

    if call.data == "Махачкала":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш район", reply_markup=keyboard.mah_rayon)
    
    if call.data == "back4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите ваш город", reply_markup=keyboard.ru_city)
    
    if call.data == "САО":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ЦАО":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ЮАО":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ЮВАО":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ЗАО":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Василеостровский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Выборгский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Калининский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Кировский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Курортный":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Московский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Приморский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Фрунзенский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Центральный":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Железнодорожный":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Октябрьский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Ордожиникидзевский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Чкаловский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Индустриальный":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Ленинский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Советский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Восточный":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Калининский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Автозаводский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Канавинский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Московский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Нижегородский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Приокский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Самарский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Промышленный":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Красноглинский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Заводской":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Волжский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ЖМР":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "СМР":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ЗИП":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "РИП":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ШМР":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ЮМР":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "КМР":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ПМР":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ГМР":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "ЧМР":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Свердловский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Коминтерновский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Левобережный":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Ворошиловский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Дзержинский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Тракторозаводский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Демский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Калининский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    if call.data == "Первомайский":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Выберите товар", reply_markup=keyboard.rutovar_list)
    
    arr = call.data.split("_")
    if arr[0] == "Кристалы MDMA (1гр)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)
        bot.send_message(call.message.chat.id, f"❕ Вы выбрали: Кристалы MDMA (1гр) | {arr[1]}грн\n\n"\
            "Шедевр эйфорической алхимии. Настоящая находка для ценителя и неутомимого покорителя вершин наслаждения.\n\n"\
                "Магическое сплетение молекул этого продукта наполняет душу радостью и заставляет сердца биться быстрее. Перед Вами МДМА высшей категории, синтезированный мастерами своего дела из самых качественных компонентов. Вы получите радость и тепло даже от небольшой крупинки. Кристаллы от Durman поражают своей многогранностью и постепенно раскрывается все новыми красками на протяжении всего сеанса.\n\n"\
                    "Вы чувствуете интенсивную неземную эйфорию и непреодолимое желание двигаться. Абсолютный экстаз и наслаждение.\n\n"\
                        "Кристаллы очень сильные, поэтому будьте внимательны при расчёте своей нормы. 1.2 - 1.5мг МДМА на 1кг Вашей массы\n\n"\
                            f"💲 Цена: {arr[1]} грн\n"\
                                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "💎 Амф 💎 1(г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)
        bot.send_message(call.message.chat.id, f"❕ Вы выбрали: {arr[0]} | {arr[1]}грн\n\n"\
            f"💲 Цена: {arr[1]} грн\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
   
    if arr[0] == "☮️ Шишки белая вдова ☮️ 1(г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}грн\n\n"\
            f"💲 Цена: {arr[1]} грн\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "☮️ Шишки белая вдова ☮️ 2(г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}грн\n\n"\
            f"💲 Цена: {arr[1]} грн\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "☮️ Шишки чёрная вдова ☮️ 2(г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}грн\n\n"\
            f"💲 Цена: {arr[1]} грн\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "⚡️ Альфа соль чёрная ⚡️ (1гр)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}грн\n\n"\
            f"💲 Цена: {arr[1]} грн\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "🍯 Метадон 🍯 (1гр)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}грн\n\n"\
            f"💲 Цена: {arr[1]} грн\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "☮️ Гаш ☮️ (1гр)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}грн\n\n"\
            "🗿Вкус и аромат нашего гашиша впечатлит даже самого продвинутого ценителя от мира старокуров . Сбаланситованный эффект подарит приятную релаксацию мышцам, чувство эйфории и подъем настроения. Мысли станут лёгкими.\n\n"\
                "🗿Цвет:Тёмно-коричневый\n\n"\
                    "🗿Плотный и мощный накур!!! Вы будете переполнены идеями и вдохновением.\n\n"\
                        f"💲 Цена: {arr[1]} грн\n"\
                            f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "⚡️ Альфа соль белая ⚡️ (1гр)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}грн\n\n"\
            f"💲 Цена: {arr[1]} грн\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    
    if arr[0] == "🍚 Меф кристаллы 🍚 (1гр)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}грн\n\n"\
            f"😻Меф -Эйфоретик . Вызывает эйфорию и сексуальное возбуждение. Является аналогом/альтернативой КОКАИНА и ЭКСТАЗИ\n\n😻ЭФФЕКТЫ :\nРезкое повышение настроения и эйфории. Возврастает сексуальное возбуждение, влечение/стимуляция. Повышает чрезмерную речевую и двигательную активность. Повышает звуковосприятие , мир становится красочнее.Вначале наступает эйфорическое состояние , мир становится ярче хочется всех любить , повышается сексуальное влечение , яркие оргазмы и незабываемые ощущения это неизменная составляющая этого продукта (виагра женская и мужская нервно курит в углу) 1г на двоих и вам обеспечены такие ощущения о которых будет хотеться рассказать всему миру и обнять весь земной шар\n\n💲 Цена: {arr[1]} грн\n🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "💎 Скорость a-PVP 💎 0.5(г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "💎 Скорость a-PVP 💎 1(г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    if arr[0] == "☮️ Гашиш [Афганский] ☮️ 1(г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            "🗿Вкус и аромат нашего гашиша впечатлит даже самого продвинутого ценителя от мира старокуров . Сбаланситованный эффект подарит приятную релаксацию мышцам, чувство эйфории и подъем настроения. Мысли станут лёгкими.\n\n"\
                "🗿Цвет:Тёмно-коричневый\n\n"\
                    "🗿Плотный и мощный накур!!! Вы будете переполнены идеями и вдохновением.\n\n"\
                        f"💲 Цена: {arr[1]} руб\n"\
                            f"🏴 Количество товара: {сolvo}", reply_markup=key)

    if arr[0] == "☮️ Гашиш VHQ Lemon ☮️ 2(г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            "🗿Вкус и аромат нашего гашиша впечатлит даже самого продвинутого ценителя от мира старокуров . Сбаланситованный эффект подарит приятную релаксацию мышцам, чувство эйфории и подъем настроения. Мысли станут лёгкими.\n\n"\
                "🗿Цвет:Тёмно-коричневый\n\n"\
                    "🗿Плотный и мощный накур!!! Вы будете переполнены идеями и вдохновением.\n\n"\
                        f"💲 Цена: {arr[1]} руб\n"\
                            f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "☮️ Гашиш VHQ Black Mamba☮️ 2(г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            "🗿Вкус и аромат нашего гашиша впечатлит даже самого продвинутого ценителя от мира старокуров . Сбаланситованный эффект подарит приятную релаксацию мышцам, чувство эйфории и подъем настроения. Мысли станут лёгкими.\n\n"\
                "🗿Цвет:Тёмно-коричневый\n\n"\
                    "🗿Плотный и мощный накур!!! Вы будете переполнены идеями и вдохновением.\n\n"\
                        f"💲 Цена: {arr[1]} руб\n"\
                            f"🏴 Количество товара: {сolvo}", reply_markup=key)

    if arr[0] == "☮️ Гашиш VHQ Paris☮️ (2г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            "🗿Вкус и аромат нашего гашиша впечатлит даже самого продвинутого ценителя от мира старокуров . Сбаланситованный эффект подарит приятную релаксацию мышцам, чувство эйфории и подъем настроения. Мысли станут лёгкими.\n\n"\
                "🗿Цвет:Тёмно-коричневый\n\n"\
                    "🗿Плотный и мощный накур!!! Вы будете переполнены идеями и вдохновением.\n\n"\
                        f"💲 Цена: {arr[1]} руб\n"\
                            f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "☮️ White Widow ☮️ (1г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "☮️ Бошки убойные LSD ☮️ (2г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "☮️ AK-47 ☮️ (1г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "⚡️Амфетамин White Power ⚡️ (1г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "⚡️ Амфетамин White Luxury ⚡️ (1г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)

    if arr[0] == "⚡️ Амфетамин White Luxury ⚡️ (2г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "❤️ Мефедрон [Мука] ❤️ (1г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            "😻Меф -Эйфоретик . Вызывает эйфорию и сексуальное возбуждение. Является аналогом/альтернативой КОКАИНА и ЭКСТАЗИ\n\n"\
                "😻ЭФФЕКТЫ :\nРезкое повышение настроения и эйфории. Возврастает сексуальное возбуждение, влечение/стимуляция. Повышает чрезмерную речевую и двигательную активность. Повышает звуковосприятие , мир становится красочнее.Вначале наступает эйфорическое состояние , мир становится ярче хочется всех любить , повышается сексуальное влечение , яркие оргазмы и незабываемые ощущения это неизменная составляющая этого продукта (виагра женская и мужская нервно курит в углу) 1г на двоих и вам обеспечены такие ощущения о которых будет хотеться рассказать всему миру и обнять весь земной шар\n\n"\
                    f"💲 Цена: {arr[1]} руб\n"\
                        f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "❤️ [LUX!!!] Мефедрон ❤️ (1г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            "😻Меф -Эйфоретик . Вызывает эйфорию и сексуальное возбуждение. Является аналогом/альтернативой КОКАИНА и ЭКСТАЗИ\n\n"\
                "😻ЭФФЕКТЫ :\nРезкое повышение настроения и эйфории. Возврастает сексуальное возбуждение, влечение/стимуляция. Повышает чрезмерную речевую и двигательную активность. Повышает звуковосприятие , мир становится красочнее.Вначале наступает эйфорическое состояние , мир становится ярче хочется всех любить , повышается сексуальное влечение , яркие оргазмы и незабываемые ощущения это неизменная составляющая этого продукта (виагра женская и мужская нервно курит в углу) 1г на двоих и вам обеспечены такие ощущения о которых будет хотеться рассказать всему миру и обнять весь земной шар\n\n"\
                    f"💲 Цена: {arr[1]} руб\n"\
                        f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "♦️ МДМА (1гр)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)


        bot.send_message(call.message.chat.id, f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            "Шедевр эйфорической алхимии. Настоящая находка для ценителя и неутомимого покорителя вершин наслаждения.\n\n"\
                "Магическое сплетение молекул этого продукта наполняет душу радостью и заставляет сердца биться быстрее. Перед Вами МДМА высшей категории, синтезированный мастерами своего дела из самых качественных компонентов. Вы получите радость и тепло даже от небольшой крупинки. Кристаллы от Durman поражают своей многогранностью и постепенно раскрывается все новыми красками на протяжении всего сеанса.\n\n"\
                    "Вы чувствуете интенсивную неземную эйфорию и непреодолимое желание двигаться. Абсолютный экстаз и наслаждение.\n\n"\
                        "Кристаллы очень сильные, поэтому будьте внимательны при расчёте своей нормы. 1.2 - 1.5мг МДМА на 1кг Вашей массы\n\n"\
                            f"💲 Цена: {arr[1]} руб\n"\
                                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "♦️ МДМА (2гр)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id, f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            "Шедевр эйфорической алхимии. Настоящая находка для ценителя и неутомимого покорителя вершин наслаждения.\n\n"\
                "Магическое сплетение молекул этого продукта наполняет душу радостью и заставляет сердца биться быстрее. Перед Вами МДМА высшей категории, синтезированный мастерами своего дела из самых качественных компонентов. Вы получите радость и тепло даже от небольшой крупинки. Кристаллы от Durman поражают своей многогранностью и постепенно раскрывается все новыми красками на протяжении всего сеанса.\n\n"\
                    "Вы чувствуете интенсивную неземную эйфорию и непреодолимое желание двигаться. Абсолютный экстаз и наслаждение.\n\n"\
                        "Кристаллы очень сильные, поэтому будьте внимательны при расчёте своей нормы. 1.2 - 1.5мг МДМА на 1кг Вашей массы\n\n"\
                            f"💲 Цена: {arr[1]} руб\n"\
                                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "🍯 Метадон 🍯 (0.5г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "🍯 Метадон 🍯 (1г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "🍚 Героин 🍚 (1г":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "⚡️ LUXURY COCAINE [AUDI] ⚡️ (0.5г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "⚡️ LUXURY COCAINE [AUDI] ⚡️ (1г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    
    if arr[0] == "★ Кокаин 24 Colombia ★ (0.5г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "★ VHQ Кокаин DTJ Colombia★":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "🎇LSD: Марки 220 - 250 мкг🎇 (5шт)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "❄️Метамфетамин HQ(Крис)❄️ (1г)":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("💰Оплатить", callback_data="pay1_{}".format(arr[1])))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        сolvo = random.randint(5,15)

        bot.send_message(call.message.chat.id,f"❕ Вы выбрали: {arr[0]} | {arr[1]}руб\n\n"\
            f"💲 Цена: {arr[1]} руб\n"\
                f"🏴 Количество товара: {сolvo}", reply_markup=key)
    
    if arr[0] == "pay":
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("👨‍💻Оператор продаж", url = f"{config.operator}"))
        key.row(types.InlineKeyboardButton("❌Закрыть", callback_data="delete"))
        
        bot.send_message(call.message.chat.id, "На данный момент автоматическая оплата не возможна\n"\
            "Покупка производиться через оператора", reply_markup=key)
    
    if arr[0] == "pay1":
        connect = sqlite3.connect('bot.db')
        q = connect.cursor()
        balik = q.execute(f"SELECT balance from info where id = '{call.message.chat.id}'").fetchone()[0]
        balik = int(balik)
        if balik == 0 or balik < int(arr[1]):
            bot.send_message(call.message.chat.id, "НЕДОСТАТОЧНО ДЕНЕГ\n\nВАМ НУЖНО ПОПОЛНИТЬ БАЛАНС", reply_markup=keyboard.nomoney)
        else:
            new_balance = int(balik) - int(arr[1])
            q.execute(f"update info set balance = '{new_balance}' where id = '{call.message.chat.id}'")
            connect.commit()

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Покупка прошла успешно✅\n\n"\
                "ВАШ АДРЕС: 💠 2021-05-08 15:33:41 | Р‘РµСЂРµР·РѕРІСЃРєРёР№ РїР°СЂРє, Р·Р° С„РѕС‚Рѕ Рє РѕРїРµСЂР°С‚РѕСЂСѓ")
    
    if arr[0] == "check":
        summ = int(arr[1])
        connect = sqlite3.connect('bot.db')
        q = connect.cursor()
        info = q.execute(f"SELECT bill FROM check_pay where id = '{call.message.chat.id}'").fetchone()[0]
        stat = p2p.check(bill_id=info).status
        if stat == "PAID":
            q.execute(f"DELETE FROM check_pay where id = '{call.message.chat.id}'")
            q.execute(f"update info set balance = balance + '{summ}' where id = '{call.message.chat.id}'")
            connect.commit()
            bot.send_message(call.message.chat.id, f"Ваш баланс пополнено на {summ}₽")
        else:
            bot.send_message(call.message.chat.id, f"Платеж не найден\n"\
                "Повторите проверку через несколько секунд")
    if call.data == "cancel":
        connect = sqlite3.connect('bot.db')
        q = connect.cursor()
        q.execute(f"DELETE FROM check_pay where id = '{call.message.chat.id}'")
        connect.commit()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "❌Платёж отменен")
        



def app_btc(message):
    summ = message.text
    if int(summ) >= 1000:
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("Возникли трудности⁉️", url=f"{config.operator}"))
        summ_rub = int(message.text)
        req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
        response = req.json()
        sell_price = int(response["btc_usd"]["sell"])
        sell_price_rub = sell_price * config.dollar_rate
        sum_btc = summ_rub / sell_price_rub
        sum_btc = float('{:.8f}'.format(sum_btc))
        bot.send_message(message.chat.id, "Информация об оплате\n"\
                    f"🔄Курс конвертации: {sell_price_rub} руб\n"\
                        f"🔄BTC адрес: {config.btc_adress}\n\n"\
                            f"Переведите на указанный адрес {sum_btc} btc.\nПосле 1 подтверждения транзакции, деньги поступят вам на баланс", reply_markup=key)

    
def next_step(message):
    try:
        userid = str(message.text)
        send = bot.send_message(message.chat.id, "Введите сумму для баланса пользователя")
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.register_next_step_handler(send, reset_bal, userid)
    except Exception as e:
        print(e)

def reset_bal(message, userid):
    userid = str(userid)
    balance = message.text
    connect = sqlite3.connect('bot.db')
    q = connect.cursor()
    q.execute(f"update info set balance = '{balance}' where id = '{userid}'")
    connect.commit()
    bot.send_message(message.chat.id, f"Баланс для {userid} был успешно изменен на сумму {balance}")



def app_balance(message):
    summ = message.text 
    if summ.isdigit():
        userid = message.chat.id
        new_bill = p2p.bill(amount=summ, lifetime=15)
        url = new_bill.pay_url
        info = new_bill.bill_id
        connect = sqlite3.connect('bot.db')
        q = connect.cursor()
        key = types.InlineKeyboardMarkup()
        key.row(types.InlineKeyboardButton("🔎Проверить платеж", callback_data="check_{}".format(summ)), types.InlineKeyboardButton("❌Отменить платеж", callback_data="cancel"))
        row = q.execute("SELECT * FROM info where id is " + str(userid)).fetchone()
        if row is None:
            q.execute("INSERT INTO check_pay (id, bill) VALUES ('%s', '%s')"%(userid, info))
            connect.commit()
        else:
            q.execute(f"DELETE FROM info where id = '{userid}'")
            connect.commit()
            q.execute("INSERT INTO check_pay (id, bill) VALUES ('%s', '%s')"%(userid, info))
            connect.commit()
        
        bot.send_message(userid, f"Ссылка на быстрое пополнения баланса\n\n"\
            f"{url}", reply_markup=key)




def spam(message):
    try:
        connect = sqlite3.connect('bot.db')
        q = connect.cursor()
        q.execute("SELECT id FROM info")
        results = q.fetchall()
        q.close()
        bot.send_message(message.chat.id, "<b>Рассылка начнеться через 10 секунд</b>", parse_mode='html')
        time.sleep(10)
        bot.send_message(message.chat.id, "<b>Рассылка пошла...</b>", parse_mode='html')
        k = 0
        for result in results:
            try:
                bot.send_message(result[0], message.text, parse_mode='html')
            except:
                pass
            time.sleep(0.3)
            k +=1
        bot.send_message(message.chat.id, f"Рассылку получило {str(k)} человек")
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка рассылки!")



    



while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        time.sleep(10)