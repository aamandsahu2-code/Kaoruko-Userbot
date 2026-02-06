# 📁 Kaoruko Userbot - Project Structure

```
kaoruko-userbot/
│
├── 📄 main.py                      # Main entry point - starts the userbot
├── 📄 config.py                    # Configuration and settings
├── 📄 generate_session.py          # Session string generator script
├── 📄 setup.sh                     # Automated setup script
├── 📄 requirements.txt             # Python dependencies
│
├── 📄 .env.example                 # Environment variables template
├── 📄 .gitignore                   # Git ignore rules
├── 📄 LICENSE                      # MIT License
│
├── 📚 Documentation/
│   ├── 📄 README.md                # Complete documentation
│   ├── 📄 QUICKSTART.md            # Quick start guide
│   ├── 📄 FEATURES.md              # Feature list
│   └── 📄 STRUCTURE.txt            # This file
│
├── 🔧 utils/                       # Utility modules
│   ├── 📄 __init__.py              # Package initializer
│   ├── 📄 logger.py                # Beautiful colored logging
│   ├── 📄 database.py              # MongoDB database manager
│   └── 📄 helpers.py               # Helper functions & anime styling
│
├── 🔌 plugins/                     # User plugins directory
│   ├── 📄 __init__.py              # Package initializer
│   ├── 📄 afk.py                   # 💤 AFK module with auto-reply
│   ├── 📄 basic.py                 # 🎯 Basic utility commands
│   ├── 📄 plugin_manager.py        # 🔧 Dynamic plugin management
│   └── 📄 fun.py                   # 🎮 Fun & entertainment commands
│
└── 🤖 assistant/                   # Assistant bot directory
    ├── 📄 __init__.py              # Package initializer
    └── 📄 inline.py                # Inline features & button menus
```

---

## 📦 File Descriptions

### Core Files

**main.py** (3.5 KB)
- Bot initialization
- Client setup
- Database connection
- Plugin loader
- Startup handler

**config.py** (2.0 KB)
- Configuration class
- Environment variables
- Settings validation
- Default values

**generate_session.py** (2.0 KB)
- Interactive session generator
- Phone number login
- 2FA support
- Session string export

**setup.sh** (3.5 KB)
- Automated installation
- Dependency checks
- MongoDB setup
- Configuration wizard

**requirements.txt** (512 B)
- Pyrogram
- TgCrypto
- Motor (MongoDB async)
- Python-dotenv
- Additional dependencies

---

### Utils Module (17 KB total)

**logger.py** (2.5 KB)
- Colored console output
- File logging
- Log rotation
- Custom formatters

**database.py** (6.0 KB)
- MongoDB connection
- CRUD operations
- AFK data management
- Settings storage
- Plugin data
- Filters & notes

**helpers.py** (4.5 KB)
- Time formatting
- Mention helpers
- Argument parsers
- Anime borders
- Info boxes
- Progress bars

---

### Plugins (31 KB total)

**afk.py** (5.0 KB)
- Set AFK status
- Auto-reply to mentions
- Media support
- Time tracking
- Mention counter
- Database persistence

**basic.py** (7.0 KB)
- `.ping` - Response time
- `.alive` - Status check
- `.help` - Help system
- `.stats` - Statistics
- `.id` - Get IDs
- `.purge` - Bulk delete
- `.del` - Delete message

**plugin_manager.py** (6.5 KB)
- `.plugins` - List plugins
- `.load` - Load plugin
- `.unload` - Unload plugin
- `.reload` - Reload plugin
- Dynamic management
- Error handling

**fun.py** (8.0 KB)
- `.quote` - Anime quotes
- `.kaomoji` - Emoticons
- `.aesthetic` - Text styling
- `.typewriter` - Animation
- `.countdown` - Timer
- `.love` - Calculator
- `.flip` - Coin flip
- `.roll` - Dice roll
- `.choose` - Random choice

---

### Assistant Bot (12 KB total)

**inline.py** (7.5 KB)
- `/start` - Main menu
- Button handlers
- Callback queries
- Settings interface
- Statistics display
- Plugin info
- Access control

---

### Documentation (16 KB total)

**README.md** (8.5 KB)
- Complete documentation
- Installation guide
- Features list
- Command reference
- Troubleshooting
- Contributing guide

**QUICKSTART.md** (3.0 KB)
- 5-minute setup
- Quick commands
- Common issues
- First steps

**FEATURES.md** (5.5 KB)
- Detailed feature list
- Use cases
- Performance specs
- Upcoming features

---

## 🎯 Key Components

### 1. Main Bot (main.py)
Entry point that initializes everything:
- Creates Pyrogram clients
- Connects to MongoDB
- Loads plugins
- Starts assistant bot
- Handles lifecycle

### 2. Plugin System
Modular architecture:
- Each plugin is independent
- Hot-reload support
- Auto-discovery
- Error isolation

### 3. Database Layer
MongoDB integration:
- Async operations
- Multiple collections
- Easy queries
- Data persistence

### 4. Utility Layer
Helper functions:
- Time management
- Text formatting
- Anime styling
- Common operations

### 5. Assistant Bot
Separate bot instance:
- Inline features
- Button menus
- Settings UI
- Statistics

---

## 🔄 Data Flow

```
User Message
     ↓
Pyrogram Client
     ↓
Plugin Handler
     ↓
Database Query (if needed)
     ↓
Helper Functions (styling)
     ↓
Response to User
```

---

## 💡 Development Tips

### Adding New Plugin
1. Create file in `plugins/`
2. Import required modules
3. Use decorators for handlers
4. Add `__MODULE__` and `__HELP__`
5. Use helper functions for styling

### Using Database
```python
from main import bot

# In async function
await bot.db.set_plugin_setting("myPlugin", "key", "value")
value = await bot.db.get_plugin_setting("myPlugin", "key")
```

### Styling Messages
```python
from utils.helpers import anime_border, info_box

# Anime border
response = anime_border("Your text here", "Title")

# Info box
response = info_box("Title", {
    "Key1": "Value1",
    "Key2": "Value2"
})
```

---

## 📊 Size Distribution

```
Total Size: ~95 KB

Plugins:        31 KB (33%)
Utils:          17 KB (18%)
Documentation:  16 KB (17%)
Assistant:      12 KB (13%)
Core:           10 KB (10%)
Config:         9 KB  (9%)
```

---

**Made with 💙**

*Clean code, beautiful design, powerful features*
