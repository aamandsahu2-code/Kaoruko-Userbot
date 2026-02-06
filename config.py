"""
Configuration file for Kaoruko Userbot
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram API credentials
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    SESSION_STRING = os.getenv("SESSION_STRING", "")
    
    # Bot token for assistant
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    
    # Database
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "kaoruko_db")
    
    # Owner and sudo users
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    
    # Parse SUDO_USERS safely
    sudo_users_str = os.getenv("SUDO_USERS", "")
    SUDO_USERS = []
    if sudo_users_str:
        for user_id in sudo_users_str.split():
            try:
                # Skip placeholder values
                if user_id.startswith("user_id"):
                    continue
                SUDO_USERS.append(int(user_id))
            except ValueError:
                print(f"Warning: Invalid SUDO_USER value '{user_id}' - skipping")
    
    # Command prefix
    CMD_PREFIX = os.getenv("CMD_PREFIX", ".")
    
    # Bot settings
    BOT_NAME = "Kaoruko"
    BOT_VERSION = "1.0.0"
    
    # Theme colors (Kaoruko Waguri - Blue aesthetic)
    THEME_COLOR = "#4A90E2"  # Blue
    ACCENT_COLOR = "#7CB9E8"  # Light blue
    
    # Logging
    LOG_CHAT = int(os.getenv("LOG_CHAT", "0")) if os.getenv("LOG_CHAT", "0").isdigit() else 0
    
    # AFK settings
    AFK_MEDIA = os.getenv("AFK_MEDIA", "")  # URL or file_id for AFK media
    
    @classmethod
    def validate(cls):
        """Validate required configuration"""
        if not cls.API_ID or cls.API_ID == 0:
            raise ValueError("❌ API_ID is required! Get it from https://my.telegram.org")
        
        if not cls.API_HASH:
            raise ValueError("❌ API_HASH is required! Get it from https://my.telegram.org")
        
        if not cls.SESSION_STRING:
            raise ValueError("❌ SESSION_STRING is required! Run: python generate_session.py")
        
        if not cls.MONGO_URI:
            raise ValueError("❌ MONGO_URI is required!")
        
        print("✅ Configuration validated successfully!")
