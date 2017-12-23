from discord import __version__ as d_v
from discord import Embed, Colour
import textwrap
from discord.ext.commands import command


class Core:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        msg = textwrap.dedent(f"""
        =====================================
        Discord Version: {d_v}
        Username: {self.bot.user.name}
        User ID: {self.bot.user.id}
        =====================================""")
        await self.bot.http.send_message(394213627118354444, msg)
        print(msg)

    @command()
    async def feedback(self, ctx, *, suggestion=None):
        if suggestion:
            await ctx.send("Feedback received.")
            feedback_embed = Embed(
                title="Suggestion",
                description=f'Suggestion: *{suggestion} by {ctx.author}*',
                color=Colour.purple()
            )
            await self.bot.get_channel(394216813564526614).send(embed=feedback_embed)
        else:
            await ctx.send("You have not said what your suggestion is.")


def setup(bot):
    bot.add_cog(Core(bot))
