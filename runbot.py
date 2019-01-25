#MCPD v1.1 By SuperShadowPlay#8793 
import discord
import asyncio
from mcstatus import MinecraftServer
import datetime
import time
from MCPDConfig import *

client = discord.Client()

'''Imports:
TOKEN
cIP
cPort
cRefresh
cBasePrompt
cEnableNames
cSkipNoPlayers
cNoPlayers'''

print('#MCPD v1.1 By SuperShadowPlay#8793')

#Checks for TOKEN
if TOKEN == 'null':
    print('Edit MCPDConfig.py and add your bot\'s run token')
    print('and other settings!')
    input()
    quit()

#Get time in H:M:S format
def getTime():
    _bigTime = time.strftime('%H:%M:%S')
    return _bigTime

#Bot status for player count
async def playerSidebar():
    await client.wait_until_ready()
    while not client.is_closed:
        mcServer = MinecraftServer(cIP, cPort)
        serverStatus = mcServer.status()
        if cEnableNames == True:
            mcQuery = mcServer.query()
        sidebarCount = '{0} Players Online'.format(serverStatus.players.online)
        await client.change_presence(game=discord.Game(name=sidebarCount))
        await asyncio.sleep(int(cRefresh))
        #Change the player count on the basis of how many seconds were inputted into cRefresh

@client.event
async def on_message(message):
    msgSplit = message.content.split()
    try:
        msgSplit[0]
    except IndexError:
        return

    if len(msgSplit) == 1 or 0:
        return
    
    if message.author == client.user:
        return

    #Makes cBasePrompt = 0 usable
    if cBasePrompt == 0:
        cPrompt = '<@' + str(client.user.id) + '>'
    else:
        cPrompt = cBasePrompt
        
    #Detects if the bot was called
    if msgSplit[0] == cPrompt:
        
        #<prompt> ping - Pings the bot
        if msgSplit[1].lower() == 'ping':
            await client.send_message(message.channel, 'Pong!')
            print('Pong\'ed user ' + str(message.author) + ' at ' + str(getTime()))

        #<prompt> list - Lists players online. Only the amount is listed if cEnableNames is False
        if msgSplit[1].lower() == 'list':
            mcServer = MinecraftServer(cIP, cPort)
            serverStatus = mcServer.status()

            if serverStatus.players.online == 0:
                if cSkipNoPlayers == False:
                    await client.send_message(message.channel, cNoPlayers.format(cIP))
                
            elif cEnableNames == True and '{1}' in cMessageSend and serverStatus.players.online != 0:
                mcQuery = mcServer.query()
                await client.send_message(message.channel, cMessageSend.format(serverStatus.players.online, ", ".join(mcQuery.players.names), cIP))

            else:
                await client.send_message(message.channel, cMessageSend.format(serverStatus.players.online))

async def printStatus():
    #Prints the updating status to the console
    await client.wait_until_ready()
    while not client.is_closed:
        mcServer = MinecraftServer(cIP, cPort)
        serverStatus = mcServer.status()
                    
        if cEnableNames == True and '{1}' in cMessageSend and serverStatus.players.online != 0:
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
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    #Enables correct display when cPrompt is 0
    if cBasePrompt == 0:
        cPromptText = '@' + client.user.name
    else:
        cPromptText = str(cBasePrompt)
    print('Prompt: ' + cPromptText)
    print('------')
    
client.loop.create_task(playerSidebar())
client.loop.create_task(printStatus())
client.run(TOKEN)
