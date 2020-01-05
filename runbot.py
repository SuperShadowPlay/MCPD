"""MCPD Uptime v1.0 from github.com/SuperShadowPlay/MCPD ."""
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
cNoPlayers'''


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
        serverDown = False
        mcServer = MinecraftServer(cIP, cPort)
        try:
            serverStatus = mcServer.status()
        except KeyboardInterrupt:
            raise
        except:
            serverDown = True

        if serverDown is False:
            if serverStatus.players.online == 1:
                sApply = ''
            else:
                sApply = 's'
            await client.change_presence(status=discord.Status.online,
                                         activity=discord.Game('Server Up; {0} Player{1}'.format(serverStatus.players.online, sApply)))
        else:
            await client.change_presence(status=discord.Status.online,
                                         activity=discord.Game('Server Down'))

        #Change the player count on the basis of how many seconds were inputted into cRefresh
        await asyncio.sleep(int(cRefresh))


async def warnUptime():
    """Whole point of branch Uptime."""
    connectStatus = True
    await client.wait_until_ready()
    while not client.is_closed():
        mcServer = MinecraftServer(cIP, cPort)
        lastStatus = connectStatus

        #Ping server
        try:
            pingTime = mcServer.ping()
            connectStatus = True

        #Workaround for bad coding
        except KeyboardInterrupt:
            raise

        #Failing to ping the server can raise a lot of
        #different errors depending on the circumstance.
        #So to catch them all I covered my behind above and
        #made a plain "except:" block
        except:
            connectStatus = False

        if connectStatus != lastStatus and connectStatus is False:
            print('Server is down! :: {0}'.format(getTime()))
            for i in cUsers:
                await client.get_user(i).send('{0} is down Detected at {1}!'.format(cIP, getTime()))

        await asyncio.sleep(int(cRefresh))


@client.event
async def on_message(message):
    """On message portion.

    I'm too lazy to update this to the non-async method, so this
    is where users can interact with the bot."""

    #Don't respond to self
    if message.author == client.user:
        return

    #Make a list to sort through for arg parsing
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
{0} Ping - Ping the bot
{0} Source - Github Source Code'''.format(cPrompt))

        #<prompt> ping - Pings the bot
        if msgSplit[1].lower() == 'ping':
            await message.channel.send('Pong!')
            print('Pong\'ed user ' + str(message.id)
                  + ' :: ' + str(getTime()))

        #<prompt> source - Github link
        if msgSplit[1].lower() == 'source':
            await message.channel.send('''MCPD Uptime v1.0, licensed under the MIT license.
Full source code at:
https://github.com/SuperShadowPlay/MCPD''')
            print(str(message.author) + ' Requested Source :: ' + getTime())


async def printStatus():
    """Print the updating status to the console."""
    await client.wait_until_ready()
    while not client.is_closed():
        serverDown = False
        mcServer = MinecraftServer(cIP, cPort)
        try:
            serverStatus = mcServer.status()
        except KeyboardInterrupt:
            raise
        except:
            serverDown = True

        if serverDown is False:
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
client.loop.create_task(warnUptime())
client.run(TOKEN)
