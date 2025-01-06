import os

import discord
from dotenv import load_dotenv

load_dotenv()

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        # Checks to see if the bot has sent a message by itself
        if message.author == self.user:
            return

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

# Environment variables
bot_token = os.getenv("BOT_TOKEN")

client.run(bot_token)