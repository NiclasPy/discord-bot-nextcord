# Imports #

import nextcord
from nextcord.ext import commands


class cog(commands.Cog, name='cog'):
    def __init__(self, client):
        self.client = client
       
    @commands.command()
    @commands.is_owner()
    async def hello(self, ctx):
        await ctx.send("Hi")
            


def setup(client):
    client.add_cog(cog(client))