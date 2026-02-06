# 💙 Kaoruko Userbot - Complete Command Reference

## 📚 Table of Contents
1. [Basic Commands](#basic-commands)
2. [AFK Module](#afk-module)
3. [Plugin Manager](#plugin-manager)
4. [Fun Commands](#fun-commands)
5. [Message Management](#message-management)
6. [Assistant Bot](#assistant-bot)

---

## 🎯 Basic Commands

### `.ping`
**Description:** Check bot's response time  
**Usage:** `.ping`  
**Example:**
```
.ping
```
**Output:**
```
╭─「 💙 Pong! 」
│
│  Response Time: 45.23ms
│  Status: Online
│  Version: 1.0.0
│
╰─「 ✨ Kaoruko Userbot 」
```

---

### `.alive`
**Description:** Check if bot is running  
**Usage:** `.alive`  
**Example:**
```
.alive
```
**Output:**
```
╭─「 💙 System Status 」
│
│  Bot: Kaoruko
│  Version: 1.0.0
│  Status: Online
│  Theme: Kaoruko Waguri 💙
│
╰─「 ✨ Kaoruko Userbot 」
```

---

### `.help [plugin]`
**Description:** Show help menu or plugin-specific help  
**Usage:** 
- `.help` - Show general help
- `.help plugin_name` - Show specific plugin help

**Examples:**
```
.help
.help afk
.help fun
.help basic
```

---

### `.stats`
**Description:** Show your Telegram statistics  
**Usage:** `.stats`  
**Example:**
```
.stats
```
**Output:**
```
╭─「 💙 Statistics 」
│
│  Name: Your Name
│  Username: @yourusername
│  User ID: 123456789
│  Private Chats: 45
│  Groups: 23
│  Channels: 12
│  Bots: 8
│  Total: 88
│
╰─「 ✨ Kaoruko Userbot 」
```

---

### `.id`
**Description:** Get chat or user ID  
**Usage:** 
- `.id` - Get current chat ID
- `.id` (reply to message) - Get user ID

**Examples:**
```
.id
.id (reply to someone's message)
```

---

## 💤 AFK Module

### `.afk [reason]`
**Description:** Set yourself as Away From Keyboard  
**Usage:** 
- `.afk` - Set AFK without reason
- `.afk reason` - Set AFK with reason
- `.afk` (reply to media) - Set AFK with media

**Examples:**
```
.afk
.afk Going to sleep 😴
.afk Working on something important
.afk Lunch break
.afk Be back in 30 mins
```

**With Media:**
```
(Reply to a photo/video/GIF)
.afk Away for a while
```

**Features:**
- ✅ Auto-replies to mentions
- ✅ Shows AFK duration
- ✅ Counts mentions
- ✅ Supports photos/videos/GIFs
- ✅ Automatically removes when you send a message

**Auto-Reply Example:**
When someone mentions you:
```
╭─「 💙 User is AFK 」
│
│  User: @yourusername
│  Status: AFK
│  Since: 2 hours, 30 minutes
│  Reason: Going to sleep 😴
│
╰─「 ✨ Kaoruko Userbot 」
```

**Return Message:**
```
╭─「 💙 Welcome Back 」
│
│  Status: Back Online
│  AFK Duration: 2 hours, 30 minutes
│  Mentions: 15
│
╰─「 ✨ Kaoruko Userbot 」
```

---

## 🔌 Plugin Manager

### `.plugins`
**Description:** List all available plugins  
**Usage:** `.plugins`  
**Example:**
```
.plugins
```
**Output:**
```
╭─「 💙 Plugins (4) 」
│
│  1. ✅ afk
│  2. ✅ basic
│  3. ✅ plugin_manager
│  4. ✅ fun
│
╰─「 ✨ Kaoruko Userbot 」
```
*✅ = Loaded, ❌ = Not loaded*

---

### `.load <plugin_name>`
**Description:** Load a plugin dynamically  
**Usage:** `.load plugin_name`  
**Examples:**
```
.load afk
.load fun
.load basic
```

---

### `.unload <plugin_name>`
**Description:** Unload a plugin  
**Usage:** `.unload plugin_name`  
**Examples:**
```
.unload afk
.unload fun
```

---

### `.reload <plugin_name>`
**Description:** Reload a plugin (unload + load)  
**Usage:** `.reload plugin_name`  
**Examples:**
```
.reload afk
.reload fun
```

---

## 🎮 Fun Commands

### `.quote`
**Description:** Get a random anime quote  
**Usage:** `.quote`  
**Example:**
```
.quote
```
**Output:**
```
╭─「 💙 Anime Quote 」
│
│  "The only ones who should kill are those 
│   prepared to be killed." - Lelouch
│
╰─「 ✨ Kaoruko Userbot 」
```

---

### `.kaomoji`
**Description:** Get a random Japanese emoticon  
**Usage:** `.kaomoji`  
**Example:**
```
.kaomoji
```
**Output:**
```
💙 (｡♥‿♥｡)
💙 ( ´ ▽ ` )
💙 ヾ(⌐■_■)ノ♪
```

---

### `.aesthetic <text>`
**Description:** Convert text to aesthetic format  
**Usage:** `.aesthetic text`  
**Examples:**
```
.aesthetic Kaoruko
.aesthetic Hello World
.aesthetic Anime Lover
```
**Output:**
```
✨ K a o r u k o ✨
✨ H e l l o   W o r l d ✨
```

---

### `.typewriter <text>`
**Description:** Display text with typewriter animation  
**Usage:** `.typewriter text`  
**Examples:**
```
.typewriter Hello World
.typewriter Kaoruko Userbot
```
**Effect:**
Shows text appearing character by character with animation.

---

### `.countdown [seconds]`
**Description:** Start a countdown timer  
**Usage:** 
- `.countdown` - 5 second countdown (default)
- `.countdown seconds` - Custom countdown

**Examples:**
```
.countdown
.countdown 10
.countdown 30
```
**Max:** 60 seconds

---

### `.love Name1 & Name2`
**Description:** Calculate love percentage between two names  
**Usage:** `.love Name1 & Name2`  
**Examples:**
```
.love Alice & Bob
.love Romeo & Juliet
.love Kaoruko & Anime
```
**Output:**
```
╭─「 💙 Love Calculator 」
│
│  Person 1: Alice
│  Person 2: Bob
│  Love: 87% 💕
│  Status: Perfect Match
│
╰─「 ✨ Kaoruko Userbot 」
```

**Status Levels:**
- 💔 Not Compatible (< 30%)
- 💛 Maybe? (30-59%)
- ❤️ Good Match (60-79%)
- 💕 Perfect Match (80-100%)

---

### `.flip`
**Description:** Flip a coin  
**Usage:** `.flip`  
**Example:**
```
.flip
```
**Output:**
```
👑 Heads!
🔄 Tails!
```

---

### `.roll [sides]`
**Description:** Roll a dice  
**Usage:** 
- `.roll` - Roll 6-sided dice (default)
- `.roll sides` - Roll custom dice

**Examples:**
```
.roll
.roll 20
.roll 100
```
**Max:** 100 sides

---

### `.choose option1, option2, option3`
**Description:** Choose randomly from options  
**Usage:** `.choose option1, option2, option3, ...`  
**Examples:**
```
.choose Pizza, Burger, Sushi
.choose Yes, No, Maybe
.choose Red, Blue, Green, Yellow
.choose Study, Sleep, Game
```
**Output:**
```
╭─「 💙 Decision Made 」
│
│  I choose: Pizza
│
╰─「 ✨ Kaoruko Userbot 」
```

---

## 🗑️ Message Management

### `.purge`
**Description:** Delete multiple messages at once  
**Usage:** `.purge` (reply to a message)  
**Example:**
```
(Reply to the first message you want to delete)
.purge
```
**Effect:** Deletes all messages from the replied message to your purge command.

**Output:**
```
✅ Purged 45 messages!
```
*(Auto-deletes after 3 seconds)*

---

### `.del`
**Description:** Delete a single message  
**Usage:** 
- `.del` - Delete your own message
- `.del` (reply) - Delete replied message

**Examples:**
```
.del
(Reply to someone's message)
.del
```

---

## 🤖 Assistant Bot Commands

*(Works in bot's private chat)*

### `/start`
**Description:** Start the assistant bot  
**Usage:** `/start`  
**Features:**
- 💙 Help menu
- ⚙️ Settings
- 📊 Statistics
- 🔌 Plugins
- ✨ About

**Interactive Buttons:**
All features accessible through beautiful inline button menus.

---

## 📝 Command Examples by Use Case

### Daily Usage
```bash
.ping              # Check bot status
.alive             # Confirm it's running
.stats             # View your stats
```

### Going Away
```bash
.afk Sleeping      # Set AFK
# Bot auto-replies to mentions
# Send any message to remove AFK
```

### Having Fun
```bash
.quote             # Inspirational quote
.kaomoji           # Random emoticon
.flip              # Decision making
.love Me & Anime   # Fun calculator
```

### Managing Messages
```bash
.purge             # Clean up spam
.del               # Delete single message
```

### Plugin Management
```bash
.plugins           # See all plugins
.load fun          # Load fun commands
.unload fun        # Unload if not needed
.reload afk        # Restart AFK module
```

---

## ⚙️ Advanced Usage

### Combining Commands
```bash
# Set AFK with aesthetic text
.aesthetic Going Away | Copy the output
.afk [paste aesthetic text]
```

### Custom Prefix
You can change command prefix in `.env`:
```env
CMD_PREFIX=!
```
Then use:
```
!ping
!alive
!afk
```

---

## 🎨 Command Formatting Tips

### Using Markdown
Commands support HTML formatting:
```
.afk <b>Bold text</b>
.afk <i>Italic text</i>
.afk <code>Monospace</code>
```

### Emojis
```
.afk Going to sleep 😴💤
.afk Working hard 💼💪
.afk Gaming time 🎮🎯
```

---

## 📊 Command Categories Summary

| Category | Commands | Description |
|----------|----------|-------------|
| **Basic** | 6 commands | Essential utilities |
| **AFK** | 1 command | Away system |
| **Plugins** | 4 commands | Plugin management |
| **Fun** | 8 commands | Entertainment |
| **Messages** | 2 commands | Message management |
| **Assistant** | 1 command | Bot interface |

**Total: 22+ Commands** 🎉

---

## 🔧 Command Syntax Guide

### Basic Format
```
.command [required_argument] <optional_argument>
```

### Reply-Based Commands
```
(Reply to a message first)
.command
```

### Multi-Argument Commands
```
.command arg1, arg2, arg3
.command arg1 & arg2
```

---

## 💡 Pro Tips

1. **Quick Access**: Pin frequently used commands in Saved Messages
2. **Aliases**: Create notes with common command combinations
3. **Shortcuts**: Use bot's command history (↑ arrow in Telegram)
4. **Testing**: Try commands in Saved Messages first
5. **Help**: Use `.help plugin_name` for detailed info

---

## 🆘 Command Not Working?

1. Check prefix (default is `.`)
2. Verify plugin is loaded (`.plugins`)
3. Check for typos
4. Use `.help` for correct syntax
5. Reload plugin if needed (`.reload plugin_name`)

---

## 🌟 Coming Soon

Future command additions:
- Media downloader
- Auto-responder
- Custom filters
- Notes system
- Tag system
- Group management
- And more!

---

**Made with 💙 by Kaoruko Userbot**

*Command Prefix: `.` (customizable)*  
*Total Commands: 22+*  
*Version: 1.0.0*