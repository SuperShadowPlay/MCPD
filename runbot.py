#By SuperShadowPlay#8793
import discord
import asyncio
from mcstatus import MinecraftServer
import datetime
import time


client = discord.Client()

try:
    my_file = open('psConfig.txt')
except IOError:
    print('Run configbot.py first!')
    input()
    quit()
    
#Read config data and turn it to a list
def readConfig():
    _readConfig = open("psConfig.txt", "r")
    _returnedConfig = _readConfig.read().split(';')
    _readConfig.close()
    return _returnedConfig
config = readConfig()
#End read config data

#Bot status for player count
async def playerSidebar():
    await client.wait_until_ready()
    while not client.is_closed:
        mcServer = MinecraftServer(config[2], int(config[3]))
        serverStatus = mcServer.status()
        sidebarCount = '{0} Players Online'.format(serverStatus.players.online)
        print('Sidebar Updated To: ' + sidebarCount + ': ' + str(datetime.datetime.now()))
        await client.change_presence(game=discord.Game(name=sidebarCount))
        await asyncio.sleep(int(config[4]))
        #Change the player count on the basis of how many seconds were inputted into config[4]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '<@' + str(client.user.id) + '>':
        await client.send_message(message.channel, 'Pong!')
        print('Pong\'ed user ' + str(message.author.id) + ' at ' + str(datetime.datetime.now()))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
client.loop.create_task(playerSidebar())
TOKEN = config[1]
client.run(TOKEN)
