#!/bin/bash

# Kaoruko Userbot Setup Script
# This script helps you set up the userbot easily

echo "╭─────────────────────────────────────╮"
echo "│                                     │"
echo "│    💙 Kaoruko Userbot Setup 💙     │"
echo "│                                     │"
echo "╰─────────────────────────────────────╯"
echo ""

# Check Python version
echo "🔍 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.9"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then 
    echo "✅ Python $python_version is installed"
else
    echo "❌ Python 3.9+ is required. You have $python_version"
    exit 1
fi

# Check if pip is installed
echo ""
echo "🔍 Checking pip..."
if command -v pip3 &> /dev/null; then
    echo "✅ pip3 is installed"
else
    echo "❌ pip3 is not installed"
    echo "📦 Installing pip3..."
    sudo apt install python3-pip -y
fi

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Check MongoDB
echo ""
echo "🔍 Checking MongoDB..."
if command -v mongod &> /dev/null; then
    echo "✅ MongoDB is installed"
    
    # Check if MongoDB is running
    if systemctl is-active --quiet mongodb; then
        echo "✅ MongoDB is running"
    else
        echo "⚠️  MongoDB is not running"
        echo "📝 Starting MongoDB..."
        sudo systemctl start mongodb
        sudo systemctl enable mongodb
        echo "✅ MongoDB started"
    fi
else
    echo "⚠️  MongoDB is not installed"
    echo "📝 Would you like to install MongoDB? (y/n)"
    read -r install_mongo
    
    if [ "$install_mongo" = "y" ] || [ "$install_mongo" = "Y" ]; then
        echo "📦 Installing MongoDB..."
        sudo apt update
        sudo apt install mongodb -y
        sudo systemctl start mongodb
        sudo systemctl enable mongodb
        echo "✅ MongoDB installed and started"
    else
        echo "⚠️  You can install MongoDB later with: sudo apt install mongodb"
    fi
fi

# Create .env file
echo ""
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created from template"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file and add your credentials!"
    echo "   Run: nano .env"
else
    echo "✅ .env file already exists"
fi

# Generate session (optional)
echo ""
echo "📝 Do you want to generate session string now? (y/n)"
read -r generate_session

if [ "$generate_session" = "y" ] || [ "$generate_session" = "Y" ]; then
    python3 generate_session.py
fi

echo ""
echo "╭─────────────────────────────────────╮"
echo "│    ✅ Setup Complete! ✅           │"
echo "╰─────────────────────────────────────╯"
echo ""
echo "📝 Next Steps:"
echo "   1. Edit .env file: nano .env"
echo "   2. Add your API credentials"
echo "   3. Generate session: python3 generate_session.py"
echo "   4. Run the bot: python3 main.py"
echo ""
echo "💙 Enjoy your Kaoruko Userbot!"
echo ""
