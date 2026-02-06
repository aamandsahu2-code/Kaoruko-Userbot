# 🪟 Windows Setup Guide for Kaoruko Userbot

## ⚠️ Important for Windows Users

Windows pe kuch extra steps hain. Yeh guide follow karo:

---

## 📋 Prerequisites

### 1. Install Python 3.9+

1. Download from: https://www.python.org/downloads/
2. **IMPORTANT:** Check "Add Python to PATH" during installation
3. Verify installation:
```powershell
python --version
```

### 2. Install Visual C++ Build Tools (Required for TgCrypto)

**Option A: Install Visual Studio Build Tools**
1. Download: https://visualstudio.microsoft.com/downloads/
2. Select "Build Tools for Visual Studio 2022"
3. Install "Desktop development with C++"

**Option B: Quick Install via Chocolatey**
```powershell
# Install Chocolatey first (if not installed)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Then install build tools
choco install visualstudio2022buildtools --package-parameters "--add Microsoft.VisualStudio.Workload.VCTools"
```

### 3. Install MongoDB

**Option A: MongoDB Community Server (Local)**
1. Download: https://www.mongodb.com/try/download/community
2. Install with default settings
3. MongoDB Compass (GUI) is optional but helpful

**Option B: MongoDB Atlas (Cloud - Recommended)**
1. Go to: https://www.mongodb.com/cloud/atlas
2. Create free account
3. Create free cluster
4. Get connection string
5. Use in `.env` file

---

## 🚀 Installation Steps

### Step 1: Extract Files

```powershell
# Extract the tar.gz file
# You can use 7-Zip or WinRAR
# Or use PowerShell:
tar -xzf kaoruko-userbot.tar.gz
cd kaoruko-userbot
```

### Step 2: Install Dependencies

```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install TgCrypto (for speed)
pip install TgCrypto

# Install all dependencies
pip install -r requirements.txt
```

**If TgCrypto fails to install:**
```powershell
# Bot will still work, just slower
# Continue with other dependencies
pip install -r requirements.txt
```

### Step 3: Create .env File

```powershell
# Copy example file
copy .env.example .env

# Edit with notepad
notepad .env
```

**Fill in your details:**
```env
API_ID=12345678
API_HASH=abc123def456
SESSION_STRING=your_session_string
BOT_TOKEN=123456:ABC-DEF
OWNER_ID=987654321
MONGO_URI=mongodb://localhost:27017
```

**IMPORTANT:** 
- Remove placeholder values like "your_api_id", "user_id1"
- Use actual numbers and strings
- No quotes needed around values

### Step 4: Generate Session String

```powershell
python generate_session.py
```

Follow the prompts:
1. Enter phone number (with country code): `+1234567890`
2. Enter the code you receive
3. If 2FA enabled, enter password
4. Copy the session string
5. Paste in `.env` file

### Step 5: Start MongoDB (if using local)

**Option A: MongoDB Service**
```powershell
# Start as Windows Service
net start MongoDB
```

**Option B: Manual Start**
```powershell
# Navigate to MongoDB bin folder
cd "C:\Program Files\MongoDB\Server\7.0\bin"
mongod
```

**Option C: Use MongoDB Atlas (Cloud)**
- No need to start anything
- Just use your Atlas connection string in `.env`

### Step 6: Run the Bot!

```powershell
python main.py
```

---

## 🔧 Common Windows Issues

### Issue 1: "TgCrypto is missing"
**Solution:**
```powershell
# Install Visual C++ Build Tools first
# Then install TgCrypto
pip install TgCrypto
```

### Issue 2: "ValueError: invalid literal for int()"
**Solution:**
Your `.env` file has placeholder values. Edit it:
```powershell
notepad .env
```
Replace:
- `your_api_id` → Your actual API ID (numbers only)
- `user_id1` → Remove this line or leave SUDO_USERS empty
- `your_api_hash` → Your actual API hash
- etc.

### Issue 3: "ModuleNotFoundError"
**Solution:**
```powershell
pip install -r requirements.txt --upgrade
```

### Issue 4: MongoDB Connection Failed
**Solution A (Local MongoDB):**
```powershell
# Check if MongoDB is running
Get-Service MongoDB

# Start if not running
net start MongoDB
```

**Solution B (Use Cloud):**
```env
# In .env file, use MongoDB Atlas
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
```

### Issue 5: Permission Denied
**Solution:**
```powershell
# Run PowerShell as Administrator
# Right-click PowerShell → Run as Administrator
```

### Issue 6: Python Not Found
**Solution:**
```powershell
# Try using 'py' instead of 'python'
py main.py

# Or add Python to PATH:
# 1. Search "Environment Variables" in Windows
# 2. Edit System PATH
# 3. Add Python installation folder
```

---

## 📝 Windows-Specific Notes

### Using PowerShell vs Command Prompt

**PowerShell (Recommended):**
```powershell
python main.py
```

**Command Prompt:**
```cmd
python main.py
```

### File Paths

Windows uses backslashes:
```
C:\Users\YourName\Desktop\kaoruko-userbot
```

But in code/config, use forward slashes or double backslashes:
```python
"C:/Users/YourName/Desktop/kaoruko-userbot"
# or
"C:\\Users\\YourName\\Desktop\\kaoruko-userbot"
```

### Running in Background

**Option A: Use `pythonw`**
```powershell
pythonw main.py
# Runs without console window
```

**Option B: Windows Terminal**
```powershell
# Install Windows Terminal from Microsoft Store
# Create new tab for bot
# Keep it running
```

**Option C: Task Scheduler**
1. Open Task Scheduler
2. Create Basic Task
3. Trigger: At startup
4. Action: Start program
5. Program: `python`
6. Arguments: `main.py`
7. Start in: `C:\path\to\kaoruko-userbot`

---

## 🎯 Quick Start (Windows)

```powershell
# 1. Extract
tar -xzf kaoruko-userbot.tar.gz
cd kaoruko-userbot

# 2. Install
pip install -r requirements.txt

# 3. Configure
copy .env.example .env
notepad .env
# Edit and save

# 4. Generate session
python generate_session.py
# Copy session string to .env

# 5. Run!
python main.py
```

---

## 💡 Pro Tips for Windows

1. **Use Windows Terminal** - Better than CMD
2. **MongoDB Atlas** - Easier than local MongoDB
3. **VS Code** - Great for editing code
4. **Git Bash** - Unix-like commands on Windows
5. **Virtual Environment** - Keep dependencies isolated

### Creating Virtual Environment

```powershell
# Create venv
python -m venv venv

# Activate
.\venv\Scripts\Activate.ps1

# If execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate again
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run bot
python main.py

# Deactivate when done
deactivate
```

---

## 🆘 Still Having Issues?

1. **Check Python Version:**
```powershell
python --version
# Should be 3.9 or higher
```

2. **Check pip:**
```powershell
pip --version
```

3. **Reinstall Dependencies:**
```powershell
pip uninstall pyrogram tgcrypto motor -y
pip install -r requirements.txt
```

4. **Check .env file:**
```powershell
type .env
# Should show your actual values, not placeholders
```

5. **Run with verbose logging:**
```powershell
python main.py --verbose
```

---

## 📱 Alternative: Use WSL (Windows Subsystem for Linux)

If Windows is giving too many issues, use WSL:

```powershell
# Install WSL
wsl --install

# After restart, install Ubuntu
# Then follow Linux installation guide
```

---

**Windows setup complete! Enjoy your Kaoruko Userbot! 💙**
