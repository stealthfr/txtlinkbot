import discord
from discord.ext import commands

# Set up the bot with command prefix and intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your channel ID
target_channel_id = 123456789012345678

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Check if the message is in the specific channel and contains a file
    if message.channel.id == target_channel_id and message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith('.txt'):
                # Send the attachment URL wrapped in triple backticks as a response
                await message.channel.send(f"```\n{attachment.url}\n```")
                break

    # Allow commands to be processed
    await bot.process_commands(message)

# Replace 'your_token_here' with your actual bot token
bot.run('your_token_here')
