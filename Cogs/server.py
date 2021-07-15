import discord, psutil

from discord.ext import commands
from discord_slash import SlashContext, cog_ext

def setup(bot):
    bot.add_cog(Server(bot))


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.GB = 1024 ** 3
        self.owner_id = 689283707055636554
    
    @cog_ext.cog_slash(name="server", description="You Can See Server of Bot Owner's Server")
    async def server(self, ctx: SlashContext):
        if ctx.author_id != self.owner_id:
            await ctx.defer(hidden=True)
            await ctx.send(content="You are not able to use this command!")
            return
        embed = discord.Embed(name="**Server**", description=f"Show Server Of {self.bot.user.name}", color=0x777777)
        embed.add_field(name="CPU", value=f"CPU {psutil.cpu_percent()}% Used", inline=False)
        disk = psutil.disk_usage("C:")
        embed.add_field(name="DISK", value=f"DISK {disk.used // self.GB} / {disk.total // self.GB} GB Used", inline=False)
        ram = psutil.virtual_memory()
        embed.add_field(name="RAM", value=f"RAM {ram.available // self.GB} / {ram.total // self.GB} GB Used", inline=False)
        await ctx.send(embed=embed)