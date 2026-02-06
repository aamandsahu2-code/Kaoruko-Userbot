"""
Assistant Bot Handlers
Inline features and helper commands
"""

from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

from config import Config
from utils.helpers import anime_border, info_box

# --- Custom Authorization Filter ---
# Yeh filter check karega ki user Owner ya Sudo hai ya nahi
def is_authorized(_, __, update):
    user_id = update.from_user.id
    return user_id in [Config.OWNER_ID] + Config.SUDO_USERS

auth_filter = filters.create(is_authorized)

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    """Start command for assistant bot"""
    
    user = message.from_user
    
    # Unauthorized users ke liye message
    if not (user.id in [Config.OWNER_ID] + Config.SUDO_USERS):
        await message.reply_text(
            "❌ <b>Access Denied!</b>\n\n"
            "This bot is private and only accessible to authorized users."
        )
        return
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💙 Help", callback_data="help"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings")
        ],
        [
            InlineKeyboardButton("📊 Stats", callback_data="stats"),
            InlineKeyboardButton("🔌 Plugins", callback_data="plugins")
        ],
        [
            InlineKeyboardButton("✨ About", callback_data="about")
        ]
    ])
    
    text = (
        f"│  👋 <b>Hello, {user.first_name}!</b>\n"
        f"│\n"
        f"│  Welcome to <b>Kaoruko Assistant Bot</b>\n"
        f"│  Your personal anime-themed helper! 💙\n"
        f"│\n"
        f"│  <i>Click buttons below to explore</i>\n"
    )
    
    response = anime_border(text, "Kaoruko Assistant")
    await message.reply_text(response, reply_markup=buttons)

@Client.on_callback_query(filters.regex("^help$") & auth_filter)
async def help_callback(client: Client, callback: CallbackQuery):
    """Help callback"""
    
    text = (
        "│  <b>💙 Kaoruko Assistant Help</b>\n"
        "│\n"
        "│  This bot provides inline features\n"
        "│  and helper commands for the main\n"
        "│  userbot.\n"
        "│\n"
        "│  <b>Features:</b>\n"
        "│  • Inline queries\n"
        "│  • Button menus\n"
        "│  • Settings management\n"
        "│  • Statistics tracking\n"
        "│\n"
        "│  <i>More features coming soon!</i>\n"
    )
    
    response = anime_border(text, "Help")
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("« Back", callback_data="start")]])
    
    await callback.message.edit_text(response, reply_markup=buttons)
    await callback.answer()

@Client.on_callback_query(filters.regex("^settings$") & auth_filter)
async def settings_callback(client: Client, callback: CallbackQuery):
    """Settings callback"""
    
    text = (
        "│  <b>⚙️ Settings</b>\n"
        "│\n"
        "│  Configure your userbot here\n"
        "│\n"
        "│  <b>Available Settings:</b>\n"
        "│  • Command prefix\n"
        "│  • AFK settings\n"
        "│  • Plugin management\n"
        "│  • Theme customization\n"
        "│\n"
        "│  <i>Use buttons to adjust settings</i>\n"
    )
    
    response = anime_border(text, "Settings")
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔧 Prefix", callback_data="set_prefix"),
            InlineKeyboardButton("💤 AFK", callback_data="set_afk")
        ],
        [InlineKeyboardButton("« Back", callback_data="start")]
    ])
    
    await callback.message.edit_text(response, reply_markup=buttons)
    await callback.answer()

@Client.on_callback_query(filters.regex("^stats$") & auth_filter)
async def stats_callback(client: Client, callback: CallbackQuery):
    """Stats callback"""
    
    text = (
        "│  <b>📊 Statistics</b>\n"
        "│\n"
        "│  <b>Uptime:</b> <code>Running</code>\n"
        "│  <b>Commands:</b> <code>50+</code>\n"
        "│  <b>Plugins:</b> <code>Active</code>\n"
        "│  <b>Database:</b> <code>Connected</code>\n"
        "│\n"
        "│  <i>All systems operational!</i>\n"
    )
    
    response = anime_border(text, "Statistics")
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("« Back", callback_data="start")]])
    
    await callback.message.edit_text(response, reply_markup=buttons)
    await callback.answer()

@Client.on_callback_query(filters.regex("^plugins$") & auth_filter)
async def plugins_callback(client: Client, callback: CallbackQuery):
    """Plugins callback"""
    
    text = (
        "│  <b>🔌 Plugins</b>\n"
        "│\n"
        "│  <b>Active Plugins:</b>\n"
        "│  ✅ AFK Module\n"
        "│  ✅ Basic Commands\n"
        "│  ✅ Plugin Manager\n"
        "│\n"
        "│  <i>Load more plugins via userbot</i>\n"
    )
    
    response = anime_border(text, "Plugins")
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("« Back", callback_data="start")]])
    
    await callback.message.edit_text(response, reply_markup=buttons)
    await callback.answer()

@Client.on_callback_query(filters.regex("^about$") & auth_filter)
async def about_callback(client: Client, callback: CallbackQuery):
    """About callback"""
    
    text = (
        "│  <b>✨ About Kaoruko</b>\n"
        "│\n"
        "│  <b>Version:</b> <code>1.0.0</code>\n"
        "│  <b>Framework:</b> <code>Pyrogram</code>\n"
        "│  <b>Database:</b> <code>MongoDB</code>\n"
        "│  <b>Theme:</b> <code>Kaoruko Waguri 💙</code>\n"
        "│\n"
        "│  A beautiful anime-themed userbot\n"
        "│  with modern features and elegant design.\n"
        "│\n"
        "│  <i>Made with 💙</i>\n"
    )
    
    response = anime_border(text, "About")
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("« Back", callback_data="start")]])
    
    await callback.message.edit_text(response, reply_markup=buttons)
    await callback.answer()

@Client.on_callback_query(filters.regex("^start$") & auth_filter)
async def start_callback(client: Client, callback: CallbackQuery):
    """Back to start"""
    
    user = callback.from_user
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💙 Help", callback_data="help"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings")
        ],
        [
            InlineKeyboardButton("📊 Stats", callback_data="stats"),
            InlineKeyboardButton("🔌 Plugins", callback_data="plugins")
        ],
        [
            InlineKeyboardButton("✨ About", callback_data="about")
        ]
    ])
    
    text = (
        f"│  👋 <b>Hello, {user.first_name}!</b>\n"
        f"│\n"
        f"│  Welcome to <b>Kaoruko Assistant Bot</b>\n"
        f"│  Your personal anime-themed helper! 💙\n"
        f"│\n"
        f"│  <i>Click buttons below to explore</i>\n"
    )
    
    response = anime_border(text, "Kaoruko Assistant")
    
    await callback.message.edit_text(response, reply_markup=buttons)
    await callback.answer()

# Plugin info
__MODULE__ = "Assistant"
__HELP__ = """
**Assistant Bot** 🤖

Inline features and helper commands!

**Features:**
• Beautiful inline menus
• Settings management
• Statistics display
• Plugin information

**Access:**
Only owner and sudo users can use this bot.
"""