import asyncio

import discord
from discord.ext import commands

from .server import HttpRequestHandler


class Loader(object):
    def __init__(self, command_prefix, description, formatter):
        self.bot = commands.Bot(
            command_prefix=command_prefix,
            description=description,
            formatter=formatter
        )

    def load_commands(self, class_bot):
        self.bot.add_cog(class_bot(self.bot))

    def load(self, discord_token, bonobot_token, url, port, Action, debug):
        loop = asyncio.get_event_loop()
        f = loop.create_server(
                lambda: HttpRequestHandler(
                    debug=debug,
                    keep_alive=75,
                    client=self.bot,
                    action=Action,
                    token=bonobot_token),
                url, port)
        srv = loop.run_until_complete(f)
        asyncio.ensure_future(self.bot.start(discord_token))
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            loop.close()
