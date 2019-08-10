"""MCPD v2.0 from github.com/SuperShadowPlay/MCPD ."""
import discord
import asyncio
from mcstatus import MinecraftServer
import time
from MCPDConfig import *
print("Loaded Libraries")
print("This software is licensed under the MIT License")
print("For more information see ./LICENSE\n")
client = discord.Client()

'''Imports:
TOKEN
cIP
cPort
cRefresh
cBasePrompt
cEnableNames
cSkipNoPlayers
cNoPlayers
cEnableOutput
cOutputChannel
cDynamicOutput'''


if TOKEN == 'null':
    """Checks for TOKEN"""
    print('Edit MCPDConfig.py and add your bot\'s run token')
    print('and other settings!')
    input()
    quit()


def getTime():
    """Get time in H:M:S format."""
    _bigTime = time.strftime('%H:%M:%S')
    return _bigTime


async def playerCountUpdate():
    """Bot status for player count in the sidebar and output.

    The top part of this function is for the sidebar player count,
    the bottom part is for the output channel (if requested).
    """
    await client.wait_until_ready()
    while not client.is_closed():
        #Sidebar portion
        mcServer = MinecraftServer(cIP, cPort)
        serverStatus = mcServer.status()
        sidebarCount = discord.Game('{0} Players Online'.format(serverStatus.players.online))
        await client.change_presence(status=discord.Status.online,
                                     activity=sidebarCount)

        #Output portion
        if cEnableNames is True:
            mcQuery = mcServer.query()
        try:
            lastSetOfPlayers
        except NameError:
            lastSetOfPlayers = "Notch"
        #Check if requested
        if cEnableOutput is True and cEnableNames is True:

            if cDynamicOutput is True:
                #This is dynamic output, essentially sending a new output
                #message only when player counts change.
                diffOfPlayers = (mcQuery.players.names != lastSetOfPlayers)
                if diffOfPlayers is True:
                    lastSetOfPlayers = mcQuery.players.names
                    if serverStatus.players.online != 0:
                        playerNames = ", ".join(mcQuery.players.names)
                        outputMessage = """
{0} | {1} Players Online |
{2}""".format(getTime(), serverStatus.players.online, playerNames)
                    else:
                        outputMessage = ("{0} | No players online".format(getTime()))
                    if diffOfPlayers is True:
                        await cOutputChannel.send(outputMessage)

            elif cDynamicOutput is False:
                #Just print every <cRefresh> seconds
                if serverStatus.players.online != 0:
                    playerNames = ", ".join(mcQuery.players.names)
                    outputMessage = """
{0} | {1} Players Online |
{2}""".format(getTime(), serverStatus.players.online, playerNames)
                else:
                    outputMessage = ("{0} | No players online".format(getTime()))

                await cOutputChannel.send(outputMessage)

        #Change the player count on the basis of how many seconds were inputted into cRefresh
        await asyncio.sleep(int(cRefresh))


@client.event
async def on_message(message):
    """On message portion, most of the actual programming is in this function."""
    if message.author == client.user:
        return

    msgSplit = message.content.split()
    #If the message content is **only** an image, this
    #prevents an error message from clogging the console.
    try:
        msgSplit[0]
    except IndexError:
        return

    #Makes cBasePrompt = 0 usable
    if cBasePrompt == "0":
        cPrompt = '<@' + str(client.user.id) + '>'
    else:
        cPrompt = cBasePrompt

    #Detects if the bot was called
    if msgSplit[0] == cPrompt:

        #<prompt> help - Lists commands
        if msgSplit[1].lower() == 'help':
            await message.channel.send('''The commands available are:
{0} Help - Displays this message
{0} List - List the players online at {1}
{0} Ping - Ping the bot
{0} Source - Github Source Code'''.format(cPrompt, cIP))

        #<prompt> ping - Pings the bot
        if msgSplit[1].lower() == 'ping':
            await message.channel.send('Pong!')
            print('Pong\'ed user ' + str(message.author)
                  + ' :: ' + str(getTime()))

        #<prompt> list - Lists players online. Only the amount is
        #listed if cEnableNames is False
        if msgSplit[1].lower() == 'list':
            mcServer = MinecraftServer(cIP, cPort)
            serverStatus = mcServer.status()

            if serverStatus.players.online == 0:
                if cSkipNoPlayers is False:
                    await message.channel.send(cNoPlayers.format(cIP))

            elif cEnableNames is True and '{1}' in cMessageSend:
                if serverStatus.players.online != 0:
                    onPlayers = serverStatus.players.online
                    mcQuery = mcServer.query()
                    await messagge.channel.send(cMessageSend.format(onPlayers,
                                                ", ".join(mcQuery.players.names), cIP))

            else:
                await message.channel.send(cMessageSend.format(serverStatus.players.online))

        #<prompt> source - Github link
        if msgSplit[1].lower() == 'source':
            await message.channel.send('''MCPD v2.0, licensed under the MIT license.
Full source code at:
https://github.com/SuperShadowPlay/MCPD''')
            print(str(message.author) + ' Requested Source :: ' + getTime())


async def printStatus():
    """Print the updating status to the console."""
    await client.wait_until_ready()
    while not client.is_closed():
        mcServer = MinecraftServer(cIP, cPort)
        serverStatus = mcServer.status()

        if cEnableNames is True and '{1}' in cMessageSend and serverStatus.players.online != 0:
            mcQuery = mcServer.query()
            if serverStatus.players.online == 1:
                print('{0} Player :: {2} :: {1}'.format(serverStatus.players.online, ", ".join(mcQuery.players.names), getTime()))
            else:
                print('{0} Players :: {2} :: {1}'.format(serverStatus.players.online, ", ".join(mcQuery.players.names), getTime()))

        else:
            if serverStatus.players.online == 1:
                print('{0} Player :: {1}'.format(serverStatus.players.online, getTime()))
            else:
                print('{0} Players :: {1}'.format(serverStatus.players.online, getTime()))

        await asyncio.sleep(int(cRefresh))


@client.event
async def on_ready():
    """Log in and other such wonders."""
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    #Enables correct display when cPrompt is 0
    if cBasePrompt == "0":
        cPromptText = '@' + client.user.name
    else:
        cPromptText = str(cBasePrompt)
    print('Prompt: ' + cPromptText)
    print('------')

client.loop.create_task(playerCountUpdate())
client.loop.create_task(printStatus())
client.run(TOKEN)
