"""
Bridge between assistant bot and userbot
Allows controlling userbot via bot interface
"""

from pyrogram import Client, filters
from pyrogram.types import Message

# Required Imports
from config import Config
from main import bot
from utils.helpers import anime_border

@Client.on_message(filters.command("userstats") & filters.private)
async def user_stats_command(client: Client, message: Message):
    """Get real-time statistics from the userbot account"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    try:
        # Access the userbot instance
        userbot = bot.app
        me = await userbot.get_me()
        
        # Fetching dialogs (Private, Groups, Channels)
        dialogs = await userbot.get_dialogs()
        
        private = sum(1 for d in dialogs if d.chat.type.name == "PRIVATE")
        groups = sum(1 for d in dialogs if d.chat.type.name in ["GROUP", "SUPERGROUP"])
        channels = sum(1 for d in dialogs if d.chat.type.name == "CHANNEL")
        
        stats_text = (
            f"│  <b>Userbot Statistics</b>\n"
            f"│\n"
            f"│  <b>Name:</b> {me.first_name}\n"
            f"│  <b>ID:</b> <code>{me.id}</code>\n"
            f"│\n"
            f"│  👤 <b>Private:</b> {private}\n"
            f"│  👥 <b>Groups:</b> {groups}\n"
            f"│  📢 <b>Channels:</b> {channels}\n"
            f"│  📊 <b>Total:</b> {len(dialogs)}\n"
        )
        
        response = anime_border(stats_text, "User Stats")
        await message.reply_text(response)
        
    except Exception as e:
        await message.reply_text(f"❌ <b>Error:</b> <code>{str(e)}</code>")

@Client.on_message(filters.command("sendmsg") & filters.private)
async def send_message_command(client: Client, message: Message):
    """Send a message to any chat using the Userbot account"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    try:
        # Usage: /sendmsg chat_id text
        args = message.text.split(None, 2)
        chat_id = args[1]
        text = args[2]
        
        userbot = bot.app
        await userbot.send_message(chat_id, text)
        await message.reply_text("✅ Message sent successfully via Userbot!")
        
    except IndexError:
        await message.reply_text(
            "❌ <b>Usage:</b> <code>/sendmsg chat_id text</code>\n"
            "<b>Example:</b> <code>/sendmsg me Hello!</code>"
        )
    except Exception as e:
        await message.reply_text(f"❌ <b>Error:</b> <code>{str(e)}</code>")

@Client.on_message(filters.command("forward") & filters.private)
async def forward_command(client: Client, message: Message):
    """Forward a replied message via Userbot"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    if not message.reply_to_message:
        return await message.reply_text("❌ Reply to a message to forward it!")
    
    try:
        # Usage: /forward chat_id (as a reply)
        chat_id = message.text.split()[1]
        
        userbot = bot.app
        await userbot.forward_messages(
            chat_id=chat_id,
            from_chat_id=message.chat.id,
            message_ids=message.reply_to_message.id
        )
        
        await message.reply_text(f"✅ Message forwarded to <code>{chat_id}</code>")
        
    except IndexError:
        await message.reply_text("❌ Provide a target <code>chat_id</code>!")
    except Exception as e:
        await message.reply_text(f"❌ <b>Error:</b> <code>{str(e)}</code>")