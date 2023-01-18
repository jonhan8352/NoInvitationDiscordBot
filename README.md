# NoInvitationDiscordBot

We are going to create a simple Discord bot that sends a warning message when a member invites others to a YouTube channel, another Discord server, or a Twitch channel, except the server owner or administrators.

First of all, let's import the Discord library.

```
import discord
from discord import Message
```

Let's say we also need to verify whether the Discord bot successfully executed, we also need to add following lines in the code.

```
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
```

Now, here is the most important part of the code. It will verify the message if it contain the URL of Youtube or Discord or Twitch. If it found the message containing the prohibited URL, the bot will send a warning message.

```
@bot.event
async def on_message(message: Message):
    if message.author.bot:
        return
    if not message.author.guild_permissions.administrator:
        if "youtube.com" in message.content or "discord.gg" in message.content or "discordapp.com/invite" in message.content or "twitch.tv" in message.content:
            await message.channel.send("Please do not post links to other YouTube, Discord or Twitch channels here.")
```

And finally at the end of the Python script, please add the Discord bot token in order for the Python script to verify the Discord bot's token.

```
bot.run('YOUR_BOT_TOKEN')
```
