import discord
import openai
import os

# Load environment variables from GitHub Secrets
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Ensure that environment variables are loaded correctly
if DISCORD_TOKEN is None:
    raise ValueError("DISCORD_TOKEN is not set. Please check your GitHub Secrets.")
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY is not set. Please check your GitHub Secrets.")

# Initialize a client object for Discord bot with the required intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
client = discord.Client(intents=intents)

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function that sends a message to the OpenAI API and gets a response
async def ask_gpt(message_content):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": message_content}
        ]
    )
    answer = response.choices[0].message['content']
    return answer

# Listener that checks for messages in Discord
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Sends message to OpenAI API
    response = await ask_gpt(message.content)
    # Sends response back to channel
    await message.channel.send(response)

# Event listener for when the bot is ready
@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')

# Start the bot
client.run(DISCORD_TOKEN)

