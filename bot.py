import discord
from discord.ext import commands

intents = discord.Intents.all()

file = open("/home/tux/Discord/bot-files/BOT_token.txt", "r")
token = file.read()
file.close()

bot = commands.Bot(command_prefix='!', intents=intents)

# Event that triggers when the bot has connected to Discord
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Command that responds to "ping" with "pong"
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
