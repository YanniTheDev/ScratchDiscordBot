# Housekeeping libraries
import os
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord.ext import commands

load_dotenv()

class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        # Checks to see if the bot has sent a message by itself
        if message.author == self.user:
            return

intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix="?", intents=intents)

@client.tree.command(name="hi", description="Say hello!")
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")

# Environment variables
bot_token = os.getenv("BOT_TOKEN")

client.run(bot_token)