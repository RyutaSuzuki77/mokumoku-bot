import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

if os.getenv("RAILWAY_ENVIRONMENT") is None:
    load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# botコマンド
@bot.command()
async def start(ctx):
    await ctx.send("もくもくSTART")

@bot.command()
async def rest(ctx):
    await ctx.send("休憩")

@bot.command()
async def restart(ctx):
    await ctx.send("再開")

@bot.command()
async def end(ctx):
    await ctx.send("もくもくEND")

bot.run(TOKEN)