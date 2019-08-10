"""Config file for MCPD v2.0"""
"KEEP THE QUOTES"
"True and False and case sensitive!"
#################################

#Bot's run token
TOKEN = "null"

#Minecraft Server IP and Port (the IP *will* display to users, so capitalize at will
cIP = "example.minecraft.server"
cPort = 25565

#Player count's refresh in seconds (Default = 60)
cRefresh = 60

#What message to use for the beginnings of commands, setting this to 0 makes it an @mention to the bot (Default 0)
cBasePrompt = "0"

#"enable-query" in your "server.properties" MUST BE SET TO "true" TO DISPLAY PLAYER NAMES
#Once that is done, set this to True to enable player names in mc! list (Default False)
cEnableNames = False

#What message to send with <prompt> list
#{0} is replaced by the number of players online
#{1} is replaced by the names of the online players - ONLY USE IF cEnableNames IS TRUE
#{2} is replaced by the IP of the server
cMessageSend = "{0} Player(s) Online: {1}"

#If <prompt> list is called and there are no players
#Set to true if you want to send above message anyway. Set false if you want a custom no players online message (Default False)
cSkipNoPlayers = False
#If above is set to False, set the message that will display instead
#{0} is replace by the IP of the server
cNoPlayers = "There are no players on {0}"

#Chat output
#Set to True to enable output of players to a chatbox (cEnableNames must be True!!!) (Default False)
cEnableOutput = False
#Put the channel id of the output channel here
cOutputChannel = 0
#Set to True to update the player count each time the list of players change
#Set to False to update regardless of changes (Default True)
cDynamicOutput = True
