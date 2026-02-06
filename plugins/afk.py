"""
AFK Plugin for Kaoruko Userbot
Beautiful anime-themed AFK system 💙
"""

import time
from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import get_time_difference, anime_border, edit_or_reply, mention_user
from utils.logger import LOGGER

# Store AFK data in memory
afk_status = {}

@Client.on_message(
    filters.command("afk", prefixes=Config.CMD_PREFIX) & filters.me
)
async def set_afk_command(client: Client, message: Message):
    """Set AFK status"""
    
    # Get reason from message
    reason = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    
    # Get media if replied to photo/video
    media = None
    if message.reply_to_message:
        if message.reply_to_message.photo:
            media = message.reply_to_message.photo.file_id
        elif message.reply_to_message.video:
            media = message.reply_to_message.video.file_id
        elif message.reply_to_message.animation:
            media = message.reply_to_message.animation.file_id
    
    # Set AFK
    afk_status[client.me.id] = {
        "reason": reason,
        "time": time.time(),
        "media": media,
        "mentions": 0
    }
    
    # Save to database
    try:
        from main import bot
        if bot.db:
            await bot.db.set_afk(client.me.id, reason, media)
    except:
        pass
    
    # Create beautiful AFK message
    afk_text = "│  <b>Status:</b> <code>AFK</code>\n"
    if reason:
        afk_text += f"│  <b>Reason:</b> <i>{reason}</i>\n"
    
    response = anime_border(afk_text, "Going AFK")
    
    if media:
        if message.reply_to_message.photo:
            await message.reply_photo(media, caption=response)
        elif message.reply_to_message.video:
            await message.reply_video(media, caption=response)
        elif message.reply_to_message.animation:
            await message.reply_animation(media, caption=response)
        await message.delete()
    else:
        await edit_or_reply(message, response)
    
    LOGGER.info(f"AFK set with reason: {reason}")

@Client.on_message(filters.mentioned & ~filters.me & ~filters.bot)
async def afk_mention_handler(client: Client, message: Message):
    """Handle mentions when AFK"""
    
    # Check if user is AFK
    if client.me.id not in afk_status:
        return
    
    afk_data = afk_status[client.me.id]
    
    # Increment mention counter
    afk_data["mentions"] += 1
    
    # Calculate time
    afk_time = get_time_difference(afk_data["time"])
    
    # Create response
    response_text = (
        f"│  <b>User:</b> {mention_user(client.me)}\n"
        f"│  <b>Status:</b> <code>AFK</code>\n"
        f"│  <b>Since:</b> <code>{afk_time}</code>\n"
    )
    
    if afk_data["reason"]:
        response_text += f"│  <b>Reason:</b> <i>{afk_data['reason']}</i>\n"
    
    response = anime_border(response_text, "User is AFK")
    
    # Send response
    if afk_data["media"]:
        try:
            # Determine media type and send accordingly
            await message.reply_photo(afk_data["media"], caption=response)
        except:
            await message.reply_text(response)
    else:
        await message.reply_text(response, disable_web_page_preview=True)

@Client.on_message(filters.outgoing & ~filters.command("afk", prefixes=Config.CMD_PREFIX))
async def remove_afk_on_message(client: Client, message: Message):
    """Remove AFK when user sends a message"""
    
    if client.me.id not in afk_status:
        return
    
    afk_data = afk_status[client.me.id]
    afk_time = get_time_difference(afk_data["time"])
    mentions = afk_data["mentions"]
    
    # Remove AFK
    del afk_status[client.me.id]
    
    # Remove from database
    try:
        from main import bot
        if bot.db:
            await bot.db.remove_afk(client.me.id)
    except:
        pass
    
    # Create welcome back message
    response_text = (
        f"│  <b>Status:</b> <code>Back Online</code>\n"
        f"│  <b>AFK Duration:</b> <code>{afk_time}</code>\n"
        f"│  <b>Mentions:</b> <code>{mentions}</code>\n"
    )
    
    response = anime_border(response_text, "Welcome Back")
    
    await message.reply_text(response, quote=False)
    LOGGER.info(f"AFK removed after {afk_time}")

# Plugin info
__MODULE__ = "AFK"
__HELP__ = """
**AFK Module** 💙

Set yourself as Away From Keyboard with anime aesthetic!

**Commands:**
• `.afk [reason]` - Set AFK status
• `.afk` (reply to media) - Set AFK with media

**Features:**
• Auto-reply to mentions
• Beautiful anime-themed messages
• Track mentions count
• Support for photos/videos/GIFs
• MongoDB persistence

**Examples:**
```
.afk Sleeping 😴
.afk Working on something important
.afk (reply to anime gif)
```
"""
