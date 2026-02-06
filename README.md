# 💙 Kaoruko Userbot

<div align="center">

![Kaoruko](https://img.shields.io/badge/Kaoruko-Userbot-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0+-blue?style=for-the-badge)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green?style=for-the-badge&logo=mongodb)

**A beautiful anime-themed Telegram userbot inspired by Kaoruko Waguri**

*Fast • Elegant • Feature-rich*

</div>

---

## ✨ Features

### 🎨 **Aesthetic Design**
- Beautiful blue anime theme inspired by Kaoruko Waguri
- Elegant message formatting with custom borders
- Clean and intuitive interface

### 🔌 **Plugin System**
- Dynamic plugin loading/unloading
- No restart required for plugin management
- Easy to extend with custom plugins
- Hot-reload support

### 💤 **AFK Module**
- Auto-reply to mentions when away
- Support for custom reasons and media
- Beautiful anime-styled responses
- Mention counter
- MongoDB persistence

### 🤖 **Assistant Bot**
- Inline button menus
- Settings management
- Statistics display
- Beautiful UI with callbacks

### 💾 **Database**
- MongoDB for persistent storage
- Async operations
- Efficient data management
- Easy to query and update

### ⚡ **Performance**
- Built with Pyrogram (fast MTProto library)
- Async/await architecture
- Optimized for speed
- Low resource usage

---

## 📋 Requirements

- Python 3.9 or higher
- MongoDB (local or cloud)
- Telegram API credentials
- A Telegram account

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/kaoruko-userbot.git
cd kaoruko-userbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup MongoDB

**Option A: Local MongoDB**
```bash
# Install MongoDB
sudo apt install mongodb

# Start MongoDB service
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

**Option B: MongoDB Atlas (Cloud)**
1. Go to https://www.mongodb.com/cloud/atlas
2. Create a free cluster
3. Get your connection string
4. Use it in your `.env` file

### 4. Get API Credentials

1. Go to https://my.telegram.org
2. Login with your phone number
3. Click on "API Development Tools"
4. Create a new application
5. Note down your `API_ID` and `API_HASH`

### 5. Get Bot Token

1. Open Telegram and search for @BotFather
2. Send `/newbot` and follow instructions
3. Note down your bot token

### 6. Generate Session String

```bash
python3 generate_session.py
```

Follow the prompts and save the session string.

### 7. Configure Environment

```bash
cp .env.example .env
nano .env  # or use any text editor
```

Fill in your details:
```env
API_ID=your_api_id
API_HASH=your_api_hash
SESSION_STRING=your_session_string
BOT_TOKEN=your_bot_token
MONGO_URI=mongodb://localhost:27017
OWNER_ID=your_user_id
```

### 8. Run the Userbot

```bash
python3 main.py
```

---

## 📚 Commands

### 💙 Basic Commands

| Command | Description |
|---------|-------------|
| `.ping` | Check bot response time |
| `.alive` | Check if bot is running |
| `.help [plugin]` | Show help message |
| `.stats` | Show user statistics |
| `.id` | Get chat/user ID |
| `.purge` | Delete messages in bulk (reply) |
| `.del` | Delete a message (reply) |

### 💤 AFK Module

| Command | Description |
|---------|-------------|
| `.afk [reason]` | Set AFK with optional reason |
| `.afk` (reply to media) | Set AFK with media |

**Auto Features:**
- Replies to mentions when AFK
- Removes AFK when you send a message
- Tracks mention count
- Shows AFK duration

### 🔌 Plugin Manager

| Command | Description |
|---------|-------------|
| `.plugins` | List all available plugins |
| `.load <name>` | Load a plugin |
| `.unload <name>` | Unload a plugin |
| `.reload <name>` | Reload a plugin |

---

## 🎨 Customization

### Theme Colors

Edit `config.py` to change theme colors:

```python
THEME_COLOR = "#4A90E2"  # Main blue
ACCENT_COLOR = "#7CB9E8"  # Light blue
```

### Command Prefix

Change the command prefix in `.env`:

```env
CMD_PREFIX=.  # Default
# or
CMD_PREFIX=!
CMD_PREFIX=/
```

### Adding Custom Plugins

Create a new file in `plugins/` directory:

```python
# plugins/my_plugin.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from utils.helpers import edit_or_reply, anime_border

@Client.on_message(
    filters.command("mycommand", prefixes=Config.CMD_PREFIX) & filters.me
)
async def my_command(client: Client, message: Message):
    """Your custom command"""
    
    response = anime_border(
        "│  Your custom response here\n",
        "My Plugin"
    )
    
    await edit_or_reply(message, response)

# Plugin info
__MODULE__ = "My Plugin"
__HELP__ = """
**My Plugin** 🎨

Description of your plugin

**Commands:**
• `.mycommand` - Does something cool

**Examples:**
```
.mycommand
```
"""
```

Then load it: `.load my_plugin`

---

## 🗂️ Project Structure

```
kaoruko-userbot/
├── main.py                 # Main entry point
├── config.py               # Configuration
├── requirements.txt        # Dependencies
├── generate_session.py     # Session generator
├── .env.example           # Environment template
├── utils/
│   ├── logger.py          # Colored logging
│   ├── database.py        # MongoDB manager
│   └── helpers.py         # Helper functions
├── plugins/
│   ├── afk.py            # AFK module
│   ├── basic.py          # Basic commands
│   └── plugin_manager.py # Plugin management
└── assistant/
    └── inline.py         # Assistant bot handlers
```

---

## 🛡️ Security

### ⚠️ Important Warnings

1. **Never share your SESSION_STRING** - It gives full access to your account
2. **Keep your .env file private** - Add it to .gitignore
3. **Use at your own risk** - Userbots violate Telegram ToS
4. **Recommended**: Use a secondary account
5. **Be careful with sudo users** - They have elevated privileges

### 🔒 Best Practices

- Don't run untrusted plugins
- Review plugin code before loading
- Keep your dependencies updated
- Use strong MongoDB passwords
- Enable MongoDB authentication
- Use firewall rules for MongoDB

---

## 🐛 Troubleshooting

### MongoDB Connection Error

```bash
# Check if MongoDB is running
sudo systemctl status mongodb

# Start MongoDB
sudo systemctl start mongodb

# Check connection
mongosh
```

### Session String Invalid

```bash
# Generate a new session string
python3 generate_session.py
```

### Plugin Not Loading

```bash
# Check plugin syntax
python3 -m py_compile plugins/your_plugin.py

# Reload the plugin
.reload your_plugin
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

---

## 📝 To-Do

- [ ] Add more plugins
- [ ] Web dashboard
- [ ] Redis support
- [ ] Media downloader
- [ ] Auto-responder
- [ ] Custom filters
- [ ] Notes system
- [ ] Tag system
- [ ] Anti-spam features
- [ ] Backup/restore system

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## ⚠️ Disclaimer

This userbot is for educational purposes only. Using userbots violates Telegram's Terms of Service and may result in account termination. Use at your own risk. The developers are not responsible for any misuse or damage caused by this software.

**We strongly recommend:**
- Using a secondary account
- Not using this for spam or abuse
- Being respectful of others
- Following all applicable laws

---

## 💙 Credits

- **Theme**: Inspired by Kaoruko Waguri
- **Framework**: [Pyrogram](https://docs.pyrogram.org/)
- **Database**: [MongoDB](https://www.mongodb.com/)
- **Developer**: Made with 💙

---

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Discussions**: Use GitHub Discussions
- **Updates**: Watch the repository for updates

---

<div align="center">

**Made with 💙 by anime enthusiasts**

*Kaoruko Userbot © 2026*

</div>
