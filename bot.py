import discord
from discord.ext import commands
import os
import datetime

# Your bot's token
TOKEN = 'BOT_TOKEN_HERE'

# Intents for your bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True  # Enable this if you need member-related events

# Your bot's command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
    # Get the current date in MM-DD-YYYY format
    current_date = datetime.datetime.now().strftime('%m-%d-%Y')
    
    # Construct the folder path for the current date
    your_base_folder = os.path.join(os.path.expanduser('~/xur'), current_date)
    
    # Check if the folder for the current date exists
    if os.path.exists(your_base_folder):
        # Read the content of inventory.txt
        inventory_path = os.path.join(your_base_folder, 'inventory.txt')
        with open(inventory_path, 'r') as inventory_file:
            inventory_text = inventory_file.read()
        
        # Read the content of location.txt
        location_path = os.path.join(your_base_folder, 'location.txt')
        with open(location_path, 'r') as location_file:
            location_text = location_file.read()
        
        # Get the "💰where-is-xûr" channel
        channel_name = "💰where-is-xûr"
        target_channel = discord.utils.get(bot.get_all_channels(), name=channel_name)
        
        if target_channel:
            # Send the messages to the specific channel
            await target_channel.send(inventory_text)
            await target_channel.send(location_text)
            await target_channel.send("GO!")
        else:
            print(f"Channel '{channel_name}' not found!")
    else:
        print(f"No data available for {current_date}")

    # Close the bot after sending the messages
    await bot.close()

# Start the bot
bot.run(TOKEN)
