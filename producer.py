import os
import asyncio
import requests
import feedparser
from dotenv import load_dotenv
from pprint import pprint
from telegram import Bot
from telegram import Update
from telegram.ext import Updater, MessageHandler, Application, CommandHandler, CallbackContext
from telegram.ext import filters  # Импорт фильтров для обработчиков сообщений
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputPeerChannel


load_dotenv()



# # URL новостной ленты
# # url = 'https://moex.com/export/news.aspx?cat=100'
# url = 'https://smart-lab.ru/allblog/'
#
# # Загрузка и разбор новостной ленты
# feed = feedparser.parse(url)
#
# # Вывод заголовков новостей из ленты
# for entry in feed.entries:
#     print(entry.title)
#
# # response = requests.get('https://swapi.dev/api/starships/9/')
# response = requests.get('https://t.me/if_market_news/72187')
# response = response.json()
# # pprint(response.text)


# def get_chat_history(update: Update, context: CallbackContext):
#     chat_id = update.message.chat_id
#     limit = 10
#
#     # Получаем обновления из чата
#     updates = context.bot.get_updates(chat_id=chat_id, limit=limit)
#
#     # Обрабатываем полученные сообщения
#     for update in updates:
#         if update.message:
#             print(f"Сообщение: {update.message.text}")
#
#
#
# def main():
#
#     # Получите токен бота от BotFather
#     bot_token = os.getenv("bot_token")
#
#     # Создайте объект бота
#     bot = Bot(token=bot_token)
#
#     # updater = Updater(bot_token, update_queue=True)
#     #
#     # # Получаем dispatcher для регистрации обработчиков
#     # dp = updater.dispatcher
#     #
#     # dp.add_handler(CommandHandler('history', get_chat_history))
#
#     # Создаем объект Application
#     application = Application.builder().token(bot_token).build()
#
#     messages = application.get_updates(chat_id="-1001540990243", limit=10)  # Получить последние 10 сообщений из канала
#
#
#
#     for message in messages:
#         print(message.text)
#
#     # # Регистрируем обработчик для команды /start
#     # application.add_handler(CommandHandler('start', start))
#
#     # Запускаем бота
#     application.run_polling()
#
#
#
# # Функция для получения сообщений из канала
# # def channel_messages(update, context):
# #     # ID публичного канала, из которого вы хотите получать сообщения
# #     channel_id = '@https://t.me/SberInvestments'  # Замените CHANNEL_ID на ID вашего канала
# #
# #     # Получите последние 10 сообщений из канала
# #     messages = bot.get_chat_history(chat_id=channel_id, limit=10)  # Получить последние 10 сообщений из канала
# #
# #     # Обработайте полученные сообщения
# #     for message in messages:
# #         print(message.text)
# #
# # # update_queue = Dispatcher.create_update_queue()
# #
# #
# # updater = Updater(bot_token, update_queue=True)
# # dispatcher = updater.dispatcher
# #
# # # Добавьте обработчик получения сообщений из канала
# # dispatcher.add_handler(MessageHandler(filters.status_update.channel_posts, channel_messages))
# #
# # updater.start_polling()
# # updater.idle()
#
#
# if __name__ == '__main__':
#     main()


# from telethon import TelegramClient

# from telethon.tl.types import InputChannel
# import time
#
# # Настройки подключения
# api_id = os.getenv("api_id")  # Ваш API ID
# api_hash = os.getenv("api_hash")  # Ваш API Hash
# phone_number = os.getenv("phone_number")  # Ваш номер телефона

#
# # Инициализация клиента
# client = TelegramClient('session_name', api_id, api_hash)
#
#
# def get_channel_messages(channel):
#     # Получаем последние сообщения
#     messages = client(GetMessagesRequest(
#         channel,
#         min_id=0,
#         max_id=0,
#         limit=3  # Количество сообщений для получения
#     ))
#     return messages.messages
#
#
# def main():
#     client.start(os.getenv("two_fa_password"))
#     # try:
#     #     client.start()
#     # except SessionPasswordNeededError:
#     #     print("Введите ваш 2FA пароль:")
#     #     two_fa_password = input()
#     #     client.start(two_fa_password)
#
#     me = client.get_me()
#     print(f"Вы вошли как: {me.first_name} {me.last_name}")
#
#     #     # Получаем сущность канала
#     #     channel = client.get_entity(channel_name)
#     #
#     #     # Бесконечный цикл чтения сообщений
#     #     last_message_id = 0
#     #
#     #     print("Получение сообщений")
#     #     messages = get_channel_messages(channel)
#     #     print(f"messages: {messages}")
#     #
#     #     # Проверяем новые сообщения
#     #     for msg in messages:
#     #         if msg.id > last_message_id:
#     #             print(f"Новое сообщение: {msg.message}")
#     #             last_message_id = msg.id
#     #
#     #     # Задержка между проверками
#     #     # time.sleep(60)
#     #
#     #     # while True:
#     #     #     messages = get_channel_messages(channel)
#     #     #
#     #     #     # Проверяем новые сообщения
#     #     #     for msg in messages:
#     #     #         if msg.id > last_message_id:
#     #     #             print(f"Новое сообщение: {msg.message}")
#     #     #             last_message_id = msg.id
#     #     #
#     #     #     # Задержка между проверками
#     #     #     time.sleep(60)
#     #
#     #     client.disconnect()
#     #
#     # except Exception as e:
#     #     print(f"Ошибка: {str(e)}")
#
# # Запуск асинхронной функции в синхронном контексте
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(main())
#
#
# if __name__ == "__main__":
#     main()

from telethon import TelegramClient
from telethon.errors import (SessionPasswordNeededError,
                             FloodWaitError, PhoneNumberBannedError)

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
phone_number = os.getenv("phone_number")
two_fa_password = os.getenv("two_fa_password")
channel_name = os.getenv("channel_username")  # Имя канала


def get_channel_messages(channel):
    # Получаем последние сообщения
    messages = client(GetMessagesRequest(
        channel,
        limit=3  # Количество сообщений для получения
    ))
    return messages.messages

async def main():
    try:
        async with TelegramClient('имя_сессии', api_id, api_hash) as client:
            try:
                # Решить проблему с двухфакторной аутентификацией
                await client.start()
            except SessionPasswordNeededError:
                print("Введите ваш 2FA пароль:")
                two_fa_password = input()
                client.start(two_fa_password)
            except FloodWaitError as e:
                print(f"Подождите {e.seconds} секунд")
            except PhoneNumberBannedError:
                print("Ваш номер телефона заблокирован в Telegram")

            channel = await client.get_entity(channel_name)
            print("Канал получен")

            # messages = await client(GetMessagesRequest(
            #     channel,
            #     limit=3  # Количество сообщений для получения
            # ))

            messages = await client(GetHistoryRequest(
                peer=channel,
                limit=10,  # Количество сообщений
                offset_id=0,
                offset_date=None,
                add_offset=0,
                max_id=0,
                min_id=0,
                hash=0
            ))

            # print("Получение сообщений")
            # messages = get_channel_messages(channel)
            # Перебираем каждое сообщение и выводим его текст
            for msg in messages.messages:
                print(f"ID сообщения: {msg.id}")
                print(f"Дата отправки: {msg.date}")
                print(f"Текст сообщения: {msg.message}")
                print("---" * 20)


    except Exception as e:
        print(f"Произошла ошибка: {e}")


asyncio.run(main())

# if __name__ == '__main__':
#     main()