import discord

from discord.ext import commands
from discord_slash import SlashContext, cog_ext


def setup(bot):
    bot.add_cog(Anonymity(bot))


class Anonymity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @cog_ext.cog_slash(name="anonymity", description="익명으로 채팅을 남길 수 있습니다!")
    async def anonymity(self, ctx: SlashContext, text: str):
        log = open("anonymity.log", "a", encoding="utf-8")
        log.write(f"{ctx.author} : {text}\n")
        log.close()
        await ctx.defer(True)
        if text.__contains__("ㅗ"):
            await ctx.send("유해하다 판단 되어 취소하였습니다.")
            return
        elif text.__contains__("ㅅㅂ"):
            await ctx.send("유해하다 판단 되어 취소하였습니다.")
            return
        elif text.__contains__("시발"):
            await ctx.send("유해하다 판단 되어 취소하였습니다.")
            return
        elif text.__contains__("씨발"):
            await ctx.send("유해하다 판단 되어 취소하였습니다.")
            return
        elif text.__contains__("ㅆㅂ"):
            await ctx.send("유해하다 판단 되어 취소하였습니다.")
            return
        elif text.__contains__("fuck"):
            await ctx.send("유해하다 판단 되어 취소하였습니다.")
            return
        elif text.__contains__("데이트"):
            await ctx.send("커플이라 판단 되어 취소하였습니다... ㅂㄷㅂㄷ 딱대...")
            return
        await ctx.send(f"{ctx.author} : {text}")
        await ctx.channel.send(f"[ 익명 ] {text}")