from discord.ext import commands
import discord


class Fame:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def halloffame(self, ctx, user: discord.Member):
        """Get added to the Hall Of Fame"""
        fame = discord.Embed(
            title="Entry to the Hall of Fame"
        )
        fame.add_field(
            name="User",
            value=f"{user}"
        )
        fame.set_thumbnail(
            url=user.avatar_url
        )
        channel = ctx.guild.get_channel(394215397647319050)
        await channel.send(embed=fame)


def setup(bot):
    bot.add_cog(Fame(bot))
