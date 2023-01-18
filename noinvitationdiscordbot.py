import discord
from discord import Message

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message: Message):
    if message.author.bot:
        return
    if not message.author.guild_permissions.administrator:
        if "youtube.com" in message.content or "discord.gg" in message.content or "discordapp.com/invite" in message.content or "twitch.tv" in message.content:
            await message.channel.send("Please do not post links to other YouTube, Discord or Twitch channels here.")

bot.run('YOUR_BOT_TOKEN')