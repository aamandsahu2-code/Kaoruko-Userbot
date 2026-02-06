"""
Quiz Feature for Assistant Bot
Interactive quiz with inline buttons
"""

from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import Config
from utils.helpers import anime_border
import random

# Quiz questions database
QUIZ_DATA = [
    {
        "question": "What is the capital of Japan?",
        "options": ["Tokyo", "Osaka", "Kyoto", "Nagoya"],
        "correct": 0
    },
    {
        "question": "Which anime has the most episodes?",
        "options": ["One Piece", "Naruto", "Bleach", "Dragon Ball"],
        "correct": 0
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct": 1
    },
    {
        "question": "Which programming language is used for this bot?",
        "options": ["JavaScript", "Python", "Java", "C++"],
        "correct": 1
    },
    {
        "question": "What color is the Kaoruko theme?",
        "options": ["Red", "Blue", "Green", "Purple"],
        "correct": 1
    }
]

@Client.on_message(filters.command("quiz") & filters.private)
async def quiz_command(client: Client, message: Message):
    """Start a quiz game"""
    
    # Check authorization
    if message.from_user.id not in [Config.OWNER_ID] + Config.SUDO_USERS:
        await message.reply_text("❌ You are not authorized!")
        return
    
    # Select random question
    question = random.choice(QUIZ_DATA)
    q_index = QUIZ_DATA.index(question)
    
    # Create option buttons
    buttons = []
    for i, option in enumerate(question["options"]):
        buttons.append([
            InlineKeyboardButton(
                option,
                callback_data=f"quiz_{q_index}_{i}"
            )
        ])
    
    markup = InlineKeyboardMarkup(buttons)
    
    text = (
        f"│  🎯 <b>Question:</b>\n"
        f"│\n"
        f"│  {question['question']}\n"
        f"│\n"
        f"│  Choose your answer below:\n"
    )
    
    response = anime_border(text, "Quiz Time")
    await message.reply_text(response, reply_markup=markup)

@Client.on_callback_query(filters.regex("^quiz_"))
async def quiz_callback(client: Client, callback: CallbackQuery):
    """Handle quiz answer callbacks"""
    
    data = callback.data.split("_")
    q_index = int(data[1])
    answer = int(data[2])
    
    question = QUIZ_DATA[q_index]
    correct = question["correct"]
    
    if answer == correct:
        emoji = "✅"
        status = "Correct!"
        message = "Well done! 🎉"
    else:
        emoji = "❌"
        status = "Wrong!"
        message = f"Correct answer: {question['options'][correct]}"
    
    result_text = (
        f"│  {emoji} <b>{status}</b>\n"
        f"│\n"
        f"│  {message}\n"
    )
    
    response = anime_border(result_text, "Quiz Result")
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔄 Try Again", callback_data="quiz_restart"),
            InlineKeyboardButton("❌ Close", callback_data="quiz_close")
        ]
    ])
    
    await callback.message.edit_text(response, reply_markup=buttons)
    await callback.answer()

@Client.on_callback_query(filters.regex("^quiz_restart$"))
async def quiz_restart(client: Client, callback: CallbackQuery):
    """Restart quiz with new question"""
    
    # Select new random question
    question = random.choice(QUIZ_DATA)
    q_index = QUIZ_DATA.index(question)
    
    # Create option buttons
    buttons = []
    for i, option in enumerate(question["options"]):
        buttons.append([
            InlineKeyboardButton(
                option,
                callback_data=f"quiz_{q_index}_{i}"
            )
        ])
    
    markup = InlineKeyboardMarkup(buttons)
    
    text = (
        f"│  🎯 <b>Question:</b>\n"
        f"│\n"
        f"│  {question['question']}\n"
        f"│\n"
        f"│  Choose your answer below:\n"
    )
    
    response = anime_border(text, "Quiz Time")
    await callback.message.edit_text(response, reply_markup=markup)
    await callback.answer("New question loaded! 🎮")

@Client.on_callback_query(filters.regex("^quiz_close$"))
async def quiz_close(client: Client, callback: CallbackQuery):
    """Close quiz"""
    
    await callback.message.delete()
    await callback.answer("Quiz closed!")