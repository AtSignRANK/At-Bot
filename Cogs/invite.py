# Link : https://discord.com/api/oauth2/authorize?client_id=864547565050658858&permissions=8&scope=bot%20applications.commands

import discord

from discord.ext import commands
from discord_slash import SlashContext, cog_ext

def setup(bot):
    bot.add_cog(Invite(bot))


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.link = "https://discord.com/api/oauth2/authorize?client_id=864547565050658858&permissions=8&scope=bot%20applications.commands"
    

    @cog_ext.cog_slash(name="invite", description="초대 링크를 받을 수 있습니다!")
    async def invite(self, ctx: SlashContext):
        await ctx.defer(True)
        await ctx.send(f"This is {self.bot} invite link! {self.link}")