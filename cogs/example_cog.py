"""
Eric Beaulne

Example Cog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is an example cog that shows how to create a cog.
"""

import discord
from discord import app_commands
from discord.ext import commands

class ExampleCog(commands.Cog, name="Example"):
    """Example Cog
    
    This is an example cog that shows how to create a cog.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="ping", # The name of the command
        description="Basic ping command! Will respond with Pong!"
    )
    async def example_command(self, interaction: discord.Interaction):
        """Example Command
        
        As you can see I define the Async Function with the app_commands.command decorator.
        The name argument sets the name of the command. By default it will use the function name.
        Therefore even though the function name is example_command, the command name will be ping.
        """

        await interaction.response.send_message("Pong!")

async def setup(bot: commands.Bot):
    """Setup
    
    This is the setup function for the cog.
    It will be called when the cog is loaded using bot.load_extension().
    If you are using bot.add_cog() then this function will not be called.
    """
    await bot.add_cog(ExampleCog(bot))
