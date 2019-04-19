import random
import discord
from discord.ext.commands import Bot
name = 'TestBot'

BOT_PREFIX = "."

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def eight_ball():
    possible_responses = [
        'That is a no from me',
        'It is not looking likely',
        "It is quite possible",
        'Row Row Fight The Power',
    ]
    await client.say(random.choice(possible_responses))

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Test')
    await client.add_roles(member, role)
    for channel in member.server.channels:
        if channel.name == 'general':
             await client.send_message( channel, "Welcome to Sterben's test server!, "
                                                 "Here he will scream about why his bot doesn't work!")

@client.command(pass_context=True)
async def purge(ctx, amount=5):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Sesi has entered the building')





@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if name == 'TestBot':
    import secret
    client.run(secret.TOKEN)
