# Housekeeping libraries
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

# Initialize the bot
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# What to do when bot is ready
@bot.event
async def on_ready(self):
    print(f"Ready as {self.user}...")

'''
@param ctx: 
ctx stands for context. It stores all the info about the command that was executed
such as who executed it, the server that was executed in, etc
'''
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# Environment variables
bot_token = os.getenv("BOT_TOKEN")

bot.run(bot_token)