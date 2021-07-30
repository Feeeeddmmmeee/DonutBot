import discord
import json
from discord.ext import commands

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["kick"]["aliases"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=f'{member} has been kicked!',
            timestamp=ctx.message.created_at
        )
        embed.set_author(name=self.client.get_user(738788356506386462), url=self.client.get_user(738788356506386462).avatar_url)
        embed.set_footer(text=f"Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)
        
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Kick(client))