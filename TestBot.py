import random
import os
import discord
from discord.ext.commands import Bot
name = 'TestBot'

BOT_PREFIX = "."

client = Bot(command_prefix=BOT_PREFIX)

players = {}

# Eight Ball command, Tells your future
@client.command()
async def eightball():
    possible_responses = [
        'Thvtt is a no form me',
        'It is not lookvklng llkely',
        "It is quite possivle",
        'I fucikng havte u sterbv.',
    ]
    await client.say(random.choice(possible_responses))

# Adds Role "Test" To a user on Join
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Test')
    await client.add_roles(member, role)
    for channel in member.server.channels:
        if channel.name == 'general':
             await client.send_message( channel, "Welcome to Sterben's test server!, "
                                                 "Here he will scream about why his bot doesn't work!")


# Post random image from path variable
@client.command(pass_context=True)
async def poi(ctx):
    path = r"C:\Users\kicky\Desktop\Poi"
    channel = ctx.message.channel
    choice = os.path.join(path, random.choice(os.listdir(path)))
    await client.send_file(channel, choice)

# Deletes set amount of messages in channel where command is called
@client.command(pass_context=True)
async def purge(ctx, amount=5):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Sefi habve entruted the buildifing')

# Plays music using Youtube_dl
@client.command(pass_context=True)
async def play (ctx, url):
    channel = ctx.message.author.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

# Leaves current voice channel
@client.command(pass_context=True)
async def leave (ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if name == 'TestBot':
    import secret
    client.run(secret.TOKEN)
