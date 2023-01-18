# NoInvitationDiscordBot

We are going to create a simple Discord bot that sends a warning message when a member invites others to a YouTube channel, another Discord server, or a Twitch channel, except the server owner or administrators.

First of all, let's import the Discord and OS library. The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc. Instead of putting the token in the script, we will use OS module to retrieve the bot token.

```
import discord
import os
from discord import Message
```

Let's use the keep_alive library with following code.

```
from keep_alive import keep_alive
```

Let's say we also need to verify whether the Discord bot successfully executed, we need to add following lines in the code. It will prompt the messsage on the console screen.

```
client = discord.Client()

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

We will need to use following code to enable the bot to stay alive.

```
keep_alive()
```

And finally at the end of the Python script, please add the Discord bot token in order for the Python script to verify the Discord bot's token.

```
client.run(os.getenv('your_secret_token_key'))
```
