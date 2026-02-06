# 🔌 Plugin Development Guide - Kaoruko Userbot

## 📚 Table of Contents
1. [Basic Plugin Structure](#basic-plugin-structure)
2. [Simple Command Plugin](#simple-command-plugin)
3. [Reply-Based Plugin](#reply-based-plugin)
4. [Database Plugin](#database-plugin)
5. [Multi-Command Plugin](#multi-command-plugin)
6. [Advanced Examples](#advanced-examples)

---

## 🎯 Basic Plugin Structure

### Minimum Required Code:

```python
"""
Plugin description
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config

@Client.on_message(
    filters.command("mycommand", prefixes=Config.CMD_PREFIX) & filters.me
)
async def my_handler(client: Client, message: Message):
    """Handler function"""
    await message.edit("Hello from my plugin!")

# Plugin info (optional but recommended)
__MODULE__ = "My Plugin"
__HELP__ = """
**My Plugin** 🎨

Description here

**Commands:**
• `.mycommand` - Does something

**Examples:**
```
.mycommand
```
"""
```

---

## 📝 Example 1: Simple Command Plugin

### File: `plugins/hello.py`

```python
"""
Simple Hello World Plugin
Shows basic command handling
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import edit_or_reply, anime_border

@Client.on_message(
    filters.command("hello", prefixes=Config.CMD_PREFIX) & filters.me
)
async def hello_command(client: Client, message: Message):
    """Say hello"""
    
    user = await client.get_me()
    
    text = (
        f"│  👋 <b>Hello, {user.first_name}!</b>\n"
        f"│\n"
        f"│  Welcome to Kaoruko Userbot!\n"
        f"│  Have a great day! ✨\n"
    )
    
    response = anime_border(text, "Greeting")
    await edit_or_reply(message, response)

# Plugin info
__MODULE__ = "Hello"
__HELP__ = """
**Hello Plugin** 👋

Simple greeting command!

**Commands:**
• `.hello` - Get a personalized greeting

**Examples:**
```
.hello
```
"""
```

**Usage:**
```
.hello
```

**Output:**
```
╭─「 💙 Greeting 」
│
│  👋 Hello, Ray!
│
│  Welcome to Kaoruko Userbot!
│  Have a great day! ✨
│
╰─「 ✨ Kaoruko Userbot 」
```

---

## 📝 Example 2: Command with Arguments

### File: `plugins/say.py`

```python
"""
Say Plugin - Repeats your text
Shows argument handling
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import edit_or_reply, get_arg

@Client.on_message(
    filters.command("say", prefixes=Config.CMD_PREFIX) & filters.me
)
async def say_command(client: Client, message: Message):
    """Make bot say something"""
    
    # Get text after command
    text = get_arg(message)
    
    if not text:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.say your text here</code>"
        )
        return
    
    # Delete command message
    await message.delete()
    
    # Send the text
    await client.send_message(
        message.chat.id,
        text
    )

@Client.on_message(
    filters.command("saybig", prefixes=Config.CMD_PREFIX) & filters.me
)
async def saybig_command(client: Client, message: Message):
    """Say something in big text"""
    
    text = get_arg(message)
    
    if not text:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.saybig text</code>"
        )
        return
    
    # Convert to big text (aesthetic)
    big_text = " ".join(text)
    
    await message.edit(f"✨ <b>{big_text}</b> ✨")

# Plugin info
__MODULE__ = "Say"
__HELP__ = """
**Say Plugin** 💬

Make the bot say things!

**Commands:**
• `.say <text>` - Send text as new message
• `.saybig <text>` - Send text in big format

**Examples:**
```
.say Hello World
.saybig Kaoruko
```
"""
```

**Usage:**
```
.say Hello everyone!
.saybig HELLO
```

---

## 📝 Example 3: Reply-Based Plugin

### File: `plugins/copy.py`

```python
"""
Copy Plugin - Copy replied messages
Shows reply handling
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import edit_or_reply, get_reply_msg

@Client.on_message(
    filters.command("copy", prefixes=Config.CMD_PREFIX) & filters.me
)
async def copy_command(client: Client, message: Message):
    """Copy a replied message"""
    
    # Get replied message
    reply = get_reply_msg(message)
    
    if not reply:
        await edit_or_reply(
            message,
            "❌ Reply to a message to copy it!"
        )
        return
    
    # Delete command
    await message.delete()
    
    # Copy the message
    if reply.text:
        await client.send_message(
            message.chat.id,
            reply.text
        )
    elif reply.caption:
        # For media with caption
        await reply.copy(message.chat.id)
    else:
        # For media without caption
        await reply.copy(message.chat.id)

@Client.on_message(
    filters.command("reverse", prefixes=Config.CMD_PREFIX) & filters.me
)
async def reverse_command(client: Client, message: Message):
    """Reverse replied text"""
    
    reply = get_reply_msg(message)
    
    if not reply or not reply.text:
        await edit_or_reply(
            message,
            "❌ Reply to a text message!"
        )
        return
    
    # Reverse the text
    reversed_text = reply.text[::-1]
    
    await edit_or_reply(
        message,
        f"🔄 <code>{reversed_text}</code>"
    )

# Plugin info
__MODULE__ = "Copy"
__HELP__ = """
**Copy Plugin** 📋

Copy and manipulate messages!

**Commands:**
• `.copy` - Copy replied message
• `.reverse` - Reverse replied text

**Usage:**
```
(Reply to a message)
.copy

(Reply to text)
.reverse
```
"""
```

---

## 📝 Example 4: Database Plugin

### File: `plugins/notes.py`

```python
"""
Notes Plugin - Save and retrieve notes
Shows database usage
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import edit_or_reply, anime_border, get_arg
from main import bot

@Client.on_message(
    filters.command("savenote", prefixes=Config.CMD_PREFIX) & filters.me
)
async def save_note_command(client: Client, message: Message):
    """Save a note"""
    
    # Get note name and content
    try:
        args = message.text.split(None, 2)
        note_name = args[1]
        note_content = args[2]
    except IndexError:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.savenote name content</code>"
        )
        return
    
    # Save to database
    chat_id = message.chat.id
    await bot.db.add_note(chat_id, note_name, note_content)
    
    await edit_or_reply(
        message,
        f"✅ Note <code>{note_name}</code> saved!"
    )

@Client.on_message(
    filters.command("getnote", prefixes=Config.CMD_PREFIX) & filters.me
)
async def get_note_command(client: Client, message: Message):
    """Get a saved note"""
    
    note_name = get_arg(message)
    
    if not note_name:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.getnote name</code>"
        )
        return
    
    # Get from database
    chat_id = message.chat.id
    note = await bot.db.get_note(chat_id, note_name)
    
    if not note:
        await edit_or_reply(
            message,
            f"❌ Note <code>{note_name}</code> not found!"
        )
        return
    
    await edit_or_reply(message, note['content'])

@Client.on_message(
    filters.command("notes", prefixes=Config.CMD_PREFIX) & filters.me
)
async def list_notes_command(client: Client, message: Message):
    """List all notes in chat"""
    
    chat_id = message.chat.id
    notes = await bot.db.get_all_notes(chat_id)
    
    if not notes:
        await edit_or_reply(
            message,
            "❌ No notes saved in this chat!"
        )
        return
    
    # Create list
    note_list = []
    for i, note in enumerate(notes, 1):
        note_list.append(f"│  {i}. <code>{note['name']}</code>")
    
    text = "\n".join(note_list)
    response = anime_border(text, f"Notes ({len(notes)})")
    
    await edit_or_reply(message, response)

@Client.on_message(
    filters.command("delnote", prefixes=Config.CMD_PREFIX) & filters.me
)
async def delete_note_command(client: Client, message: Message):
    """Delete a note"""
    
    note_name = get_arg(message)
    
    if not note_name:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.delnote name</code>"
        )
        return
    
    chat_id = message.chat.id
    deleted = await bot.db.delete_note(chat_id, note_name)
    
    if deleted:
        await edit_or_reply(
            message,
            f"✅ Note <code>{note_name}</code> deleted!"
        )
    else:
        await edit_or_reply(
            message,
            f"❌ Note <code>{note_name}</code> not found!"
        )

# Plugin info
__MODULE__ = "Notes"
__HELP__ = """
**Notes Plugin** 📝

Save and retrieve notes per chat!

**Commands:**
• `.savenote <name> <content>` - Save a note
• `.getnote <name>` - Get a note
• `.notes` - List all notes
• `.delnote <name>` - Delete a note

**Examples:**
```
.savenote greeting Hello everyone!
.getnote greeting
.notes
.delnote greeting
```
"""
```

---

## 📝 Example 5: Timer Plugin (Async Operations)

### File: `plugins/timer.py`

```python
"""
Timer Plugin - Set timers and reminders
Shows async operations
"""

import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import edit_or_reply

@Client.on_message(
    filters.command("timer", prefixes=Config.CMD_PREFIX) & filters.me
)
async def timer_command(client: Client, message: Message):
    """Set a timer"""
    
    try:
        seconds = int(message.text.split()[1])
    except (IndexError, ValueError):
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.timer seconds</code>"
        )
        return
    
    if seconds > 300:
        await edit_or_reply(
            message,
            "❌ Maximum 300 seconds (5 minutes)!"
        )
        return
    
    msg = await edit_or_reply(
        message,
        f"⏰ Timer set for <b>{seconds}</b> seconds!"
    )
    
    # Wait
    await asyncio.sleep(seconds)
    
    # Alert
    await msg.edit("🔔 <b>Time's up!</b>")
    
    # Optionally delete after 5 seconds
    await asyncio.sleep(5)
    await msg.delete()

@Client.on_message(
    filters.command("remind", prefixes=Config.CMD_PREFIX) & filters.me
)
async def remind_command(client: Client, message: Message):
    """Set a reminder"""
    
    try:
        args = message.text.split(None, 2)
        seconds = int(args[1])
        reminder_text = args[2]
    except (IndexError, ValueError):
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.remind seconds text</code>"
        )
        return
    
    if seconds > 3600:
        await edit_or_reply(
            message,
            "❌ Maximum 3600 seconds (1 hour)!"
        )
        return
    
    await edit_or_reply(
        message,
        f"✅ Reminder set for <b>{seconds}</b> seconds!"
    )
    
    # Wait
    await asyncio.sleep(seconds)
    
    # Send reminder
    await client.send_message(
        message.chat.id,
        f"🔔 <b>Reminder:</b>\n\n{reminder_text}"
    )

# Plugin info
__MODULE__ = "Timer"
__HELP__ = """
**Timer Plugin** ⏰

Set timers and reminders!

**Commands:**
• `.timer <seconds>` - Set a timer
• `.remind <seconds> <text>` - Set a reminder

**Limits:**
• Timer: Max 300 seconds (5 min)
• Reminder: Max 3600 seconds (1 hour)

**Examples:**
```
.timer 60
.remind 300 Check the oven
```
"""
```

---

## 📝 Example 6: Interactive Plugin (Buttons)

### File: `plugins/poll.py`

```python
"""
Poll Plugin - Create simple polls
Shows message manipulation
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import edit_or_reply, anime_border

@Client.on_message(
    filters.command("poll", prefixes=Config.CMD_PREFIX) & filters.me
)
async def poll_command(client: Client, message: Message):
    """Create a simple poll"""
    
    try:
        args = message.text.split(None, 1)[1]
        parts = args.split("|")
        
        question = parts[0].strip()
        options = [opt.strip() for opt in parts[1:]]
        
        if len(options) < 2:
            raise ValueError("Need at least 2 options")
            
    except (IndexError, ValueError):
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b>\n"
            "<code>.poll Question | Option1 | Option2 | Option3</code>"
        )
        return
    
    # Create poll text
    poll_text = f"<b>📊 {question}</b>\n\n"
    
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    
    for i, option in enumerate(options[:10]):
        poll_text += f"{emojis[i]} {option}\n"
    
    poll_text += "\n<i>React with emoji to vote!</i>"
    
    await message.edit(poll_text)

# Plugin info
__MODULE__ = "Poll"
__HELP__ = """
**Poll Plugin** 📊

Create simple text polls!

**Commands:**
• `.poll Question | Opt1 | Opt2 | ...` - Create poll

**Examples:**
```
.poll Best anime? | Naruto | One Piece | Bleach
.poll Pizza toppings? | Pepperoni | Mushrooms | Olives
```

**Note:** Max 10 options
"""
```

---

## 🎨 Template for New Plugins

### File: `plugins/_template.py`

```python
"""
Plugin Name - Short description
Detailed description here
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import (
    edit_or_reply,
    anime_border,
    info_box,
    get_arg,
    get_reply_msg
)

# Import database if needed
# from main import bot

@Client.on_message(
    filters.command("commandname", prefixes=Config.CMD_PREFIX) & filters.me
)
async def command_handler(client: Client, message: Message):
    """
    Command description
    
    Args:
        client: Pyrogram client
        message: Message object
    """
    
    # Your code here
    await edit_or_reply(message, "Hello from template!")

# Add more commands as needed

# Plugin info (REQUIRED)
__MODULE__ = "Plugin Name"
__HELP__ = """
**Plugin Name** 🎨

Description of what the plugin does

**Commands:**
• `.command1` - Description
• `.command2 <arg>` - Description

**Examples:**
```
.command1
.command2 argument
```

**Notes:**
• Additional info
• Usage tips
"""
```

---

## 📋 Plugin Development Checklist

✅ **File Location:** `plugins/your_plugin.py`  
✅ **Imports:** Pyrogram, Config, Helpers  
✅ **Decorators:** `@Client.on_message()`  
✅ **Filters:** `filters.me` for userbot  
✅ **Error Handling:** Try-except blocks  
✅ **Help Text:** `__MODULE__` and `__HELP__`  
✅ **Anime Styling:** Use helper functions  
✅ **Testing:** Test before loading  

---

## 🚀 How to Use Your Plugin

### Step 1: Create Plugin File
```powershell
# In plugins/ directory
notepad plugins/myplugin.py
```

### Step 2: Write Code
Use examples above as reference

### Step 3: Load Plugin
```
.load myplugin
```

### Step 4: Test
```
.yourcommand
```

### Step 5: Debug if Needed
```
.reload myplugin
```

---

## 💡 Pro Tips

1. **Start Simple:** Begin with basic commands
2. **Use Helpers:** Leverage `utils/helpers.py` functions
3. **Error Handling:** Always handle exceptions
4. **User Feedback:** Give clear success/error messages
5. **Documentation:** Write good `__HELP__` text
6. **Testing:** Test in Saved Messages first
7. **Database:** Use MongoDB for persistence
8. **Async:** Use `await` for async operations
9. **Styling:** Use anime borders for beauty
10. **Modular:** One responsibility per plugin

---

**Happy Plugin Development! 💙✨**