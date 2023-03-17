from config import *
from pyrogram import Client, filters, idle
from pyrogram.types import Message, BotCommand
from pyrogram.handlers import MessageHandler
import asyncio
import logging

user_bot = Client('user_bot', api_id=api_id, api_hash=api_hash)
bot_content = Client('bot_content', api_id=api_id, api_hash=api_hash, bot_token=bot_token)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')


@user_bot.on_message(filters.chat(chats=donors_ids))
async def new_post(client: Client, message: Message):
    await client.copy_message(chat_id=tech_channel, from_chat_id=message.chat.id, message_id=message.id)


@bot_content.on_message(filters.reply)
async def copy_to_my_channel(client: Client, message: Message):
    await client.copy_message(chat_id=my_target_channel, from_chat_id=message.chat.id, message_id=message.reply_to_message.id)
    await message.delete()
    await message.reply_to_message.delete()

# user_bot.start()
# bot_content.start()
# idle()
# user_bot.stop()
# bot_content.stop()
