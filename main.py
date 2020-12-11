import discord
from checker import check

f = open("token.txt", "r")
token = f.readline()

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:", client.user)

@client.event
async def on_message(message):
    guild = client.get_guild(738466199263903792)
    if message.author != client.user:
        if message.channel.id == 738653551064121354:
            print(message.content)
            splitter = message.content.split()
            roll = splitter[-1]
            name = " ".join(splitter[:-1])
            if check(name, roll):
                channel = client.get_channel(786787040774979585)
                await channel.send(f"Name: {name}\nRoll:{roll}")
                await message.delete()
            else:
                print("sad")

client.run(token)