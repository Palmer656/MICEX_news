import asyncio
import os
import re
from pprint import pprint

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import (FloodWaitError, PhoneNumberBannedError,
                             SessionPasswordNeededError)
from telethon.tl.functions.messages import GetHistoryRequest

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")
two_fa_password = os.getenv("TWO_FA_PASSWORD")
channel_name = os.getenv("CHANNEL_USERNAME")


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

            messages = await client(GetHistoryRequest(
                peer=channel,
                limit=50,  # Количество сообщений
                offset_id=0,
                offset_date=None,
                add_offset=0,
                max_id=0,
                min_id=0,
                hash=0
            ))

            cleared_messages = []
            for msg in messages.messages:
                if not msg.message:
                    continue
                date = msg["datetime"].date()
                time = msg["datetime"].time()
                msg_dict = {"telegram_msg_id": msg.id,
                            "date": date,
                            "time": time,
                            "text": msg.message}
                tags_list = re.findall(r'#\w+', msg_dict["text"])
                tags_list = [tag.replace("#", "") for tag in tags_list]
                msg_dict["tags"] = tags_list
                cleared_messages.append(msg_dict)
            pprint(cleared_messages)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

asyncio.run(main())