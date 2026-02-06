"""
Additional Commands for Assistant Bot
Extends the inline.py functionality with more features
"""

import time
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from main import bot
from utils.helpers import anime_border, info_box

# --- AUTHORIZATION CHECK ---
def is_auth(user_id):
    """Checks if the user is authorized to use the bot"""
    return user_id in [Config.OWNER_ID] + Config.SUDO_USERS

# ==========================================
#         USERBOT CONTROL COMMANDS
# ==========================================

@Client.on_message(filters.command("userstats") & filters.private)
async def user_stats_command(client: Client, message: Message):
    """Get real-time statistics from the userbot account"""
    
    if not is_auth(message.from_user.id):
        return await message.reply_text("❌ <b>Access Denied!</b>")
    
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
            f"│  <b>Username:</b> @{me.username or 'None'}\n"
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
    
    if not is_auth(message.from_user.id):
        return await message.reply_text("❌ <b>Access Denied!</b>")
    
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
            "❌ <b>Usage:</b> <code>/sendmsg chat_id text</code>\n\n"
            "<b>Examples:</b>\n"
            "<code>/sendmsg me Hello!</code>\n"
            "<code>/sendmsg -100123456 Important update</code>"
        )
    except Exception as e:
        await message.reply_text(f"❌ <b>Error:</b> <code>{str(e)}</code>")

@Client.on_message(filters.command("forward") & filters.private)
async def forward_command(client: Client, message: Message):
    """Forward a replied message via Userbot"""
    
    if not is_auth(message.from_user.id):
        return await message.reply_text("❌ <b>Access Denied!</b>")
    
    if not message.reply_to_message:
        return await message.reply_text(
            "❌ Reply to a message to forward it!\n\n"
            "<b>Usage:</b> Reply to message + <code>/forward chat_id</code>"
        )
    
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
        await message.reply_text(
            "❌ Provide a target <code>chat_id</code>!\n\n"
            "<b>Example:</b> <code>/forward me</code>"
        )
    except Exception as e:
        await message.reply_text(f"❌ <b>Error:</b> <code>{str(e)}</code>")

# ==========================================
#         UTILITY COMMANDS
# ==========================================

@Client.on_message(filters.command("botinfo") & filters.private)
async def bot_info_command(client: Client, message: Message):
    """Show bot information"""
    
    if not is_auth(message.from_user.id):
        return await message.reply_text("❌ <b>Access Denied!</b>")
    
    bot_me = await client.get_me()
    
    info_text = (
        f"│  <b>Bot Information</b>\n"
        f"│\n"
        f"│  <b>Name:</b> {bot_me.first_name}\n"
        f"│  <b>Username:</b> @{bot_me.username}\n"
        f"│  <b>ID:</b> <code>{bot_me.id}</code>\n"
        f"│  <b>Version:</b> <code>1.0.0</code>\n"
        f"│  <b>Framework:</b> <code>Pyrogram</code>\n"
        f"│  <b>Theme:</b> <code>Kaoruko 💙</code>\n"
    )
    
    response = anime_border(info_text, "Bot Info")
    await message.reply_text(response)

@Client.on_message(filters.command("broadcast") & filters.private)
async def broadcast_command(client: Client, message: Message):
    """Broadcast message to all chats via userbot"""
    
    # Only owner can broadcast
    if message.from_user.id != Config.OWNER_ID:
        return await message.reply_text("❌ Only owner can use this command!")
    
    try:
        broadcast_text = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply_text(
            "❌ <b>Usage:</b> <code>/broadcast message</code>\n\n"
            "<b>Example:</b>\n"
            "<code>/broadcast Hello everyone!</code>"
        )
    
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
                await asyncio.sleep(0.5)  # Avoid flood
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

@Client.on_message(filters.command("system") & filters.private)
async def system_command(client: Client, message: Message):
    """Show system information"""
    
    if not is_auth(message.from_user.id):
        return await message.reply_text("❌ <b>Access Denied!</b>")
    
    import platform
    import psutil
    
    # Get system info
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_total = ram.total / (1024 ** 3)  # GB
    ram_used = ram.used / (1024 ** 3)  # GB
    
    system_text = (
        f"│  <b>System Information</b>\n"
        f"│\n"
        f"│  <b>OS:</b> <code>{platform.system()}</code>\n"
        f"│  <b>Python:</b> <code>{platform.python_version()}</code>\n"
        f"│\n"
        f"│  <b>CPU Usage:</b> <code>{cpu_percent}%</code>\n"
        f"│  <b>RAM Usage:</b> <code>{ram_percent}%</code>\n"
        f"│  <b>RAM:</b> <code>{ram_used:.2f}/{ram_total:.2f} GB</code>\n"
    )
    
    response = anime_border(system_text, "System Info")
    await message.reply_text(response)

# ==========================================
#         ADMIN COMMANDS
# ==========================================

@Client.on_message(filters.command("restart") & filters.private)
async def restart_command(client: Client, message: Message):
    """Restart the userbot"""
    
    # Only owner can restart
    if message.from_user.id != Config.OWNER_ID:
        return await message.reply_text("❌ Only owner can restart!")
    
    await message.reply_text(
        "🔄 <b>Restarting...</b>\n\n"
        "<i>Bot will be back online in a few seconds.</i>"
    )
    
    import os
    import sys
    
    # Restart the bot
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("logs") & filters.private)
async def logs_command(client: Client, message: Message):
    """Send bot logs"""
    
    # Only owner can view logs
    if message.from_user.id != Config.OWNER_ID:
        return await message.reply_text("❌ Only owner can view logs!")
    
    try:
        # Read last 50 lines from log file
        with open("kaoruko.log", "r") as f:
            logs = f.readlines()
            last_logs = "".join(logs[-50:])
        
        if len(last_logs) > 4000:
            # Send as file if too long
            await message.reply_document(
                "kaoruko.log",
                caption="📄 <b>Bot Logs</b>"
            )
        else:
            await message.reply_text(
                f"📄 <b>Last 50 Log Entries:</b>\n\n"
                f"<code>{last_logs}</code>"
            )
    except FileNotFoundError:
        await message.reply_text("❌ No log file found!")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

# ==========================================
#         HELP COMMAND
# ==========================================

@Client.on_message(filters.command("commands") & filters.private)
async def commands_list(client: Client, message: Message):
    """List all available bot commands"""
    
    if not is_auth(message.from_user.id):
        return await message.reply_text("❌ <b>Access Denied!</b>")
    
    commands_text = (
        f"│  <b>Available Commands:</b>\n"
        f"│\n"
        f"│  <b>🎮 Basic:</b>\n"
        f"│  • /start - Main menu\n"
        f"│  • /ping - Check latency\n"
        f"│  • /help - Help menu\n"
        f"│\n"
        f"│  <b>📊 Userbot:</b>\n"
        f"│  • /userstats - User statistics\n"
        f"│  • /sendmsg - Send message\n"
        f"│  • /forward - Forward message\n"
        f"│  • /broadcast - Broadcast (owner)\n"
        f"│\n"
        f"│  <b>⚙️ System:</b>\n"
        f"│  • /botinfo - Bot information\n"
        f"│  • /system - System info\n"
        f"│  • /restart - Restart bot (owner)\n"
        f"│  • /logs - View logs (owner)\n"
        f"│\n"
        f"│  <b>⏰ Utilities:</b>\n"
        f"│  • /setreminder - Set reminder\n"
    )
    
    response = anime_border(commands_text, "Commands List")
    await message.reply_text(response)

# ==========================================
#         MODULE INFO
# ==========================================

__MODULE__ = "Assistant Commands"
__HELP__ = """
**Assistant Bot Commands** 🤖

Additional commands for bot management!

**Userbot Control:**
• `/userstats` - Get userbot statistics
• `/sendmsg <chat> <msg>` - Send message via userbot
• `/forward <chat>` - Forward message (reply)
• `/broadcast <msg>` - Broadcast to all (owner)

**Utilities:**
• `/botinfo` - Show bot information
• `/system` - System information
• `/commands` - List all commands
• `/setreminder <min> <text>` - Set reminder

**Admin (Owner Only):**
• `/restart` - Restart the bot
• `/logs` - View bot logs
• `/broadcast` - Broadcast message

**Examples:**
```
/userstats
/sendmsg me Hello!
/setreminder 30 Check oven
/system
```
"""