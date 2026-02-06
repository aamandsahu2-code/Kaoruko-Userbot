#!/usr/bin/env python3
"""
Session String Generator for Kaoruko Userbot
Run this to generate your SESSION_STRING
"""

import asyncio
import sys
from pyrogram import Client
from pyrogram.errors import (
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

print("""
╭─────────────────────────────────────╮
│                                     │
│    💙 Kaoruko Userbot 💙           │
│    Session String Generator         │
│                                     │
╰─────────────────────────────────────╯
""")

print("⚠️  IMPORTANT NOTES:")
print("   • Phone number with country code (e.g., +1234567890)")
print("   • You will receive a code via Telegram")
print("   • If 2FA enabled, you'll need your password")
print("   • Keep the session string PRIVATE!\n")

API_ID = input("Enter your API_ID: ").strip()
API_HASH = input("Enter your API_HASH: ").strip()

if not API_ID or not API_HASH:
    print("\n❌ API_ID and API_HASH are required!")
    print("   Get them from: https://my.telegram.org\n")
    sys.exit(1)

try:
    API_ID = int(API_ID)
except ValueError:
    print("\n❌ API_ID must be a number!")
    print("   Example: 12345678\n")
    sys.exit(1)

print("\n⏳ Connecting to Telegram...\n")

async def main():
    try:
        client = Client(
            name="kaoruko_session",
            api_id=API_ID,
            api_hash=API_HASH,
            in_memory=True
        )
        
        async with client:
            # Get user info to verify
            me = await client.get_me()
            
            # Export session string
            session_string = await client.export_session_string()
            
            print("\n" + "="*70)
            print("\n✅ Session string generated successfully!\n")
            print("👤 Logged in as:")
            print(f"   Name: {me.first_name}")
            if me.username:
                print(f"   Username: @{me.username}")
            print(f"   User ID: {me.id}")
            print("\n" + "="*70)
            print(f"\n{session_string}\n")
            print("="*70)
            
            print("\n📝 NEXT STEPS:")
            print("   1. Copy the session string above")
            print("   2. Open your .env file")
            print("   3. Paste it as: SESSION_STRING=<paste_here>")
            print("   4. Also add your User ID as: OWNER_ID=" + str(me.id))
            print("\n⚠️  SECURITY WARNING:")
            print("   • Never share this session string with anyone!")
            print("   • It gives full access to your Telegram account!")
            print("   • Keep your .env file private!\n")
            
            # Ask if user wants to save to file
            save = input("💾 Save to session.txt file? (y/n): ").strip().lower()
            if save == 'y':
                with open("session.txt", "w") as f:
                    f.write(session_string)
                print("✅ Saved to session.txt\n")
            
    except PhoneNumberInvalid:
        print("\n❌ Error: Invalid phone number!")
        print("   Use format: +1234567890 (with country code)\n")
        sys.exit(1)
        
    except PhoneCodeInvalid:
        print("\n❌ Error: Invalid verification code!")
        print("   Make sure you entered the code correctly.\n")
        sys.exit(1)
        
    except PhoneCodeExpired:
        print("\n❌ Error: Verification code expired!")
        print("   Run the script again to get a new code.\n")
        sys.exit(1)
        
    except SessionPasswordNeeded:
        print("\n❌ Error: Two-step verification is enabled!")
        print("   The script will ask for your password.\n")
        sys.exit(1)
        
    except PasswordHashInvalid:
        print("\n❌ Error: Invalid password!")
        print("   Make sure you entered your 2FA password correctly.\n")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("\nCommon issues:")
        print("   • Invalid API_ID or API_HASH")
        print("   • Network connection problems")
        print("   • Telegram server issues")
        print("\nTry again or check your credentials.\n")
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n❌ Session generation cancelled by user!")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        sys.exit(1)