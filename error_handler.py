"""
Custom Exception Handler
Suppresses Pyrogram peer resolution errors
"""

import sys
import logging
import warnings
from functools import wraps

# ==========================================
#     COMPLETE ERROR SUPPRESSION SYSTEM
# ==========================================

# 1. Suppress all pyrogram warnings
logging.getLogger("pyrogram").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.connection").setLevel(logging.CRITICAL)

# 2. Suppress specific error messages
warnings.filterwarnings("ignore")

# 3. Custom exception hook to suppress peer errors
original_excepthook = sys.excepthook

def custom_excepthook(exc_type, exc_value, exc_traceback):
    """Custom exception handler to suppress peer errors"""
    
    # Check if it's a peer error
    error_message = str(exc_value)
    
    if "Peer id invalid" in error_message:
        # Silently ignore peer errors
        return
    
    if "ID not found" in error_message:
        # Silently ignore peer cache errors
        return
    
    if "Task exception was never retrieved" in error_message:
        # Silently ignore task exceptions
        return
    
    # For other errors, use original handler
    original_excepthook(exc_type, exc_value, exc_traceback)

# Install custom exception handler
sys.excepthook = custom_excepthook

# 4. Patch asyncio to suppress task exceptions
import asyncio

# Store original Task class
_original_task_class = asyncio.Task

class SilentTask(asyncio.Task):
    """Custom Task class that doesn't print exceptions"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add done callback to suppress exceptions
        self.add_done_callback(self._silent_exception_handler)
    
    @staticmethod
    def _silent_exception_handler(task):
        """Silently handle task exceptions"""
        try:
            task.result()
        except asyncio.CancelledError:
            pass  # Task was cancelled
        except Exception as e:
            # Only log if it's not a peer error
            error_msg = str(e)
            if "Peer id invalid" not in error_msg and "ID not found" not in error_msg:
                # Log other errors
                logging.error(f"Task exception: {e}")

# Replace Task class
# asyncio.Task = SilentTask  # Commented out as it may cause issues

print("✅ Error suppression system loaded")