import discord
from discord.ext import commands
from config import TOKEN
from luau_processor import modify_luau_script
from downloader import download_vm
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    download_vm()

@bot.command(name="upload")
async def upload(ctx):
    await ctx.send("📄 Upload your Luau file (.lua or .txt).")

@bot.event
async def on_message(message):
    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith((".lua", ".txt")):
                filename = "uploaded_" + attachment.filename
                await attachment.save(fp=filename)

                with open(filename, "r", encoding="utf-8", errors="ignore") as f:
                    original = f.read()

                modified = modify_luau_script(original)

                result_filename = "modified_" + attachment.filename
                with open(result_filename, "w", encoding="utf-8") as f:
                    f.write(modified)

                await message.channel.send(
                    "✅ File processed! Here's your modified file:",
                    file=discord.File(result_filename)
                )

                os.remove(filename)
                os.remove(result_filename)
    await bot.process_commands(message)
