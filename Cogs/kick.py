import discord

from discord.ext import commands
from discord_slash import SlashContext, cog_ext


def setup(bot):
    bot.add_cog(Kick(bot))


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @cog_ext.cog_slash(name="kick", description="Kick User")
    async def kick(self, ctx: SlashContext, user: discord.User or discord.User.mention is None, reason: str = None):
        if not ctx.author.guild_permissions.administrator:
            await ctx.defer(True)
            await ctx.send("당신은 사람을 추방할 수 없습니다!")
            return
        await ctx.guild.kick(user=user, reason=reason)
        kickembed = discord.Embed(title=":no_entry: **Kick**", description=f"You are Kicked in {ctx.guild.name}!", color=0x777777)
        kickembed.add_field(name="Reason", value=reason, inline=False)
        await user.send(embed=kickembed)
        embed = discord.Embed(title="**Kick**", description=f"{user} kicked!")
        embed.add_field(name="Reason", value=reason, inline=False)
        await ctx.send(embed=embed)