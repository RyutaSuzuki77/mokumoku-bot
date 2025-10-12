import discord
import os
from discord import app_commands
from dotenv import load_dotenv

if os.getenv("RAILWAY_ENVIRONMENT") is None:
    load_dotenv()

if os.getenv("DISABLE_BOT") == "true":
    print("Bot is disabled in this environment.")
    exit()

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await tree.sync()  # コマンドをDiscordに同期

@tree.command(name="start", description="もくもく学習を開始します")
async def start_command(interaction: discord.Interaction):
    user_name = interaction.user.name
    await interaction.response.send_message(f"{user_name} もくもく開始")

@tree.command(name="end", description="もくもく学習を終了します")
async def end_command(interaction: discord.Interaction):
    user_name = interaction.user.name
    await interaction.response.send_message(f"{user_name} もくもく終了")

@tree.command(name="total", description="学習時間の合計を表示します")
async def total_command(interaction: discord.Interaction):
    user_name = interaction.user.name
    await interaction.response.send_message(f"{user_name} の学習時間合計(8月)：10時間30分")

client.run(TOKEN)