import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Test'):
        msg = 'Everything is Working, leave me alone already,{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTQ3MTc4NjkyMzA5NDE3OTky.D0y_iQ.MePVr3wDgxEZSdzjzvPxoHUxfWc')