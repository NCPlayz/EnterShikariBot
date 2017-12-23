from pathlib import Path
from discord.ext import commands
import discord
import os
import asyncio


class Bot(commands.Bot):
    """This is the class that initializes the bot."""
    def __init__(self):
        self.presence = discord.Game(name='The Spark | -help'
                                     , url="https://www.twitch.tv/twitchpresents", type=1)

        def get_prefix():
            """Fetches all known prefixes."""
            return ["TS ",
                    "-"]

        def get_game():
            """Fetches game presence."""
            return self.presence

        super().__init__(command_prefix=get_prefix(), game=get_game(), description="The Spark", pm_help=None,
                         help_attrs=dict(hidden=True))

        startup_extensions = [x.stem for x in Path('cogs').glob('*.py')]
        for extension in startup_extensions:
            try:
                self.load_extension(f'cogs.{extension}')
            except Exception as e:
                error = f'{extension}\n {type(e).__name__}: {e}'
                print(f'Failed to load extension {error}')

    def run(self, *args, **kwargs):
        token = os.environ['TOKEN']
        try:
            self.loop.run_until_complete(super().start(token, *args, **kwargs))
        except KeyboardInterrupt:
            self.loop.run_until_complete(self.logout())
            pending = asyncio.Task.all_tasks(loop=self.loop)
            gathered = asyncio.gather(*pending, loop=self.loop)
            try:
                gathered.cancel()
                self.loop.run_until_complete(gathered)
                gathered.exception()
            except:
                pass
        finally:
            self.loop.close()


if __name__ == '__main__':
    Bot().run()
