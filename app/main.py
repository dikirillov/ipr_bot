import telebot
import random
from telebot import types
from telebot.async_telebot import AsyncTeleBot
import asyncio
import aioschedule

from submodules import smeshars
from secret_token import TOKEN

bot = AsyncTeleBot(TOKEN)


@bot.message_handler(commands=['start'])
async def start_message(message):
    message_to_send = "Привет! Это тестовый бот, который умеет исполнять всего 5 методов\n\
/start - старт\n\
/help - помощь\n\
/statistics - статистика по чату\n\
/rand - случайное число от 1 до 100\n\
/smeshar - случайный смешарик"
    await bot.send_message(message.chat.id, message_to_send)


@bot.message_handler(commands=['statistics'])
async def stat_message(message):
    cur_chat_id = message.chat.id
    users_cnt = await bot.get_chat_member_count(cur_chat_id)
    try:
        admins_cnt = len(await bot.get_chat_administrators(cur_chat_id))
    except:
        admins_cnt = "Неизвестно"
    await bot.send_message(message.chat.id, "Число пользователей в этом чате: " + str(users_cnt) + '\n' + "Число админов в чате: " + str(admins_cnt))


@bot.message_handler(commands=['help'])
async def help_message(message):
    cur_chat_id = message.chat.id
    message_to_send = "/start - старт\n\
/help - помощь\n\
/statistics - статистика по чату\n\
/rand - случайное число от 1 до 100\n\
/smeshar - случайный смешарик"
    await bot.send_message(message.chat.id, message_to_send)


@bot.message_handler(commands=['rand'])
async def rand_message(message):
    await bot.send_message(message.chat.id, str(random.randint(1, 100)))


@bot.message_handler(commands=['smeshar'])
async def smeshar_message(message):
    await bot.send_photo(message.chat.id, random.choice(smeshars))


async def scheduler():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(bot.infinity_polling(), scheduler())


if __name__ == '__main__':
    asyncio.run(main())
