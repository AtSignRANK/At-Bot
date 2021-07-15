import discord

from discord.ext import commands
from discord_slash import cog_ext, SlashContext

def setup(bot):
    bot.add_cog(Help(bot))

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x777777
        self.owner_id = 689283707055636554
    
    @cog_ext.cog_slash(name="help", description="도움말을 보세요!")
    async def help(self, ctx: SlashContext):
        embed = discord.Embed(title="**Help**", description="Commands Help", color=self.color)
        embed.add_field(name="help", value="도움말을 볼 수 있습니다!")
        embed.add_field(name="anonymity", value="익명 채팅을 사용하실 수 있습니다!")
        if ctx.author_id == self.owner_id:
            embed.add_field(name="list", value="Cogs 파일 내에 있는 파일/폴더를 출력합니다.")
            embed.add_field(name="load", value="Cogs 파일 내에 있는 Python 파일을 로드합니다.")
            embed.add_field(name="reload", value="Cogs 파일 내에 있는 Python 파일을 리로드합니다.")
        
        await ctx.send(embed=embed)