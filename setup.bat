@echo off
echo ╔══════════════════════════════════════════════════════════════════════╗
echo ║                                                                      ║
echo ║              💙 Kaoruko Userbot - Windows Setup 💙                   ║
echo ║                                                                      ║
echo ╚══════════════════════════════════════════════════════════════════════╝
echo.

echo 🔍 Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation!
    pause
    exit /b 1
)

python --version
echo ✅ Python is installed
echo.

echo 📦 Upgrading pip...
python -m pip install --upgrade pip
echo.

echo 📦 Installing dependencies...
echo.
echo Installing TgCrypto for better performance...
pip install TgCrypto
if %errorlevel% neq 0 (
    echo ⚠️  TgCrypto installation failed. Bot will work but slower.
    echo    You may need Visual C++ Build Tools.
    echo.
)

echo Installing other dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies!
    pause
    exit /b 1
)
echo ✅ Dependencies installed
echo.

echo 📝 Setting up configuration...
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    echo ✅ .env file created
    echo.
    echo ⚠️  IMPORTANT: Edit .env file and add your credentials!
    echo.
    echo Opening .env in notepad...
    timeout /t 2 >nul
    notepad .env
) else (
    echo ✅ .env file already exists
)
echo.

echo ═══════════════════════════════════════════════════════════════
echo.
echo ✅ Setup Complete!
echo.
echo 📝 Next Steps:
echo    1. Make sure you edited .env file with your credentials
echo    2. Run: python generate_session.py
echo    3. Run: python main.py
echo.
echo 💙 Enjoy your Kaoruko Userbot!
echo.
echo ═══════════════════════════════════════════════════════════════
echo.
pause
