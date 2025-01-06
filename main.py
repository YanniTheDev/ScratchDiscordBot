import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run("MTMyNDYzMDg5ODA4NzU1OTIzOQ.GbsoGN.I1KdQqmDajnfLkjKHZJTaKO_UgtYREMjXkUa1M")