"""
Eric Beaulne

Example Main File
~~~~~~~~~~~~~~~~~~~~~
This file shows you what the main file would look like for the bot.
"""

import os
import discord
from discord import app_commands
from discord.ext import commands

# You want to make sure to load your .env file before you create the bot.
# This step is very important for safety and for functionality.
# If you do not have a .env file, you can create one by copying the .env.example file.
from dotenv import load_dotenv
load_dotenv()

from example_bot import ExampleBot

bot = ExampleBot()

def is_me():
    """Is Me
    
    This is a predicate that will check if the interaction is from the owner(s) of the bot."""
    def predicate(interaction: discord.Interaction) -> bool:
        return interaction.user.id in bot.owner_ids
    return app_commands.check(predicate)


# Commands put in the main file should be used for commands that only admins should use.
# Commands that are used by everyone should be put in a cog.
# For Example, the load, unload, and reload commands are only used by admins.
@bot.tree.command()
@is_me()
@app_commands.describe(
    cog_name="The cog to load",
)
async def load(interaction: discord.Interaction, cog_name: str):
    """Load
    
    This command will load the cog."""
    try:
        await bot.load_extension(f"cogs.{cog_name}")
        await interaction.response.send_message("Loaded")
    except commands.ExtensionNotFound:
        await interaction.response.send_message("Cog Not Found")
    except commands.ExtensionAlreadyLoaded:
        await interaction.response.send_message("Cog Already Loaded")

@bot.tree.command()
@is_me()
@app_commands.describe(
    cog_name="The cog to unload",
)
async def unload(interaction: discord.Interaction, cog_name: str):
    """Unload
    
    This command will unload the cog."""
    try:
        await bot.unload_extension(f"cogs.{cog_name}")
        await interaction.response.send_message("Unloaded")
    except commands.ExtensionNotFound:
        await interaction.response.send_message("Cog Not Found")
    except commands.ExtensionNotLoaded:
        await interaction.response.send_message("Cog Not Loaded")

@bot.tree.command()
@is_me()
@app_commands.describe(
    cog_name="The cog to reload",
)
async def reload(interaction: discord.Interaction, cog_name: str):
    """Reload
    
    This command will unload and then load the cog."""
    try:
        await bot.unload_extension(f"cogs.{cog_name}")
    except commands.ExtensionNotFound:
        await interaction.response.send_message("Cog Not Found")
        return
    except commands.ExtensionNotLoaded:
        await interaction.response.send_message("Cog Not Loaded")
        return
    await bot.load_extension(f"cogs.{cog_name}")
    await interaction.response.send_message("Reloaded")

if __name__ == "__main__":
    # When we actually run the bot we want to make sure it is in the __name__ == "__main__" block.
    # In the case that a different file is importing this file, we do not want to run the bot.
    # Since it will most likely be running in a different file.
    bot.run(os.getenv("DISCORD_TOKEN"))
