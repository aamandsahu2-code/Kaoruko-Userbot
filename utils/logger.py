"""
Beautiful logger for Kaoruko Userbot
Inspired by Kaoruko Waguri 💙
"""
import sys
import io
# Dono stdout aur stderr ko utf-8 karo
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
import logging
import sys
import os
from logging.handlers import RotatingFileHandler

# Windows terminal UTF-8 encoding fix
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Color codes for terminal
COLORS = {
    'BLUE': '\033[94m',
    'CYAN': '\033[96m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'MAGENTA': '\033[95m',
    'WHITE': '\033[97m',
    'RESET': '\033[0m',
    'BOLD': '\033[1m'
}

class ColoredFormatter(logging.Formatter):
    """Custom formatter with colors for Kaoruko Vibe"""
    
    LEVEL_COLORS = {
        'DEBUG': COLORS['CYAN'],
        'INFO': COLORS['BLUE'],
        'WARNING': COLORS['YELLOW'],
        'ERROR': COLORS['RED'],
        'CRITICAL': COLORS['MAGENTA']
    }
    
    def format(self, record):
        levelname = record.levelname
        if levelname in self.LEVEL_COLORS:
            record.levelname = (
                f"{COLORS['BOLD']}{self.LEVEL_COLORS[levelname]}"
                f"{levelname}{COLORS['RESET']}"
            )
        return super().format(record)

def setup_logger():
    """Setup the professional aesthetic logger"""
    logger = logging.getLogger("Kaoruko")
    logger.setLevel(logging.INFO)
    
    # Prevents double logging if logger is re-initialized
    if logger.hasHandlers():
        logger.handlers.clear()
    
    # 1. Console handler (Terminal output)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    console_formatter = ColoredFormatter(
        f"{COLORS['BLUE']}💙 Kaoruko{COLORS['RESET']} | "
        f"{COLORS['CYAN']}%(asctime)s{COLORS['RESET']} | "
        f"%(levelname)s | "
        f"{COLORS['WHITE']}%(message)s{COLORS['RESET']}",
        datefmt="%H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)
    
    # 2. File handler (Log file saving)
    file_handler = RotatingFileHandler(
        "kaoruko.log",
        maxBytes=5 * 1024 * 1024,  # 5MB
        backupCount=3,
        encoding='utf-8' # Force UTF-8 for log file
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Global LOGGER instance
LOGGER = setup_logger()