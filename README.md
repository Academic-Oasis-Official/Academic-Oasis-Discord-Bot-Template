# Academic Oasis Discord Bot Template

Hi, I am Eric and I am your **CTO** and this is the template I have made for you guys to follow.  
This should show you how to get started with making a default discord bot using [**Discord.py**](https://discordpy.readthedocs.io/en/stable/) along with the format you will have to follow.
 
## Getting Started

Before we can actually run the bot we need to make the bot user.

### Creating the Bot User

To start go to the [**Discord Developer Portal**](https://discord.com/developers/applications), Login and then click on **New Application**.  

Give it a name and make sure the Team is set to Personal (See [Note 1](#note-1)) and click **Create**

Copy down the **Application ID**.

Now go to the **Bot** tab click **Reset Token** and enter your 2FA Code.  
Once you get the token copy it down and keep it safe because if you forget it you will have to reset it again.

For testing reasons make sure to uncheck the **Public Bot** Option.

Scroll down and select any **Gateway Intents** you might need and then you should be complete this part.

### Inviting the bot to a server.

Make a Bot Testing Server for this.

Go to the **OAuth2** Tab, and go to url generator.

Select both **bot** and **applications.commands**.

Select the permissions the Bot Needs (See [Note 2](#note-2)).

Scroll to the bottom and click **Copy** next to the url it generated.

Put the URL into your tab and Login if asked, select the server and keep confirming until it has joined the server.

## Using the Template

First off make the **.env** file and copy the things from the [.env.example](.env.example) to it
Simply copy and paste or rewrite from the Template. If you need help contact me.
The files should be quite heavily commented. Now I don't want your code to be looking over commented, I did it to really explain everything.

You can replace a lot of comments with good variable names, and code that is easy on the eyes.

Here are some videos that could help you make your code pretty.  
- [**Variable Naming**](https://www.youtube.com/watch?v=-J3wNP6u5YU)  
- [**Nesting**](https://www.youtube.com/watch?v=CFRhGnuXG-4)


## Notes
<a name="note-1"></a>
1. For testing you will use your personal Token but in production we will have Team and the Bots will use those Bot Tokens. It is most likely that being in the Team will be reserved to high level staff for safety reasons. This is the importance of the **.ENV** file along with safety concerns.
<a name="note-2"></a>
2. If you are struggling to figure out what permissions to add then just leave it blank. Unless otherwise needed we will really only be using the slash commands. Let me know if this causes problems though. But if we were setting roles, and doing more things involved with interacting with the server itself then you would need to add the required permissions.