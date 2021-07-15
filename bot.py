import discord, os

from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix="/")
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

botVersion = "Beta 2.0.5"

main_local = "AtBot/"
settings_local = f"{main_local}BotSettings.txt"

token = open(settings_local, "r", encoding="utf-8").read().split()[0]
owner_id = int(open(settings_local, "r", encoding="utf-8").read().split()[1])

for filename in os.listdir(f"{main_local}Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f'Bot Activate')
    print(f'ID : {bot.user.id}')
    print(f'Name : {bot.user.name}')
    print(f'Tag : #{bot.user.discriminator}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("/help 를 입력해보세요!"))
    # discord.Status.online = 온라인
    # discord.Status.dnd = 다른 용무 중
    # discord.Status.offline = 오프라인
    print(f'Bot Start')


@slash.slash(name="version", description="You Can See Version of Bot")
async def version(ctx: SlashContext):
    embed = discord.Embed(name="**Version**", description=f"Show Version Of {bot.user.name}", color=0x777777)
    embed.add_field(name="Bot Version", value=f"{bot.user.name} ver {botVersion}")
    await ctx.send(embed=embed)


@slash.slash(name="list", description="Show Python File List in Cogs")
async def cogslist(ctx: SlashContext):
    if ctx.author_id == owner_id:
        embed = discord.Embed(name="List", description="Python File List", color=0x777777)
        for file in os.listdir(f"{main_local}Cogs"):
            if file.endswith(".py"):
                embed.add_field(name=f"{file}", value="Python File")
        
        await ctx.send(embed=embed)


@slash.slash(name="reload", description="Reload Python File")
async def reload(ctx: SlashContext, file_name: str = None):
    if ctx.author_id == owner_id:
        if file_name == None:
            for file in os.listdir(f'{main_local}Cogs'):
                if file.endswith('.py'):
                    bot.unload_extension(f'Cogs.{file[:-3]}')
                    bot.load_extension(f'Cogs.{file[:-3]}')
            await ctx.send(f"{bot.user.name} Reloaded.")
            print("Reloaded Completely")
        else:
            if not os.listdir(f"{main_local}Cogs").__contains__(file_name):
                await ctx.send(f"{bot.user.name}'s file {file_name} Reload Failed.")
                return
            bot.unload_extension(f"Cogs.{file_name[:-3]}")
            bot.load_extension(f"Cogs.{file_name[:-3]}")
            await ctx.send(f"{bot.user.name}'s file {file_name} Reloaded.")
            print(f"{file_name} Reloaded Completely")
        
    else:
        mention = f"<@!{ctx.author_id}>"
        await ctx.send(f"{mention} You can't reload!")


@slash.slash(name="load", description="Load Python File")
async def load(ctx: SlashContext, file_name: str):
    if ctx.author_id == owner_id:
        bot.load_extension(f'Cogs.{file_name}')
        await ctx.send(f"{bot.user.name} Loaded.")
        print("Loaded Completely")
        
    else:
        mention = f"<@!{ctx.author_id}>"
        await ctx.send(f"{mention} You can't load!")


bot.run(token)