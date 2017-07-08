import json

import os.path

import discord
from discord.ext.commands.formatter import HelpFormatter
from discord.ext import commands

from .admin import Admin
from .fun import Fun
from .loader import Loader

# On charge les variables de config
with open(os.path.dirname(
    os.path.abspath(__file__)
) + '/config.json') as config_file:
    config = json.load(config_file)


class customHelpFormatter(HelpFormatter):
    def get_ending_note(self):
        command_name = self.context.invoked_with
        return "Écrivez {0}{1} pour plus d'information sur une commande.\n" \
               "Vous pouvez également écrire {0}{1} pour plus d'information " \
               "sur une catégorie.".format(self.clean_prefix, command_name)


loader = Loader('?', config['description'], customHelpFormatter())

loader.bot.load_extension('L2p_bot.admin')
loader.bot.load_extension('L2p_bot.fun')


@loader.bot.event
async def on_ready():
    print('Connected!')
    print('Username: ' + loader.bot.user.name)
    print('ID: ' + loader.bot.user.id)


loader.load(
    config['discord_token'],
    config['bonobot_token'],
    'localhost',
    8080,
    True
)
