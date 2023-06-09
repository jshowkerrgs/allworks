import os
import telebot
import openai
import sqlite3
import threading
telegram_token = '6087135910:AAHqE9WOGITc9QOzsDm4wEzy_A-QM3pIYec'
openai.api_key = open('api_key.txt').read().strip()
bot = telebot.TeleBot(token=telegram_token)


def handle_message(message):
    conn = sqlite3.connect('data0.1.db')
    c = conn.cursor()


    # Создаем новую таблицу login_id
    c.execute(
        '''CREATE TABLE IF NOT EXISTS login_id ( 
            user_id INTEGER , 
            first_name TEXT, 
            last_name TEXT,  
            message TEXT 
            )''')

    conn.commit()
    c.execute(f"SELECT user_id FROM login_id WHERE user_id = {message.chat.id}")
    data = c.fetchone()
    user_id = [message.chat.id, message.chat.first_name, message.chat.last_name, message.text]
    c.execute("INSERT INTO login_id (user_id, first_name, last_name, message) VALUES (?, ?, ?, ?);", (user_id[0], user_id[1], user_id[2], user_id[3]))
    conn.commit()
    code = message.text



    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"##### Fix bugs in the below function\n \n### Buggy Python {code} ### Fixed Python",
        temperature=0,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["###"]
    )
    fixed_code = response.choices[0].text.strip()
    bot.reply_to(message, f"Вот готовый код😱:\n{fixed_code}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    handle_message(message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    handle_message(message)

def polling_worker():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    threading.Thread(target=polling_worker).start()
