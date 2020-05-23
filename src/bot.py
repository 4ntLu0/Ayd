import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
AZNBC = os.getenv("AznBc")
client = discord.Client()

bot = commands.Bot(command_prefix="Ayd ")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    print("connected to")
    for guild in client.guilds:
        print(guild)


@bot.command(name="yeet", help="yeets you")
@commands.has_role('DJ')
async def yeet(ctx):
    await ctx.send("I'll yeet u :)")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("you do not have the correct role for this command")


bot.run(TOKEN)
