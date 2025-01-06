import discord
from discord.ext import commands

# Initialize the bot
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# What to do when bot is ready
@bot.event
async def on_ready():
    print("Ready!")

    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands")
    except Exception as e:
        print(f"An error occured: {e}")

@bot.tree.command(name="hello", description="Greets you with a hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}")

# Environment variables
with open("token.txt") as token_file:
    token = token_file.read()

bot.run(token=token)