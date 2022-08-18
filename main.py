# Imports #

import nextcord                                 # pip install nextcord #
from nextcord.ext import commands
from nextcord import Intents

import os

# Define 'client' #

client = commands.Bot(
    command_prefix="!",                         # Bot Prefix, you can use whatever you want#
    case_insensitive=True,                      # Make the Bot case-insensitive #
    intents=nextcord.Intents.all()              # Make sure to activate the Intents at https://discord.com/developers/applications/YOUR_BOT_ID/bot #
)



# on_ready event #

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(
        activity = nextcord.Game(name = "a Game")    # The Discord Bot's Game #
    )


# Cog Loader #
# Make sure you have a Folder called "cogs" in the same Folder as "main.py" #
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}")


# client.run #

client.run(TOKEN)  # Run the Bot with your Bot Token #
