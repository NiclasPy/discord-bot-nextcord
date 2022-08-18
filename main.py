# Imports #

import nextcord                                 # pip install nextcord #
from nextcord.ext import commands
from nextcord import Intents



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


# Our first Command! #

@client.command()
async def test(ctx):
    await ctx.send("Worked!")


# client.run #

client.run(DISCORD_BOT_TOKEN)  # Run the Bot with your Bot Token #