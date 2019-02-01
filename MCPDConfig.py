#Config file for MCPD v1.1
"KEEP THE QUOTES"
"True and False and case sensitive!"
#################################

#Bot's run token
TOKEN = "null"

#Minecraft Server IP and Port (the IP *will* display to users, so capitalize at will
cIP = "Insert IP here"
cPort = 00000

#Player count's refresh in seconds (Default = 60)
cRefresh = 60

#What message to use for the beginnings of commands, setting this to 0 makes it an @mention to the bot (Default 0)
#Make sure to add "quotes" around a new prompt
cBasePrompt = 0

#"enable-query" in your "server.properties" MUST BE SET TO "true" TO DISPLAY PLAYER NAMES
#Once that is done, set this to True to enable player names in <prompt> list (Default False)
cEnableNames = False

#What message to send with <prompt> list
#{0} is replaced by the number of players online
#{1} is replaced by the names of the online players - ONLY USE IF cEnableNames IS TRUE
#{2} is replaced by the IP of the server
cMessageSend = "{0} Player(s) Online"

#If <prompt> list is called and there are no players
#Set to true if you want to send above message anyway. Set false if you want a custom no players online message (Default False)
cSkipNoPlayers = False
#If above is set to False, set the message that will display instead
#{0} is replace by the IP of the server
cNoPlayers = "There are no players on {0}"
