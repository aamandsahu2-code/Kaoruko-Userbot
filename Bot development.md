# 🤖 Assistant Bot Development Guide

## 📚 Table of Contents
1. [Basic Bot Commands](#basic-bot-commands)
2. [Inline Buttons & Callbacks](#inline-buttons--callbacks)
3. [Inline Queries](#inline-queries)
4. [Interactive Features](#interactive-features)
5. [Integration with Userbot](#integration-with-userbot)

---

## 🎯 Basic Bot Commands

### File: `assistant/commands.py`

```python
"""
Basic commands for assistant bot
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import anime_border

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    """Help command for bot"""
    
    # Check authorization
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        await message.reply_text("❌ You are not authorized to use this bot!")
        return
    
    help_text = (
        "│  <b>Available Commands:</b>\n"
        "│\n"
        "│  /start - Start the bot\n"
        "│  /help - Show this help\n"
        "│  /ping - Check bot status\n"
        "│  /info - Get user info\n"
        "│  /stats - View statistics\n"
    )
    
    response = anime_border(help_text, "Bot Help")
    await message.reply_text(response)

@Client.on_message(filters.command("ping") & filters.private)
async def ping_command(client: Client, message: Message):
    """Ping command"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    await message.reply_text("🏓 <b>Pong!</b>\n\nBot is online and working!")

@Client.on_message(filters.command("info") & filters.private)
async def info_command(client: Client, message: Message):
    """Get user information"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    user = message.from_user
    
    info_text = (
        f"│  <b>Your Information:</b>\n"
        f"│\n"
        f"│  <b>Name:</b> {user.first_name}\n"
        f"│  <b>User ID:</b> <code>{user.id}</code>\n"
    )
    
    if user.username:
        info_text += f"│  <b>Username:</b> @{user.username}\n"
    
    response = anime_border(info_text, "User Info")
    await message.reply_text(response)
```

---

## 🔘 Inline Buttons & Callbacks

### File: `assistant/buttons.py`

```python
"""
Inline button examples for assistant bot
"""

from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import Config
from utils.helpers import anime_border

@Client.on_message(filters.command("menu") & filters.private)
async def menu_command(client: Client, message: Message):
    """Show interactive menu"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ℹ️ Info", callback_data="menu_info"),
            InlineKeyboardButton("⚙️ Settings", callback_data="menu_settings")
        ],
        [
            InlineKeyboardButton("📊 Stats", callback_data="menu_stats"),
            InlineKeyboardButton("🔌 Plugins", callback_data="menu_plugins")
        ],
        [
            InlineKeyboardButton("❌ Close", callback_data="menu_close")
        ]
    ])
    
    text = (
        "│  <b>Main Menu</b>\n"
        "│\n"
        "│  Choose an option below:\n"
    )
    
    response = anime_border(text, "Menu")
    await message.reply_text(response, reply_markup=buttons)

@Client.on_callback_query(filters.regex("^menu_"))
async def menu_callback(client: Client, callback: CallbackQuery):
    """Handle menu callbacks"""
    
    action = callback.data.split("_")[1]
    
    if action == "info":
        text = (
            "│  <b>Bot Information</b>\n"
            "│\n"
            "│  <b>Name:</b> Kaoruko Assistant\n"
            "│  <b>Version:</b> 1.0.0\n"
            "│  <b>Framework:</b> Pyrogram\n"
        )
        
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("« Back", callback_data="menu_back")]
        ])
        
        response = anime_border(text, "Info")
        await callback.message.edit_text(response, reply_markup=buttons)
    
    elif action == "settings":
        text = (
            "│  <b>Settings</b>\n"
            "│\n"
            "│  Configure bot settings:\n"
        )
        
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🔔 Notifications", callback_data="set_notif"),
                InlineKeyboardButton("🌐 Language", callback_data="set_lang")
            ],
            [InlineKeyboardButton("« Back", callback_data="menu_back")]
        ])
        
        response = anime_border(text, "Settings")
        await callback.message.edit_text(response, reply_markup=buttons)
    
    elif action == "stats":
        # Get stats from database or userbot
        text = (
            "│  <b>Statistics</b>\n"
            "│\n"
            "│  <b>Uptime:</b> Running\n"
            "│  <b>Commands:</b> 30+\n"
            "│  <b>Plugins:</b> 5 active\n"
        )
        
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("« Back", callback_data="menu_back")]
        ])
        
        response = anime_border(text, "Statistics")
        await callback.message.edit_text(response, reply_markup=buttons)
    
    elif action == "plugins":
        text = (
            "│  <b>Active Plugins</b>\n"
            "│\n"
            "│  ✅ AFK Module\n"
            "│  ✅ Basic Commands\n"
            "│  ✅ Fun Commands\n"
            "│  ✅ Plugin Manager\n"
        )
        
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("« Back", callback_data="menu_back")]
        ])
        
        response = anime_border(text, "Plugins")
        await callback.message.edit_text(response, reply_markup=buttons)
    
    elif action == "close":
        await callback.message.delete()
    
    elif action == "back":
        # Recreate main menu
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ℹ️ Info", callback_data="menu_info"),
                InlineKeyboardButton("⚙️ Settings", callback_data="menu_settings")
            ],
            [
                InlineKeyboardButton("📊 Stats", callback_data="menu_stats"),
                InlineKeyboardButton("🔌 Plugins", callback_data="menu_plugins")
            ],
            [
                InlineKeyboardButton("❌ Close", callback_data="menu_close")
            ]
        ])
        
        text = (
            "│  <b>Main Menu</b>\n"
            "│\n"
            "│  Choose an option below:\n"
        )
        
        response = anime_border(text, "Menu")
        await callback.message.edit_text(response, reply_markup=buttons)
    
    # Answer callback to remove loading state
    await callback.answer()

@Client.on_callback_query(filters.regex("^set_"))
async def settings_callback(client: Client, callback: CallbackQuery):
    """Handle settings callbacks"""
    
    setting = callback.data.split("_")[1]
    
    if setting == "notif":
        # Toggle notifications
        await callback.answer("🔔 Notifications toggled!", show_alert=True)
    
    elif setting == "lang":
        # Show language options
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
                InlineKeyboardButton("🇮🇳 Hindi", callback_data="lang_hi")
            ],
            [InlineKeyboardButton("« Back", callback_data="menu_settings")]
        ])
        
        text = (
            "│  <b>Select Language</b>\n"
            "│\n"
            "│  Choose your preferred language:\n"
        )
        
        response = anime_border(text, "Language")
        await callback.message.edit_text(response, reply_markup=buttons)
```

---

## 🔍 Inline Queries

### File: `assistant/inline_query.py`

```python
"""
Inline query handler for assistant bot
"""

from pyrogram import Client, filters
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import Config
from utils.helpers import anime_border

@Client.on_inline_query()
async def inline_query_handler(client: Client, query: InlineQuery):
    """Handle inline queries"""
    
    # Only allow owner and sudo users
    if query.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    search = query.query.lower()
    
    results = []
    
    # Example 1: Quote result
    if "quote" in search or not search:
        results.append(
            InlineQueryResultArticle(
                title="💙 Anime Quote",
                description="Send a random anime quote",
                input_message_content=InputTextMessageContent(
                    message_text=anime_border(
                        "│  <i>The only ones who should kill are those\n"
                        "│   prepared to be killed.</i>\n"
                        "│\n"
                        "│  — Lelouch\n",
                        "Anime Quote"
                    )
                ),
                thumb_url="https://via.placeholder.com/150/4A90E2/FFFFFF?text=Quote"
            )
        )
    
    # Example 2: Info result
    if "info" in search or not search:
        results.append(
            InlineQueryResultArticle(
                title="ℹ️ Bot Info",
                description="Show bot information",
                input_message_content=InputTextMessageContent(
                    message_text=anime_border(
                        "│  <b>Kaoruko Userbot</b>\n"
                        "│\n"
                        "│  <b>Version:</b> 1.0.0\n"
                        "│  <b>Framework:</b> Pyrogram\n"
                        "│  <b>Theme:</b> Kaoruko Waguri 💙\n",
                        "Bot Information"
                    )
                ),
                thumb_url="https://via.placeholder.com/150/4A90E2/FFFFFF?text=Info"
            )
        )
    
    # Example 3: Help result
    if "help" in search or not search:
        results.append(
            InlineQueryResultArticle(
                title="❓ Help",
                description="Show help message",
                input_message_content=InputTextMessageContent(
                    message_text=anime_border(
                        "│  <b>How to use inline mode:</b>\n"
                        "│\n"
                        "│  Type <code>@yourbotname</code> in any chat\n"
                        "│  Then type your query\n"
                        "│\n"
                        "│  <b>Examples:</b>\n"
                        "│  • quote\n"
                        "│  • info\n"
                        "│  • help\n",
                        "Inline Help"
                    )
                ),
                thumb_url="https://via.placeholder.com/150/4A90E2/FFFFFF?text=Help"
            )
        )
    
    # Example 4: Custom text result
    if search and search not in ["quote", "info", "help"]:
        results.append(
            InlineQueryResultArticle(
                title=f"✨ Say: {search}",
                description=f"Send '{search}' as a message",
                input_message_content=InputTextMessageContent(
                    message_text=anime_border(
                        f"│  {search}\n",
                        "Message"
                    )
                ),
                thumb_url="https://via.placeholder.com/150/4A90E2/FFFFFF?text=Say"
            )
        )
    
    # Answer query
    await query.answer(
        results=results,
        cache_time=1,
        switch_pm_text="Open Bot",
        switch_pm_parameter="start"
    )
```

---

## 🎮 Interactive Features

### File: `assistant/interactive.py`

```python
"""
Interactive features for assistant bot
"""

from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import Config
from utils.helpers import anime_border
import random

# Quiz data
quiz_questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["Tokyo", "Osaka", "Kyoto", "Nagoya"],
        "correct": 0
    },
    {
        "question": "Which anime has the most episodes?",
        "options": ["One Piece", "Naruto", "Bleach", "Dragon Ball"],
        "correct": 0
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct": 1
    }
]

@Client.on_message(filters.command("quiz") & filters.private)
async def quiz_command(client: Client, message: Message):
    """Start a quiz"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    # Select random question
    question = random.choice(quiz_questions)
    q_index = quiz_questions.index(question)
    
    # Create buttons for options
    buttons = []
    for i, option in enumerate(question["options"]):
        buttons.append([
            InlineKeyboardButton(
                option,
                callback_data=f"quiz_{q_index}_{i}"
            )
        ])
    
    markup = InlineKeyboardMarkup(buttons)
    
    text = (
        f"│  <b>Question:</b>\n"
        f"│\n"
        f"│  {question['question']}\n"
        f"│\n"
        f"│  Choose your answer:\n"
    )
    
    response = anime_border(text, "Quiz Time")
    await message.reply_text(response, reply_markup=markup)

@Client.on_callback_query(filters.regex("^quiz_"))
async def quiz_callback(client: Client, callback: CallbackQuery):
    """Handle quiz answers"""
    
    data = callback.data.split("_")
    q_index = int(data[1])
    answer = int(data[2])
    
    question = quiz_questions[q_index]
    correct = question["correct"]
    
    if answer == correct:
        result_text = (
            "│  <b>✅ Correct!</b>\n"
            "│\n"
            "│  Well done! 🎉\n"
        )
    else:
        result_text = (
            "│  <b>❌ Wrong!</b>\n"
            "│\n"
            f"│  Correct answer: {question['options'][correct]}\n"
        )
    
    response = anime_border(result_text, "Quiz Result")
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Try Again", callback_data="quiz_restart")]
    ])
    
    await callback.message.edit_text(response, reply_markup=buttons)
    await callback.answer()

@Client.on_callback_query(filters.regex("^quiz_restart"))
async def quiz_restart(client: Client, callback: CallbackQuery):
    """Restart quiz"""
    
    # Select new question
    question = random.choice(quiz_questions)
    q_index = quiz_questions.index(question)
    
    buttons = []
    for i, option in enumerate(question["options"]):
        buttons.append([
            InlineKeyboardButton(
                option,
                callback_data=f"quiz_{q_index}_{i}"
            )
        ])
    
    markup = InlineKeyboardMarkup(buttons)
    
    text = (
        f"│  <b>Question:</b>\n"
        f"│\n"
        f"│  {question['question']}\n"
        f"│\n"
        f"│  Choose your answer:\n"
    )
    
    response = anime_border(text, "Quiz Time")
    await callback.message.edit_text(response, reply_markup=markup)
    await callback.answer()

# Reminder system
@Client.on_message(filters.command("setreminder") & filters.private)
async def set_reminder(client: Client, message: Message):
    """Set a reminder via bot"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    try:
        args = message.text.split(None, 2)
        minutes = int(args[1])
        reminder_text = args[2]
    except (IndexError, ValueError):
        await message.reply_text(
            "❌ <b>Usage:</b> <code>/setreminder minutes text</code>\n\n"
            "<b>Example:</b> <code>/setreminder 30 Check the oven</code>"
        )
        return
    
    if minutes > 1440:  # 24 hours
        await message.reply_text("❌ Maximum 1440 minutes (24 hours)!")
        return
    
    await message.reply_text(
        f"✅ Reminder set for <b>{minutes}</b> minutes!\n\n"
        f"<i>I'll message you when time's up.</i>"
    )
    
    # Wait and send reminder
    import asyncio
    await asyncio.sleep(minutes * 60)
    
    await message.reply_text(
        f"🔔 <b>Reminder:</b>\n\n{reminder_text}"
    )
```

---

## 🔗 Integration with Userbot

### File: `assistant/userbot_bridge.py`

```python
"""
Bridge between assistant bot and userbot
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from main import bot
from utils.helpers import anime_border

@Client.on_message(filters.command("userstats") & filters.private)
async def user_stats_command(client: Client, message: Message):
    """Get userbot statistics"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    # Access userbot client through bot instance
    try:
        userbot = bot.app
        me = await userbot.get_me()
        
        # Get dialogs
        dialogs = await userbot.get_dialogs()
        
        private = sum(1 for d in dialogs if d.chat.type.name == "PRIVATE")
        groups = sum(1 for d in dialogs if d.chat.type.name in ["GROUP", "SUPERGROUP"])
        channels = sum(1 for d in dialogs if d.chat.type.name == "CHANNEL")
        
        text = (
            f"│  <b>Userbot Statistics</b>\n"
            f"│\n"
            f"│  <b>Name:</b> {me.first_name}\n"
            f"│  <b>Username:</b> @{me.username or 'None'}\n"
            f"│  <b>ID:</b> <code>{me.id}</code>\n"
            f"│\n"
            f"│  <b>Private Chats:</b> {private}\n"
            f"│  <b>Groups:</b> {groups}\n"
            f"│  <b>Channels:</b> {channels}\n"
            f"│  <b>Total:</b> {len(dialogs)}\n"
        )
        
        response = anime_border(text, "Statistics")
        await message.reply_text(response)
        
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

@Client.on_message(filters.command("sendmsg") & filters.private)
async def send_message_command(client: Client, message: Message):
    """Send message through userbot"""
    
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        return
    
    try:
        args = message.text.split(None, 2)
        chat_id = args[1]
        text = args[2]
    except IndexError:
        await message.reply_text(
            "❌ <b>Usage:</b> <code>/sendmsg chat_id text</code>\n\n"
            "<b>Example:</b> <code>/sendmsg me Hello!</code>"
        )
        return
    
    try:
        userbot = bot.app
        await userbot.send_message(chat_id, text)
        await message.reply_text("✅ Message sent successfully!")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
```

---

## 📋 Complete Example Bot File

### File: `assistant/full_example.py`

```python
"""
Complete assistant bot example
Combines all features
"""

from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import Config
from utils.helpers import anime_border

# Command: Start
@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client: Client, message: Message):
    user = message.from_user
    
    if user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        await message.reply_text("❌ Unauthorized!")
        return
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💙 Help", callback_data="help"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings")
        ],
        [
            InlineKeyboardButton("📊 Stats", callback_data="stats"),
            InlineKeyboardButton("🎮 Games", callback_data="games")
        ]
    ])
    
    text = (
        f"│  👋 <b>Welcome, {user.first_name}!</b>\n"
        f"│\n"
        f"│  I'm your Kaoruko Assistant Bot!\n"
        f"│  Click buttons below to explore 💙\n"
    )
    
    await message.reply_text(
        anime_border(text, "Kaoruko Assistant"),
        reply_markup=buttons
    )

# Callbacks
@Client.on_callback_query()
async def callback_handler(client: Client, callback: CallbackQuery):
    data = callback.data
    
    if data == "help":
        text = (
            "│  <b>Available Commands:</b>\n"
            "│\n"
            "│  /start - Main menu\n"
            "│  /help - This help\n"
            "│  /ping - Check status\n"
            "│  /quiz - Start quiz\n"
            "│  /menu - Interactive menu\n"
        )
        
        await callback.message.edit_text(
            anime_border(text, "Help"),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("« Back", callback_data="back")
            ]])
        )
    
    await callback.answer()
```

---

## 🚀 How to Use

### Step 1: Create file in `assistant/` folder
```python
# assistant/myfeature.py
```

### Step 2: Import in main assistant file
```python
# In assistant/inline.py or create new __init__.py
```

### Step 3: Restart bot
```python
# Bot will auto-load new handlers
```

### Step 4: Test in Telegram
```
/start
/menu
/quiz
```

---

**Complete guide for bot development! 🤖💙**