# MCPD - Minecraft Player Count for Discord
**Version 2.0**

A discord bot you host yourself, that will display the amount of people in a specified Minecraft Server at version 1.7+

**WRITTEN IN PYTHON VERSION 3.7**

Depends on

> discord.py

> mcstatus

<sup>Install them with pip on the command line.</sup>

## THIS IS OLD CODE

If you have trouble I'd be willing to help you out, but set
your expectations very low. I think I was 13 when I wrote this.

## Before Running

**In your `server.properties` file, set `enable-query=true`**

Make sure you have edited `MCPDConfig.py` to your liking, or else the bot will not work.

<b>In the config is the `cPrompt` variable, what you set it to, is what will call the bot for its commands.</b>

## General Use
Run your bot with the `runbot.py` file from a python 3 interpreter.

To get all of the commands listed in discord, send `<prompt> help` in a channel that your bot can access

To ping your bot send `<prompt> ping`

To get the players online (and their names if enabled) send `<prompt> list`.

To get the link to this Github repo, send `<prompt> source`

## Changelog
#### User facing:
Added ability to display player names

Changed way you can prompt the bot to attention

	`@<bot> ping` is now `<prompt> ping`

	`<prompt>` is decided in `MCPDConfig.py`

Added command to display online player count and names

	`<prompt> list`

Added help command

	`<prompt> help`


#### Config:

Added new config method

Added ability to choose what the bot says when asked for online players

Added a whole slew of new configs that go along with player name display

When there is one player, it's player not players

## Contact Info

Discord: SuperShadowPlay#8793
