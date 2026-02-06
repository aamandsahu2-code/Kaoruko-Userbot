
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║              💙 KAORUKO USERBOT - READ THIS FIRST! 💙                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝


🎉 Welcome! Thank you for choosing Kaoruko Userbot!


⚠️  IMPORTANT - COMMON ERROR FIX:

If you get this error:
  "ValueError: invalid literal for int() with base 10: 'user_id1'"

SOLUTION:
  Your .env file has placeholder values. You need to replace them!

  1. Open .env file
  2. Replace these placeholders with REAL values:
     ❌ API_ID=your_api_id        → ✅ API_ID=12345678
     ❌ OWNER_ID=your_user_id     → ✅ OWNER_ID=987654321
     ❌ SUDO_USERS=user_id1       → ✅ SUDO_USERS=111111 222222
                                     OR leave empty: SUDO_USERS=

  3. DO NOT use text like "your_api_id" or "user_id1"
  4. Use only NUMBERS for IDs


═══════════════════════════════════════════════════════════════════════


📚 QUICK START GUIDES:

🪟 Windows Users:
   → Read: WINDOWS_SETUP.md
   → Run: setup.bat

🐧 Linux/Mac Users:
   → Read: QUICKSTART.md
   → Run: ./setup.sh

📖 Complete Documentation:
   → Read: README.md


═══════════════════════════════════════════════════════════════════════


🚀 SUPER QUICK START (5 Steps):

1️⃣  Install Python 3.9+ from: https://www.python.org/downloads/

2️⃣  Install dependencies:
    pip install -r requirements.txt

3️⃣  Setup .env file:
    - Copy .env.example to .env
    - Edit .env and add YOUR real credentials
    - Get API_ID/HASH from: https://my.telegram.org
    - Get BOT_TOKEN from: @BotFather (optional)

4️⃣  Generate session:
    python generate_session.py

5️⃣  Run the bot:
    python main.py


═══════════════════════════════════════════════════════════════════════


🔑 WHERE TO GET CREDENTIALS:

📱 API_ID and API_HASH:
   → Visit: https://my.telegram.org
   → Login with your phone number
   → Click "API Development Tools"
   → Create an app
   → Copy API_ID and API_HASH

🤖 BOT_TOKEN (Optional - for assistant bot):
   → Open Telegram
   → Search: @BotFather
   → Send: /newbot
   → Follow instructions
   → Copy the token

👤 OWNER_ID (Your Telegram ID):
   → Open Telegram
   → Search: @userinfobot
   → Start the bot
   → Copy your User ID

🗄️  MONGO_URI (Database):
   Option A - Local (Windows):
   → Install MongoDB Community Server
   → Use: mongodb://localhost:27017

   Option B - Cloud (Recommended):
   → Visit: https://www.mongodb.com/cloud/atlas
   → Create free account
   → Get connection string


═══════════════════════════════════════════════════════════════════════


✨ FEATURES YOU'LL GET:

💤 AFK System - Auto-reply when away
🎯 30+ Commands - Essential utilities
🔌 Plugin System - Load/unload on the fly
🤖 Assistant Bot - Inline menus
💾 MongoDB - Persistent storage
🎨 Anime Theme - Beautiful Kaoruko aesthetic
⚡ Fast - Pyrogram framework
🎮 Fun Commands - Games, quotes, etc.


═══════════════════════════════════════════════════════════════════════


⚠️  IMPORTANT WARNINGS:

1. Userbots violate Telegram's Terms of Service
2. Your account may get banned
3. RECOMMENDED: Use a secondary account
4. Never share your SESSION_STRING with anyone
5. Keep your .env file private
6. For educational purposes only


═══════════════════════════════════════════════════════════════════════


🆘 TROUBLESHOOTING:

❌ "TgCrypto is missing"
   → Install: pip install TgCrypto
   → Bot will still work, just slower

❌ "ValueError: invalid literal for int()"
   → Check your .env file
   → Remove placeholder values
   → Use real numbers for IDs

❌ "Module not found"
   → Run: pip install -r requirements.txt

❌ "Database connection failed"
   → Check MongoDB is running
   → Or use MongoDB Atlas (cloud)

❌ "Session string invalid"
   → Generate new: python generate_session.py


═══════════════════════════════════════════════════════════════════════


📁 FILES YOU NEED TO KNOW:

main.py              - Main bot file (run this)
config.py            - Configuration 
generate_session.py  - Session generator
.env                 - Your credentials (CREATE THIS!)

setup.bat            - Windows setup script
setup.sh             - Linux setup script

README.md            - Complete documentation
QUICKSTART.md        - Fast setup guide
WINDOWS_SETUP.md     - Windows-specific guide
FEATURES.md          - Feature list

plugins/             - Bot plugins
utils/               - Utility functions
assistant/           - Assistant bot


═══════════════════════════════════════════════════════════════════════


💡 FIRST TIME USERS:

If this is your first time setting up a Telegram userbot:

1. Read QUICKSTART.md or WINDOWS_SETUP.md first
2. Make sure you have all prerequisites
3. Follow step-by-step instructions
4. Don't skip the .env configuration!
5. Test with .ping command after starting


═══════════════════════════════════════════════════════════════════════


🎯 READY TO START?

Windows:    Run setup.bat
Linux/Mac:  Run ./setup.sh
Manual:     Read QUICKSTART.md


═══════════════════════════════════════════════════════════════════════


                        💙 Made with love 💙
                    Kaoruko Userbot v1.0.0


═══════════════════════════════════════════════════════════════════════

