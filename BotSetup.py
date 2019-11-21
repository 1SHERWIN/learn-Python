import discord
from discord.ext import commands


help_attrs = dict(hidden=True)
Client = discord.Client()
client = commands.Bot(command_prefix='!')




@Client.event
async def on_ready():
   print('Logged in as:')
   print(Client.user.name)
   print(Client.user.id)




Client.run("NTE4NDcyODM5MTM4MTE1NTg0.DuRd6g.-xQmINv-UT8gQ0-wAy_2KmMN-r4")
