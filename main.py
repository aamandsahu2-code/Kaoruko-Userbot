"""
Kaoruko Userbot - Anime Aesthetic Userbot
Inspired by Kaoruko Waguri 💙
"""

# ==========================================
#  IMPORT ERROR HANDLER FIRST (IMPORTANT!)
# ==========================================
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import error handler to suppress warnings
try:
    from utils import error_handler
except:
    pass  # If error_handler doesn't exist, continue

# ==========================================
#        STANDARD IMPORTS
# ==========================================
import asyncio
import logging
import warnings
from pathlib import Path

from pyrogram import Client, idle
from pyrogram.enums import ParseMode
from motor.motor_asyncio import AsyncIOMotorClient

from config import Config
from utils.logger import LOGGER
from utils.database import Database

# ==========================================
#    ADDITIONAL ERROR SUPPRESSION
# ==========================================
# Suppress all warnings
warnings.filterwarnings("ignore")

# Suppress Pyrogram logs
logging.getLogger("pyrogram").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.connection").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.dispatcher").setLevel(logging.CRITICAL)

# Suppress asyncio warnings
logging.getLogger("asyncio").setLevel(logging.CRITICAL)

class KaorukoBot:
    def __init__(self):
        self.app = None
        self.assistant = None
        self.db = None
        
    async def initialize(self):
        """Initialize the userbot and assistant bot"""
        LOGGER.info("🌸 Initializing Kaoruko Userbot...")
        
        # Initialize MongoDB
        try:
            mongo_client = AsyncIOMotorClient(Config.MONGO_URI)
            self.db = Database(mongo_client[Config.DB_NAME])
            await self.db.ping()
            LOGGER.info("✅ Database connected successfully")
        except Exception as e:
            LOGGER.error(f"❌ Database connection failed: {e}")
            sys.exit(1)
        
        # Initialize main userbot
        self.app = Client(
            name="kaoruko_userbot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            session_string=Config.SESSION_STRING,
            plugins=dict(root="plugins"),
            parse_mode=ParseMode.HTML,
            sleep_threshold=60
        )
        
        # Attach database to app so plugins can use it
        self.app.db = self.db
        
        # Initialize assistant bot
        if Config.BOT_TOKEN:
            self.assistant = Client(
                name="kaoruko_assistant",
                api_id=Config.API_ID,
                api_hash=Config.API_HASH,
                bot_token=Config.BOT_TOKEN,
                plugins=dict(root="assistant"),
                parse_mode=ParseMode.HTML
            )
            # Attach database to assistant too
            self.assistant.db = self.db
        
        LOGGER.info("💙 Kaoruko is ready!")
        
    async def start(self):
        """Start the userbot"""
        await self.initialize()
        
        await self.app.start()
        
        if self.assistant:
            await self.assistant.start()
            bot_info = await self.assistant.get_me()
            LOGGER.info(f"🤖 Assistant bot @{bot_info.username} started")
        
        user = await self.app.get_me()
        LOGGER.info(f"👤 Userbot started for {user.first_name}")
        
        # Send startup message
        try:
            startup_msg = (
                "╭─「 <b>💙 Kaoruko Userbot</b> 」\n"
                "│\n"
                "│  <b>Status:</b> <code>Online</code>\n"
                "│  <b>Version:</b> <code>1.0.0</code>\n"
                "│  <b>Theme:</b> <code>Kaoruko Waguri</code>\n"
                "│\n"
                "╰─「 <i>✨ Ready to serve!</i> 」"
            )
            await self.app.send_message("me", startup_msg)
        except:
            pass
        
        LOGGER.info("━" * 50)
        LOGGER.info("🚀 All systems operational!")
        LOGGER.info("💙 Bot is ready to use")
        LOGGER.info("⚡ Try: .ping in Telegram")
        LOGGER.info("━" * 50)
        
        await idle()
        
    async def stop(self):
        """Stop the userbot"""
        LOGGER.info("🌸 Shutting down Kaoruko...")
        
        if self.assistant:
            await self.assistant.stop()
        
        if self.app:
            await self.app.stop()
        LOGGER.info("👋 Goodbye!")

# Create the global bot instance
bot = KaorukoBot()

if __name__ == "__main__":
    print("\n" + "="*50)
    print("💙 Kaoruko Userbot - Starting...")
    print("="*50 + "\n")
    
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        print("\n")
        LOGGER.info("🛑 Bot stopped by user")
        print("="*50)
    except Exception as e:
        LOGGER.error(f"❌ Fatal error: {e}")
        sys.exit(1)