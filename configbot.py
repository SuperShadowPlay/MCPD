import time

config = [False, 'Null', 'Null', 'Null', 'Null']
if True:
    print('Detected that this is the first use of this program on this computer, you will now be asked to provide:')
    print('Your bot run token')
    print('Server host ip')
    print('Server port')
    print('Preferred refresh rate')
    print('... ')
    time.sleep(1)
    print('Input your bot\'s run token: (If you can\'t paste it in, run this config creator in IDLE')
    config[1] = input()
    time.sleep(1)
    print('Input your Minecraft server\' host ip:')
    config[2] = input()
    time.sleep(1)
    print('Input your Minecraft server\'s port:')
    config[3] = input()
    time.sleep(1)
    print('Input preferred refresh rate of player count in seconds:')
    config[4] = input()
    time.sleep(1)
    config[0] = True
    
    print('\n')
    print('Saving...')
    _createFileData = str(config[0]) + ';' + str(config[1]) + ';' + str(config[2]) + ';' + str(config[3] + ';' + str(config[4]))
    _newConfig = open("psConfig.txt", "w")
    _newConfig.write(_createFileData)
    _newConfig.close()
    print('Saved')
    
    time.sleep(1)
    config[0] = True
    print('\n')
    print('Your bot is now configured, if you would like to change the settings, run this config file and restart your bot')
    input('')
