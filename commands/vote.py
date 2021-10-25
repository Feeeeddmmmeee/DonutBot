import discord
import json
from discord.ext import commands

class Vote(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["vote"]["aliases"])
    async def vote(self, ctx):

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Vote for Donut on Top.gg!",
            description="Click [[this]](https://top.gg/bot/self.client.user.id/vote) link to vote!",
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)

        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Vote(client))