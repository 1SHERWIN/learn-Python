import discord
from discord import Client
from discord.ext import commands


image = "https://i1.wp.com/newkidotblog.com/wp-content/uploads/2018/05/HelloWorld.png?w=1328"
Client: Client = discord.Client()
client = commands.Bot(command_prefix='!')




@Client.event
async def on_ready():
    print('Logged in as:')
    print(Client.user.name)
    print(Client.user.id)

@Client.event
async def on_message(message):
    msg = await Client.send_message(message.channel, " HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD  HELLO WORLD ")
    res = await Client.wait_for_reaction([':👍:', ':👎:'], message=msg)
    await Client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res), embed=e)


@Client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await Client.send_message(channel, "https://i1.wp.com/newkidotblog.com/wp-content/uploads/2018/05/HelloWorld.png?w=1328")
    # 'Hello reactied with World from: goodbye world'.format(user.name, reaction.emoji, reaction.message.channel) )


Client.run("NTE4NDcyODM5MTM4MTE1NTg0.DuRd6g.-xQmINv-UT8gQ0-wAy_2KmMN-r4")
