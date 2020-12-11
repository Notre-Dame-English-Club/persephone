import discord
from checker import check
from discordvars import guild, verify, role1, role2, log

f = open("token.txt", "r")
token = f.readline()

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:", client.user)

@client.event
async def on_message(message):
    guild = client.get_guild(guild)
    if message.author != client.user:
        if message.channel.id == verify:
            print(message.content)
            splitter = message.content.split()
            roll = splitter[-1]
            name = " ".join(splitter[:-1])
            channel = client.get_channel(log)
            if check(name, roll):
                await channel.send(f"Name: {name}\nRoll:{roll}\nRegistered!\nReference User: <@{message.author.id}>")
                await message.author.add_roles(guild.get_role(role1))
                await message.author.add_roles(guild.get_role(role2))
            else:
                await channel.send(f"Name: `{name}` and Roll: `{roll}` unmatched\nReference User: <@{message.author.id}>")
            await message.delete()

client.run(token)