import discord
from discord.ext import commands

# Initialize the bot
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# What to do when bot is ready
@bot.event
async def on_ready():
    print("Ready!")

'''
@param ctx: 
ctx stands for context. It stores all the info about the command that was executed
such as who executed it, the server that was executed in, etc
'''
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

# Environment variables
with open("token.txt") as token_file:
    token = token_file.read()

bot.run(token=token)