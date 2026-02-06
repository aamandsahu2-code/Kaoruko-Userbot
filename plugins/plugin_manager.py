"""
Plugin Manager for Kaoruko Userbot
Dynamic plugin loading/unloading system
"""

import os
import importlib
import sys
from pathlib import Path
from pyrogram import Client, filters
from pyrogram.types import Message

from config import Config
from utils.helpers import edit_or_reply, anime_border, info_box
from utils.logger import LOGGER

# Track loaded plugins
loaded_plugins = {}

def get_plugins_list():
    """Get list of available plugins"""
    plugins_dir = Path("plugins")
    plugins = []
    
    for file in plugins_dir.glob("*.py"):
        if not file.name.startswith("_"):
            plugins.append(file.stem)
    
    return sorted(plugins)

def load_plugin_module(plugin_name: str):
    """Load a plugin module"""
    try:
        module = importlib.import_module(f"plugins.{plugin_name}")
        loaded_plugins[plugin_name] = module
        LOGGER.info(f"✅ Loaded plugin: {plugin_name}")
        return True, module
    except Exception as e:
        LOGGER.error(f"❌ Failed to load plugin {plugin_name}: {e}")
        return False, str(e)

def unload_plugin_module(plugin_name: str):
    """Unload a plugin module"""
    try:
        if plugin_name in loaded_plugins:
            del loaded_plugins[plugin_name]
        
        # Remove from sys.modules
        module_name = f"plugins.{plugin_name}"
        if module_name in sys.modules:
            del sys.modules[module_name]
        
        LOGGER.info(f"✅ Unloaded plugin: {plugin_name}")
        return True, None
    except Exception as e:
        LOGGER.error(f"❌ Failed to unload plugin {plugin_name}: {e}")
        return False, str(e)

@Client.on_message(
    filters.command("plugins", prefixes=Config.CMD_PREFIX) & filters.me
)
async def list_plugins(client: Client, message: Message):
    """List all plugins"""
    
    available_plugins = get_plugins_list()
    
    if not available_plugins:
        await edit_or_reply(message, "❌ No plugins found!")
        return
    
    # Create plugin list
    plugin_list = []
    for i, plugin in enumerate(available_plugins, 1):
        status = "✅" if plugin in loaded_plugins else "❌"
        plugin_list.append(f"│  {i}. {status} <code>{plugin}</code>")
    
    text = "\n".join(plugin_list)
    response = anime_border(text, f"Plugins ({len(available_plugins)})")
    
    await edit_or_reply(message, response)

@Client.on_message(
    filters.command("load", prefixes=Config.CMD_PREFIX) & filters.me
)
async def load_plugin(client: Client, message: Message):
    """Load a plugin"""
    
    try:
        plugin_name = message.text.split(None, 1)[1]
    except IndexError:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.load plugin_name</code>"
        )
        return
    
    # Check if plugin exists
    if plugin_name not in get_plugins_list():
        await edit_or_reply(
            message,
            f"❌ Plugin <code>{plugin_name}</code> not found!"
        )
        return
    
    # Check if already loaded
    if plugin_name in loaded_plugins:
        await edit_or_reply(
            message,
            f"⚠️ Plugin <code>{plugin_name}</code> is already loaded!"
        )
        return
    
    # Load the plugin
    await edit_or_reply(message, f"⏳ Loading plugin <code>{plugin_name}</code>...")
    
    success, result = load_plugin_module(plugin_name)
    
    if success:
        # Reload the client to register new handlers
        await client.restart()
        
        response = info_box(
            "Plugin Loaded",
            {
                "Plugin": plugin_name,
                "Status": "Active"
            }
        )
        await edit_or_reply(message, response)
    else:
        await edit_or_reply(
            message,
            f"❌ Failed to load plugin:\n<code>{result}</code>"
        )

@Client.on_message(
    filters.command("unload", prefixes=Config.CMD_PREFIX) & filters.me
)
async def unload_plugin(client: Client, message: Message):
    """Unload a plugin"""
    
    try:
        plugin_name = message.text.split(None, 1)[1]
    except IndexError:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.unload plugin_name</code>"
        )
        return
    
    # Check if loaded
    if plugin_name not in loaded_plugins:
        await edit_or_reply(
            message,
            f"⚠️ Plugin <code>{plugin_name}</code> is not loaded!"
        )
        return
    
    # Unload the plugin
    await edit_or_reply(message, f"⏳ Unloading plugin <code>{plugin_name}</code>...")
    
    success, result = unload_plugin_module(plugin_name)
    
    if success:
        response = info_box(
            "Plugin Unloaded",
            {
                "Plugin": plugin_name,
                "Status": "Inactive"
            }
        )
        await edit_or_reply(message, response)
    else:
        await edit_or_reply(
            message,
            f"❌ Failed to unload plugin:\n<code>{result}</code>"
        )

@Client.on_message(
    filters.command("reload", prefixes=Config.CMD_PREFIX) & filters.me
)
async def reload_plugin(client: Client, message: Message):
    """Reload a plugin"""
    
    try:
        plugin_name = message.text.split(None, 1)[1]
    except IndexError:
        await edit_or_reply(
            message,
            "❌ <b>Usage:</b> <code>.reload plugin_name</code>"
        )
        return
    
    await edit_or_reply(message, f"⏳ Reloading plugin <code>{plugin_name}</code>...")
    
    # Unload
    if plugin_name in loaded_plugins:
        unload_plugin_module(plugin_name)
    
    # Load
    success, result = load_plugin_module(plugin_name)
    
    if success:
        # Reload the client
        await client.restart()
        
        response = info_box(
            "Plugin Reloaded",
            {
                "Plugin": plugin_name,
                "Status": "Active"
            }
        )
        await edit_or_reply(message, response)
    else:
        await edit_or_reply(
            message,
            f"❌ Failed to reload plugin:\n<code>{result}</code>"
        )

# Plugin info
__MODULE__ = "Plugin Manager"
__HELP__ = """
**Plugin Manager** 🔌

Manage your userbot plugins dynamically!

**Commands:**
• `.plugins` - List all plugins
• `.load <name>` - Load a plugin
• `.unload <name>` - Unload a plugin
• `.reload <name>` - Reload a plugin

**Features:**
• Dynamic loading/unloading
• No restart required
• Beautiful plugin list
• Error handling

**Examples:**
```
.plugins
.load afk
.unload afk
.reload afk
```
"""
