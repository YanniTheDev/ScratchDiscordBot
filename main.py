import os

import discord
from dotenv import load_dotenv

load_dotenv()

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

# Environment variables
bot_token = os.getenv("BOT_TOKEN")

client.run(bot_token)