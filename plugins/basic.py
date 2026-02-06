import time
import asyncio
import random
import traceback
import os  # ← Local files check karne ke liye add kiya

from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from utils.helpers import edit_or_reply, anime_border, info_box

# Aapke Catbox links
PING_PICS = [
    "https://files.catbox.moe/05o77r.jfif",
    "https://files.catbox.moe/znkeif.jfif",
    "https://files.catbox.moe/jq8zg3.jfif",
    "https://files.catbox.moe/dctcwv.jfif",
    "https://files.catbox.moe/35kd4k.jfif",
    "https://files.catbox.moe/4q9x8e.jfif",
    "https://files.catbox.moe/zxo3mj.jfif",
    "https://files.catbox.moe/7u7bar.jfif"
]

# Local Storage Path
PICS_PATH = "resources/" # Is folder mein pics daal sakte ho

def get_local_pic():
    """Folder se random image uthane ke liye helper function"""
    if os.path.exists(PICS_PATH):
        files = [PICS_PATH + f for f in os.listdir(PICS_PATH) if f.endswith(('.jpg', '.png', '.jpeg', '.jfif'))]
        if files:
            return random.choice(files)
    return None

@Client.on_message(
    filters.command("ping", prefixes=Config.CMD_PREFIX) & filters.me
)
async def ping_command(client: Client, message: Message):
    """Debug mode enabled Ping with Local + Online Support"""
    start = time.time()
    msg = await edit_or_reply(message, "🔍 <code>Debugging & Pinging...</code>")
    end = time.time()
    
    ping_time = (end - start) * 1000
    
    # PEHLE LOCAL CHECK KARO, NAHI TOH ONLINE LINKS
    pic = get_local_pic() or random.choice(PING_PICS)
    
    ping_text = (
        f"│  <b>🏓 Pong!</b>\n"
        f"│\n"
        f"│  ⚡ <b>Latency:</b> <code>{ping_time:.2f}ms</code>\n"
        f"│  🌐 <b>Status:</b> <code>Online</code>\n"
    )
    response = anime_border(ping_text, "Kaoruko System")
    
    try:
        # Step 1: Photo bhejne ki koshish (Local ya URL dono handle karega)
        await client.send_photo(
            chat_id=message.chat.id,
            photo=pic,
            caption=response
        )
        # Step 2: Success hone par purana text delete
        await msg.delete() 
        
    except Exception:
        # STEP 3: Debugging - Agar fail hua toh error detail nikalega
        error_info = traceback.format_exc()
        short_error = error_info.splitlines()[-1]
        
        debug_msg = (
            f"{response}\n\n"
            f"❌ <b>Debug Info:</b>\n"
            f"<code>{short_error}</code>\n\n"
            f"💡 <i>Check terminal for full Traceback!</i>"
        )
        await msg.edit(debug_msg)
        print(f"DEBUG ERROR: {error_info}")

@Client.on_message(
    filters.command("alive", prefixes=Config.CMD_PREFIX) & filters.me
)
async def alive_command(client: Client, message: Message):
    """Check if bot is alive with random aesthetic media"""
    msg = await edit_or_reply(message, "⚔️ <code>Kaoruko System is waking up...</code>")
    
    # Randomly picking from local folder or online links
    pic = get_local_pic() or random.choice(PING_PICS)
    
    alive_text = (
        f"│  ⚔️ <b>SYSTEM STATUS</b>\n"
        f"│\n"
        f"│  🎛 <b>Bot:</b> <code>{Config.BOT_NAME}</code>\n"
        f"│  🧬 <b>Version:</b> <code>{Config.BOT_VERSION}</code>\n"
        f"│  🌌 <b>Theme:</b> <code>Aesthetic Dark</code>\n"
        f"│\n"
        f"│  ✨ <i>\"Protecting your digital realm...\"</i>\n"
    )
    
    response = anime_border(alive_text, "Kaoruko Online")
    
    try:
        if pic.endswith((".mp4", ".gif")):
            await client.send_video(
                chat_id=message.chat.id,
                video=pic,
                caption=response
            )
        else:
            await client.send_photo(
                chat_id=message.chat.id,
                photo=pic,
                caption=response
            )
        await msg.delete()
        
    except Exception as e:
        await msg.edit(f"{response}\n\n❌ <b>Media Error:</b> <code>{e}</code>")

@Client.on_message(
    filters.command("help", prefixes=Config.CMD_PREFIX) & filters.me
)
async def help_command(client: Client, message: Message):
    """Show help message"""
    try:
        plugin_name = message.text.split(None, 1)[1]
    except IndexError:
        text = (
            "│  💙 <b>Kaoruko Userbot</b>\n"
            "│\n"
            "│  <b>Available Commands:</b>\n"
            "│  • <code>.help [plugin]</code> - Show help\n"
            "│  • <code>.ping</code> - Response time\n"
            "│  • <code>.alive</code> - Bot status\n"
            "│\n"
            "│  👤 <b>Dev:</b> @ray\n"
        )
        response = anime_border(text, "Help Menu")
        await edit_or_reply(message, response)
        return
    
    try:
        module = __import__(f"plugins.{plugin_name}", fromlist=["__HELP__"])
        help_text = getattr(module, "__HELP__", "No help available.")
        await edit_or_reply(message, help_text)
    except Exception:
        await edit_or_reply(message, f"❌ Plugin <code>{plugin_name}</code> not found!")

@Client.on_message(
    filters.command("stats", prefixes=Config.CMD_PREFIX) & filters.me
)
async def stats_command(client: Client, message: Message):
    """Show user statistics"""
    user = await client.get_me()
    dialogs = await client.get_dialogs()
    
    private_chats = sum(1 for d in dialogs if d.chat.type.name == "PRIVATE")
    groups = sum(1 for d in dialogs if d.chat.type.name in ["GROUP", "SUPERGROUP"])
    channels = sum(1 for d in dialogs if d.chat.type.name == "CHANNEL")
    
    info = {
        "Name": user.first_name,
        "Username": f"@{user.username}" if user.username else "None",
        "User ID": user.id,
        "Private Chats": private_chats,
        "Groups": groups,
        "Channels": channels,
        "Total": len(dialogs)
    }
    
    response = info_box("Statistics", info)
    await edit_or_reply(message, response)

@Client.on_message(
    filters.command("id", prefixes=Config.CMD_PREFIX) & filters.me
)
async def id_command(client: Client, message: Message):
    """Get chat/user ID"""
    chat_id = message.chat.id
    
    info = {
        "Chat ID": chat_id,
    }
    
    if message.reply_to_message:
        replied_user = message.reply_to_message.from_user
        if replied_user:
            info["Replied User"] = replied_user.first_name
            info["User ID"] = replied_user.id
    elif message.from_user:
        info["Your User ID"] = message.from_user.id
    
    response = info_box("ID Information", info)
    await edit_or_reply(message, response)

@Client.on_message(
    filters.command("purge", prefixes=Config.CMD_PREFIX) & filters.me
)
async def purge_command(client: Client, message: Message):
    """Delete messages in bulk"""
    if not message.reply_to_message:
        return await edit_or_reply(message, "❌ Reply to a message!")
    
    msg = await edit_or_reply(message, "⏳ <i>Purging messages...</i>")
    
    start_id = message.reply_to_message.id
    end_id = message.id
    
    deleted = 0
    message_ids = []
    
    for msg_id in range(start_id, end_id + 1):
        message_ids.append(msg_id)
        if len(message_ids) >= 100:
            await client.delete_messages(
                chat_id=message.chat.id,
                message_ids=message_ids
            )
            deleted += len(message_ids)
            message_ids = []
    
    if message_ids:
        await client.delete_messages(
            chat_id=message.chat.id,
            message_ids=message_ids
        )
        deleted += len(message_ids)
    
    result = await client.send_message(
        message.chat.id,
        f"✅ Purged <code>{deleted}</code> messages!"
    )
    
    await asyncio.sleep(3)
    await result.delete()

@Client.on_message(
    filters.command("del", prefixes=Config.CMD_PREFIX) & filters.me
)
async def delete_command(client: Client, message: Message):
    """Delete replied message"""
    if message.reply_to_message:
        await message.reply_to_message.delete()
    await message.delete()

# Plugin info
__MODULE__ = "Basic"
__HELP__ = """
**Basic Commands** 💙

Essential utility commands for daily use!

**Commands:**
• `.ping` - Check response time (Auto Local/URL)
• `.alive` - Check bot status
• `.help [plugin]` - Show help
• `.stats` - Show statistics
• `.id` - Get chat/user ID
• `.purge` - Delete messages (reply)
• `.del` - Delete message (reply)

**Features:**
• Beautiful anime-themed responses
• Support for Local & Online pics
• Detailed Debugging

**Setup Local Pics:**
Put your images in `resources/` folder.
"""