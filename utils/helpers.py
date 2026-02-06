"""
Helper utilities for Kaoruko Userbot
"""

import time
from datetime import datetime, timedelta
from typing import Optional
from pyrogram.types import Message

def get_time_difference(start_time: float) -> str:
    """Get human-readable time difference"""
    seconds = int(time.time() - start_time)
    
    periods = [
        ('year', 31536000),
        ('month', 2592000),
        ('week', 604800),
        ('day', 86400),
        ('hour', 3600),
        ('minute', 60),
        ('second', 1)
    ]
    
    parts = []
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            if period_value == 1:
                parts.append(f"{period_value} {period_name}")
            else:
                parts.append(f"{period_value} {period_name}s")
    
    if not parts:
        return "just now"
    
    if len(parts) == 1:
        return parts[0]
    
    return ", ".join(parts[:2])

def format_time(timestamp: float) -> str:
    """Format timestamp to readable format"""
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%d %b %Y, %I:%M %p")

def extract_args(message: Message, arg_count: int = 1) -> tuple:
    """Extract arguments from message"""
    if not message.text:
        return tuple([None] * arg_count)
    
    parts = message.text.split(maxsplit=arg_count)
    args = parts[1:] if len(parts) > 1 else []
    
    # Pad with None if not enough arguments
    while len(args) < arg_count:
        args.append(None)
    
    return tuple(args[:arg_count])

def get_arg(message: Message) -> Optional[str]:
    """Get argument from message"""
    try:
        arg = message.text.split(None, 1)[1]
        return arg
    except:
        return None

def get_reply_msg(message: Message) -> Optional[Message]:
    """Get replied message if exists"""
    return message.reply_to_message

async def edit_or_reply(message: Message, text: str, **kwargs):
    """Edit message if outgoing, otherwise reply"""
    if message.from_user and message.from_user.is_self:
        return await message.edit(text, **kwargs)
    else:
        return await message.reply(text, **kwargs)

def mention_user(user) -> str:
    """Create mention for user"""
    if user.username:
        return f"@{user.username}"
    return f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"

def create_progress_bar(current: int, total: int, length: int = 10) -> str:
    """Create a progress bar"""
    filled = int(length * current / total)
    bar = '█' * filled + '░' * (length - filled)
    percentage = int(100 * current / total)
    return f"{bar} {percentage}%"

# Anime-themed decorators and wrappers

def anime_border(text: str, title: str = "Kaoruko") -> str:
    """Add anime-style border to text"""
    return (
        f"╭─「 <b>💙 {title}</b> 」\n"
        f"│\n"
        f"{text}\n"
        f"│\n"
        f"╰─「 <i>✨ Kaoruko Userbot</i> 」"
    )

def info_box(title: str, content: dict) -> str:
    """Create info box with anime styling"""
    lines = [f"╭─「 <b>💙 {title}</b> 」", "│"]
    
    for key, value in content.items():
        lines.append(f"│  <b>{key}:</b> <code>{value}</code>")
    
    lines.extend(["│", "╰─「 <i>✨ Kaoruko Userbot</i> 」"])
    
    return "\n".join(lines)

def success_msg(text: str) -> str:
    """Success message with anime styling"""
    return f"✅ <b>Success!</b>\n\n{text}"

def error_msg(text: str) -> str:
    """Error message with anime styling"""
    return f"❌ <b>Error!</b>\n\n{text}"

def loading_msg(text: str = "Loading") -> str:
    """Loading message"""
    return f"⏳ <i>{text}...</i>"

# Time utilities

def get_readable_time(seconds: int) -> str:
    """Convert seconds to readable time"""
    count = 0
    time_string = ""
    time_suffix_list = ["s", "m", "h", "days"]
    
    time_list = []
    for i in range(len(time_suffix_list)):
        time_list.append(0)
    
    while count < len(time_suffix_list):
        if count < 3:
            if seconds >= 60:
                time_list[count + 1] = int(seconds / 60)
                seconds %= 60
            time_list[count] = int(seconds)
            seconds = time_list[count + 1]
        else:
            time_list[count] = int(seconds / 24)
        count += 1
    
    for i in range(len(time_list)):
        time_string += f"{time_list[i]}{time_suffix_list[i]} "
    
    return time_string.strip()
