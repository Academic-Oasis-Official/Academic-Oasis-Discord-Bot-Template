"""
Eric Beaulne

Example Discord Bot for Academic Oasis
~~~~~~~~~~~~~~~~~~~~~
This is a simple example of a Discord bot using the discord.py library.
It is meant to be used as a template for future bots.
"""

import os
import discord
from discord.ext import commands

# This is the intents that the bot will use.
# It is probably best to start with Intents.default() and add to it as needed.
bot_intents = discord.Intents.default()

# Adding Member intents to the bot (Make sure to enable it in the Discord Developer Portal as well)
bot_intents.members = True

class ExampleBot(commands.Bot):
    """Example Bot

    This will show the basic setup for a bot using the discord.py library.
    It will be the format we will use for the Academic Oasis Discord Bots.
    """

    def __init__(self):
        super().__init__(
            # Command Prefix, when using commands, the bot will look for messages starting with this prefix.
            # This command prefix will likely not be important since we will most likely be using slash commands.
            command_prefix="!",

            # Setting the intents for the bot
            intents=bot_intents,

            # This is the application ID for the bot, it can be found in the Discord Developer Portal
            application_id=int(os.getenv("DISCORD_APPLICATION_ID"))
            )
        
        # Here you can do any other initialization that you need to do.
        # You should probably setup a database here so that It can be used throughout the bot.
        # For Example:
        # self.db = Database()

    async def on_ready(self):
        """On Ready
        
        This is a hook that is called when the bot is ready.
        This will be called after the bot has logged in and is ready to be used.
        
        You should not use this for any setup tasks, instead use the setup_hook.
        """
        print(f"Logged in as {self.user}")

    async def setup_hook(self):
        """Setup Hook

        This is a hook that is called when the bot is ready to be setup.
        This is useful for loading cogs and other setup tasks.
        """

        # Basic Example of loading cogs from the cogs folder.
        # for filename in os.listdir("./cogs"):
        #     if filename.endswith(".py"):
        #         await self.load_extension(f"cogs.{filename[:-3]}")

        # For Testing you should use this instead of the above code.
        await self.load_extension("cogs.example_cog")

        # This is used to tell the bot who the owners of the bot are.
        # This is used for the is_me predicate. (So not very important but definitely useful)
        app_info = await self.application_info()
        if app_info.team:
            self.owner_ids = set([team_member.id for team_member in app_info.team.members])
        else:
            self.owner_ids = set([app_info.owner.id])

        # When testing you will need to do the following for the slash commands to work immediately.
        # If not it could take up to an hour for the slash commands to be registered.
        test_guild = discord.Object(id=int(os.getenv("TEST_GUILD")))
        self.tree.copy_global_to(guild=test_guild)
        await self.tree.sync(guild=test_guild)
