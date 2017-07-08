import discord
from discord.ext import commands


def check_permissions(roles, user):
    role = discord.utils.find(lambda r: r.name in roles, user.roles)
    if role:
        return True
    return False


def is_admin():
    return commands.check(lambda ctx: check_permissions(
        'Admin', ctx.message.author
    ))
