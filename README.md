# MCPD - Minecraft Player Count for Discord
**Version 1.1**

A discord bot you host yourself, that will display the amount of people in a specified Minecraft Server at version 1.7+

**WRITTEN IN PYTHON VERSION 3.6**

Depends on

> discord.py

> mcstatus

<sup>install them with pip on the command line</sup>

## First run
Run the `configbot.py` file in a python 3 interpreter. This will
create a file called psConfig.txt in the same directory/folder as `configbot.py` 
that will store your configuration for this program.

The `runbot.py` and `psConfig.txt` **must** be in the same directory/folder to run.

## General Use
Run your bot with the `runbot.py` file from a python 3 interpreter

To ping your bot send "@\<bot> ping" in a channel that your bot can access

## Changelog
#### User facing:
Added ability to display player names

Changed way you can prompt the bot to attention

	`@<bot> ping` is now `<prompt> ping`

	`<prompt>` is decided in `MCPDConfig.py`

Added command to display online player count and names

	`<prompt> list`


#### Config:

Added new config method

Added ability to choose what the bot says when asked for online players

Added a whole slew of new configs that go along with player name display

When there is one player, it's player not players

## Contact Info

Email me at SuperShadowPlay@null.net
or contact me on discord at SuperShadowPlay#8793
