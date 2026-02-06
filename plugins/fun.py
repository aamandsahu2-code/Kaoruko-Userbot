"""
Fun Commands Plugin for Kaoruko Userbot
Anime-themed fun and entertainment commands 💙
"""

import random
from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import edit_or_reply, anime_border, info_box

# Anime quotes database
ANIME_QUOTES = [
    "The only ones who should kill are those prepared to be killed. - Lelouch",
    "People's lives don't end when they die. It ends when they lose faith. - Itachi",
    "If you don't like your destiny, don't accept it. - Naruto",
    "Hard work betrays none, but dreams betray many. - Hachiman",
    "Whatever you lose, you'll find it again. But what you throw away, you'll never get back. - Kenshin",
    "A lesson without pain is meaningless. - Edward Elric",
    "The world isn't perfect, but it's there for us trying the best it can. - Roy Mustang",
    "I'll leave tomorrow's problems to tomorrow's me. - Saitama",
    "If you can't find a reason to fight, then you shouldn't be fighting. - Akame",
    "The ticket to the future is always open. - Vash",
]

KAOMOJIS = [
    "(｡♥‿♥｡)", "( ´ ▽ ` )", "(◕‿◕✿)", "(づ｡◕‿‿◕｡)づ",
    "ヾ(⌐■_■)ノ♪", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "( ͡° ͜ʖ ͡°)", "(╯°□°）╯︵ ┻━┻",
    "¯\\_(ツ)_/¯", "(｀・ω・´)", "(=^･ω･^=)", "(ﾉ´ヮ`)ﾉ*: ･ﾟ",
    "( •̀ ω •́ )✧", "(｡◕‿◕｡)", "ʕ•ᴥ•ʔ", "(◠‿◠)"
]

@Client.on_message(
    filters.command("quote", prefixes=Config.CMD_PREFIX) & filters.me
)
async def anime_quote(client: Client, message: Message):
    """Get a random anime quote"""
    
    quote = random.choice(ANIME_QUOTES)
    
    response = anime_border(
        f"│  <i>{quote}</i>\n",
        "Anime Quote"
    )
    
    await edit_or_reply(message, response)

@Client.on_message(
    filters.command("kaomoji", prefixes=Config.CMD_PREFIX) & filters.me
)
async def random_kaomoji(client: Client, message: Message):
    """Get a random kaomoji"""
    
    kaomoji = random.choice(KAOMOJIS)
    
    await edit_or_reply(message, f"💙 {kaomoji}")

@Client.on_message(
    filters.command("aesthetic", prefixes=Config.CMD_PREFIX) & filters.me
)
async def aesthetic_text(client: Client, message: Message):
    """Convert text to aesthetic format"""
    
    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.aesthetic text</code>"
        )
        return
    
    # Aesthetic conversion
    aesthetic = " ".join(text)
    
    response = f"✨ <code>{aesthetic}</code> ✨"
    
    await edit_or_reply(message, response)

@Client.on_message(
    filters.command("typewriter", prefixes=Config.CMD_PREFIX) & filters.me
)
async def typewriter_effect(client: Client, message: Message):
    """Typewriter effect"""
    
    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        text = "Kaoruko Userbot 💙"
    
    msg = await edit_or_reply(message, "✍️")
    
    display = ""
    for char in text:
        display += char
        await msg.edit(f"✍️ {display}")
        await asyncio.sleep(0.1)
    
    await msg.edit(f"✨ {display}")

@Client.on_message(
    filters.command("countdown", prefixes=Config.CMD_PREFIX) & filters.me
)
async def countdown_command(client: Client, message: Message):
    """Countdown timer"""
    
    try:
        seconds = int(message.text.split()[1])
    except (IndexError, ValueError):
        seconds = 5
    
    if seconds > 60:
        await edit_or_reply(message, "❌ Maximum 60 seconds!")
        return
    
    msg = await edit_or_reply(message, f"⏳ Starting countdown from {seconds}...")
    
    for i in range(seconds, 0, -1):
        await msg.edit(f"⏳ <b>{i}</b>")
        await asyncio.sleep(1)
    
    await msg.edit("🎉 <b>Time's up!</b>")

@Client.on_message(
    filters.command("love", prefixes=Config.CMD_PREFIX) & filters.me
)
async def love_calculator(client: Client, message: Message):
    """Calculate love percentage"""
    
    try:
        names = message.text.split(None, 1)[1]
        name1, name2 = names.split("&")
        name1 = name1.strip()
        name2 = name2.strip()
    except:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.love Name1 & Name2</code>"
        )
        return
    
    # Generate "random" but consistent percentage
    seed = sum(ord(c) for c in name1 + name2)
    random.seed(seed)
    percentage = random.randint(1, 100)
    
    if percentage < 30:
        emoji = "💔"
        status = "Not Compatible"
    elif percentage < 60:
        emoji = "💛"
        status = "Maybe?"
    elif percentage < 80:
        emoji = "❤️"
        status = "Good Match"
    else:
        emoji = "💕"
        status = "Perfect Match"
    
    response = info_box(
        "Love Calculator",
        {
            "Person 1": name1,
            "Person 2": name2,
            "Love": f"{percentage}% {emoji}",
            "Status": status
        }
    )
    
    await edit_or_reply(message, response)

@Client.on_message(
    filters.command("flip", prefixes=Config.CMD_PREFIX) & filters.me
)
async def flip_coin(client: Client, message: Message):
    """Flip a coin"""
    
    msg = await edit_or_reply(message, "🪙 <i>Flipping...</i>")
    
    await asyncio.sleep(1)
    
    result = random.choice(["Heads", "Tails"])
    emoji = "👑" if result == "Heads" else "🔄"
    
    await msg.edit(f"{emoji} <b>{result}!</b>")

@Client.on_message(
    filters.command("roll", prefixes=Config.CMD_PREFIX) & filters.me
)
async def roll_dice(client: Client, message: Message):
    """Roll a dice"""
    
    try:
        sides = int(message.text.split()[1])
    except:
        sides = 6
    
    if sides > 100:
        await edit_or_reply(message, "❌ Maximum 100 sides!")
        return
    
    msg = await edit_or_reply(message, "🎲 <i>Rolling...</i>")
    
    await asyncio.sleep(1)
    
    result = random.randint(1, sides)
    
    await msg.edit(f"🎲 <b>{result}</b> (1-{sides})")

@Client.on_message(
    filters.command("choose", prefixes=Config.CMD_PREFIX) & filters.me
)
async def choose_option(client: Client, message: Message):
    """Choose between options"""
    
    try:
        options_text = message.text.split(None, 1)[1]
        options = [opt.strip() for opt in options_text.split(",")]
    except:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.choose option1, option2, option3</code>"
        )
        return
    
    if len(options) < 2:
        await edit_or_reply(message, "❌ Need at least 2 options!")
        return
    
    msg = await edit_or_reply(message, "🤔 <i>Thinking...</i>")
    
    await asyncio.sleep(1)
    
    choice = random.choice(options)
    
    response = anime_border(
        f"│  <b>I choose:</b> <code>{choice}</code>\n",
        "Decision Made"
    )
    
    await msg.edit(response)

# Import asyncio for delays
import asyncio

# Plugin info
__MODULE__ = "Fun"
__HELP__ = """
**Fun Commands** 🎮

Entertainment and anime-themed fun commands!

**Commands:**
• `.quote` - Random anime quote
• `.kaomoji` - Random kaomoji face
• `.aesthetic <text>` - Aesthetic text
• `.typewriter <text>` - Typewriter effect
• `.countdown [seconds]` - Countdown timer
• `.love Name1 & Name2` - Love calculator
• `.flip` - Flip a coin
• `.roll [sides]` - Roll a dice
• `.choose opt1, opt2, ...` - Choose randomly

**Examples:**
```
.quote
.kaomoji
.aesthetic Kaoruko
.typewriter Hello World
.countdown 10
.love Alice & Bob
.flip
.roll 20
.choose Pizza, Burger, Sushi
```
"""
