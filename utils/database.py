"""
MongoDB Database Manager for Kaoruko Userbot
"""

from typing import Any, Dict, List, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase
from utils.logger import LOGGER

class Database:
    """MongoDB database manager"""
    
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.afk = db.afk
        self.plugins = db.plugins
        self.filters = db.filters
        self.notes = db.notes
        self.settings = db.settings
        
    async def ping(self):
        """Ping the database"""
        try:
            await self.db.command("ping")
            return True
        except Exception as e:
            LOGGER.error(f"Database ping failed: {e}")
            return False
    
    # ========== AFK Methods ==========
    
    async def set_afk(self, user_id: int, reason: str = None, media: str = None):
        """Set user as AFK"""
        data = {
            "user_id": user_id,
            "reason": reason,
            "media": media,
            "time": None  # Will be set by the plugin
        }
        await self.afk.update_one(
            {"user_id": user_id},
            {"$set": data},
            upsert=True
        )
        LOGGER.info(f"Set AFK for user {user_id}")
    
    async def get_afk(self, user_id: int) -> Optional[Dict]:
        """Get AFK status"""
        return await self.afk.find_one({"user_id": user_id})
    
    async def remove_afk(self, user_id: int):
        """Remove AFK status"""
        result = await self.afk.delete_one({"user_id": user_id})
        if result.deleted_count:
            LOGGER.info(f"Removed AFK for user {user_id}")
        return result.deleted_count > 0
    
    # ========== Plugin Settings Methods ==========
    
    async def set_plugin_setting(self, plugin_name: str, key: str, value: Any):
        """Set plugin setting"""
        await self.plugins.update_one(
            {"plugin": plugin_name},
            {"$set": {key: value}},
            upsert=True
        )
    
    async def get_plugin_setting(self, plugin_name: str, key: str, default: Any = None) -> Any:
        """Get plugin setting"""
        doc = await self.plugins.find_one({"plugin": plugin_name})
        if doc and key in doc:
            return doc[key]
        return default
    
    async def delete_plugin_setting(self, plugin_name: str, key: str = None):
        """Delete plugin setting or entire plugin data"""
        if key:
            await self.plugins.update_one(
                {"plugin": plugin_name},
                {"$unset": {key: ""}}
            )
        else:
            await self.plugins.delete_one({"plugin": plugin_name})
    
    # ========== Filters Methods ==========
    
    async def add_filter(self, chat_id: int, keyword: str, response: str, media: str = None):
        """Add a filter"""
        data = {
            "chat_id": chat_id,
            "keyword": keyword.lower(),
            "response": response,
            "media": media
        }
        await self.filters.update_one(
            {"chat_id": chat_id, "keyword": keyword.lower()},
            {"$set": data},
            upsert=True
        )
    
    async def get_filter(self, chat_id: int, keyword: str) -> Optional[Dict]:
        """Get a filter"""
        return await self.filters.find_one({
            "chat_id": chat_id,
            "keyword": keyword.lower()
        })
    
    async def get_all_filters(self, chat_id: int) -> List[Dict]:
        """Get all filters for a chat"""
        cursor = self.filters.find({"chat_id": chat_id})
        return await cursor.to_list(length=None)
    
    async def delete_filter(self, chat_id: int, keyword: str):
        """Delete a filter"""
        result = await self.filters.delete_one({
            "chat_id": chat_id,
            "keyword": keyword.lower()
        })
        return result.deleted_count > 0
    
    # ========== Notes Methods ==========
    
    async def add_note(self, chat_id: int, name: str, content: str, media: str = None):
        """Add a note"""
        data = {
            "chat_id": chat_id,
            "name": name.lower(),
            "content": content,
            "media": media
        }
        await self.notes.update_one(
            {"chat_id": chat_id, "name": name.lower()},
            {"$set": data},
            upsert=True
        )
    
    async def get_note(self, chat_id: int, name: str) -> Optional[Dict]:
        """Get a note"""
        return await self.notes.find_one({
            "chat_id": chat_id,
            "name": name.lower()
        })
    
    async def get_all_notes(self, chat_id: int) -> List[Dict]:
        """Get all notes for a chat"""
        cursor = self.notes.find({"chat_id": chat_id})
        return await cursor.to_list(length=None)
    
    async def delete_note(self, chat_id: int, name: str):
        """Delete a note"""
        result = await self.notes.delete_one({
            "chat_id": chat_id,
            "name": name.lower()
        })
        return result.deleted_count > 0
    
    # ========== Settings Methods ==========
    
    async def set_setting(self, key: str, value: Any):
        """Set a global setting"""
        await self.settings.update_one(
            {"key": key},
            {"$set": {"value": value}},
            upsert=True
        )
    
    async def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a global setting"""
        doc = await self.settings.find_one({"key": key})
        if doc:
            return doc.get("value", default)
        return default
    
    async def delete_setting(self, key: str):
        """Delete a global setting"""
        result = await self.settings.delete_one({"key": key})
        return result.deleted_count > 0
