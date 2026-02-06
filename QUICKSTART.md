# 🚀 Quick Start Guide

Get your Kaoruko Userbot up and running in 5 minutes!

---

## ⚡ Fast Setup

### 1️⃣ Install Dependencies

```bash
./setup.sh
```

This will:
- Check Python version
- Install all required packages
- Check/install MongoDB
- Create .env file

### 2️⃣ Get Your Credentials

#### A. API Credentials
1. Go to https://my.telegram.org
2. Login with your phone number
3. Go to "API Development Tools"
4. Create new application
5. Note: `API_ID` and `API_HASH`

#### B. Bot Token
1. Open Telegram
2. Search `@BotFather`
3. Send `/newbot`
4. Follow instructions
5. Note: `BOT_TOKEN`

#### C. Your User ID
1. Open Telegram
2. Search `@userinfobot`
3. Start the bot
4. Note your User ID

### 3️⃣ Configure

Edit `.env` file:

```bash
nano .env
```

Fill in:
```env
API_ID=12345678
API_HASH=abc123def456...
BOT_TOKEN=123456:ABC-DEF...
OWNER_ID=987654321
MONGO_URI=mongodb://localhost:27017
```

### 4️⃣ Generate Session

```bash
python3 generate_session.py
```

- Enter your phone number (with country code)
- Enter the code you receive
- If you have 2FA, enter your password
- Copy the session string
- Paste it in `.env` as `SESSION_STRING`

### 5️⃣ Run!

```bash
python3 main.py
```

You should see:
```
💙 Kaoruko | HH:MM:SS | INFO | 🌸 Initializing Kaoruko Userbot...
💙 Kaoruko | HH:MM:SS | INFO | ✅ Database connected successfully
💙 Kaoruko | HH:MM:SS | INFO | 💙 Kaoruko is ready!
💙 Kaoruko | HH:MM:SS | INFO | 🤖 Assistant bot @your_bot started
💙 Kaoruko | HH:MM:SS | INFO | 👤 Userbot started for Your Name
```

---

## 🎯 First Commands

Open any Telegram chat and try:

```
.ping
```
→ Check if bot is working

```
.alive
```
→ See bot status

```
.help
```
→ View available commands

```
.afk Going to sleep 😴
```
→ Set yourself as AFK

```
.plugins
```
→ View all plugins

---

## 🔧 Common Issues

### "Session string invalid"
- Generate a new session: `python3 generate_session.py`
- Make sure you copied it completely

### "Database connection failed"
- Check MongoDB: `sudo systemctl status mongodb`
- Start MongoDB: `sudo systemctl start mongodb`

### "Module not found"
- Install dependencies: `pip3 install -r requirements.txt`

### "Permission denied"
- Make scripts executable: `chmod +x setup.sh generate_session.py`

---

## 📱 Using the Assistant Bot

1. Open Telegram
2. Search for your bot (@your_bot_username)
3. Start the bot: `/start`
4. Explore the inline menus!

---

## 🎨 Customization

### Change Command Prefix

In `.env`:
```env
CMD_PREFIX=!
```

Now use: `!ping`, `!alive`, etc.

### Change Theme Colors

In `config.py`:
```python
THEME_COLOR = "#FF69B4"  # Pink
ACCENT_COLOR = "#FFB6C1"  # Light pink
```

---

## 🆘 Need Help?

- Read full documentation: [README.md](README.md)
- Check troubleshooting section
- Open an issue on GitHub

---

## 🎉 You're Ready!

Your Kaoruko Userbot is now running! 

**Next Steps:**
- Explore built-in plugins
- Create custom plugins
- Join our community
- Share feedback

---

**Made with 💙**
