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
    guild = client.get_guild(785871363080060999)
    if message.author != client.user:
        if message.channel.id == 786229115874705418:
            print(message.content)
            splitter = message.content.split()
            roll = splitter[-1]
            name = " ".join(splitter[:-1])
            if check(name, roll):
                channel = client.get_channel(786770781051944971)
                await channel.send(f"Name: {name}\nRoll:{roll}\nRegistered!")
                await message.delete()
                await member.add_roles(guild.get_role(785872750505492501))
            else:
                await channel.send(f"Name: `{name}` and Roll: `{roll}` unmatched")

client.run(token)