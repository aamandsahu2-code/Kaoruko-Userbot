"""
Broadcast Feature for Assistant Bot
Send messages to userbot chats through bot
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import anime_border
from main import bot

@Client.on_message(filters.command("broadcast") & filters.private)
async def broadcast_command(client: Client, message: Message):
    """Broadcast message to all chats"""
    
    # Only owner can broadcast
    if message.from_user.id != Config.OWNER_ID:
        await message.reply_text("❌ Only owner can use this command!")
        return
    
    try:
        broadcast_text = message.text.split(None, 1)[1]
    except IndexError:
        await message.reply_text(
            "❌ <b>Usage:</b> <code>/broadcast message</code>\n\n"
            "<b>Example:</b>\n"
            "<code>/broadcast Hello everyone!</code>"
        )
        return
    
    status_msg = await message.reply_text("📡 <i>Broadcasting...</i>")
    
    try:
        userbot = bot.app
        dialogs = await userbot.get_dialogs()
        
        success = 0
        failed = 0
        
        for dialog in dialogs:
            try:
                await userbot.send_message(
                    dialog.chat.id,
                    broadcast_text
                )
                success += 1
            except:
                failed += 1
        
        result_text = (
            f"│  <b>Broadcast Complete!</b>\n"
            f"│\n"
            f"│  ✅ <b>Sent:</b> {success}\n"
            f"│  ❌ <b>Failed:</b> {failed}\n"
            f"│  📊 <b>Total:</b> {len(dialogs)}\n"
        )
        
        response = anime_border(result_text, "Broadcast Result")
        await status_msg.edit_text(response)
        
    except Exception as e:
        await status_msg.edit_text(f"❌ Error: {str(e)}")

@Client.on_message(filters.command("sendto") & filters.private)
async def send_to_command(client: Client, message: Message):
    """Send message to specific chat"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    try:
        args = message.text.split(None, 2)
        chat_id = args[1]
        text = args[2]
    except IndexError:
        await message.reply_text(
            "❌ <b>Usage:</b> <code>/sendto chat_id text</code>\n\n"
            "<b>Examples:</b>\n"
            "<code>/sendto me Hello!</code>\n"
            "<code>/sendto -100123456 Important message</code>"
        )
        return
    
    try:
        userbot = bot.app
        await userbot.send_message(chat_id, text)
        await message.reply_text("✅ Message sent successfully!")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

@Client.on_message(filters.command("forward") & filters.private)
async def forward_command(client: Client, message: Message):
    """Forward message to specific chat"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    if not message.reply_to_message:
        await message.reply_text(
            "❌ Reply to a message with:\n"
            "<code>/forward chat_id</code>"
        )
        return
    
    try:
        chat_id = message.text.split()[1]
    except IndexError:
        await message.reply_text("❌ Provide chat ID!")
        return
    
    try:
        userbot = bot.app
        await message.reply_to_message.forward(chat_id)
        await message.reply_text("✅ Message forwarded!")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")