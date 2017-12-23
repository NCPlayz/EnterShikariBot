from discord.ext.commands import command
import discord
import asyncio


class Mod:
    def __init__(self, bot):
        self.bot = bot

    def __local_check(self, ctx):
        return discord.utils.get(ctx.guild.roles, name="Mindsweepers [Mods]") in ctx.message.author.roles


    @command()
    async def kick(self, ctx, member: discord.Member, *, reason: str="Violation of one or more rules."):
        """Kick a user."""
        await member.send(f'You have been kicked for the following issue:\n{reason}')
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member} | Reason: {reason}')

    @command()
    async def ban(self, ctx, member: discord.Member, *, reason: str="Violation of one or more rules."):
        """Ban a user."""
        await member.send(f'You have been kicked for the following issue:\n{reason}')
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member} | Reason: {reason}')

    @command()
    async def softban(self, ctx, member: discord.Member, *, reason: str="Violation of one or more rules."):
        """Softban a user."""
        await member.send(f'You have been softbanned for the the following issue:\n{reason}')
        await member.ban(reason=reason, delete_message_days=2)
        await member.unban()
        await ctx.send(f'Softbanned {member} | Reason: {reason}')

    @command()
    async def hackban(self, ctx, member_id: int, *, reason: str="Violation of one or more rules."):
        """Ban a user."""
        member_id = discord.Object(member_id)
        await ctx.guild.ban(user=member_id, reason=reason)
        await ctx.send(f'Banned {member_id.name}')

    @command()
    async def purge(self, ctx, count: int):
        """Purge an amount of messages from a channel."""
        if count <= 1:
            msg = ctx.send('Please input a valid number of messages.')
            await asyncio.sleep(8)
            await msg.delete()
        elif count >= 1:
            deleted_messages = await ctx.channel.purge(limit=(count + 1))
            message_number = max((len(deleted_messages) - 1), 0)
            resp = 'Deleted `{} message{}` 👌 '.format(message_number, ('' if (message_number < 2) else 's'))
            confirm_message = await ctx.send(resp)
            await asyncio.sleep(8)
            await confirm_message.delete()


def setup(bot):
    bot.add_cog(Mod(bot))