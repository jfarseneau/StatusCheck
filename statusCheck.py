'''
@author: Jean-Francois Arseneau
'''

import socket, sys, ConfigParser, io, os

from datetime import datetime

if __name__ == '__main__':
    pass

scriptPath = sys.path[0] + '/' # Fix relative paths for script to be executed anywhere

config = ConfigParser.RawConfigParser()
config.read(scriptPath+'config')


# ---------- SERVER INFO ---------

terrariaHost = config.get('serverInfo', 'terrariaHost')
terrariaPort = config.get('serverInfo', 'terrariaPort')

mumbleHost = config.get('serverInfo', 'mumbleHost')
mumblePort = config.get('serverInfo', 'mumblePort')

minecraftHost = config.get('serverInfo', 'minecraftHost')
minecraftPort = config.get('serverInfo', 'minecraftPort')

BUFFER_SIZE = 1024


s = None

for res in socket.getaddrinfo(terrariaHost, terrariaPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res

    
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error, msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error, msg:
        s.close()
        s = None
        continue
    break

if s is None:
    terrariaConnect = False
    
else:
    terrariaConnect = True
    s.close()
    
# TO MAKE THIS INTO A FUNCTION
    
s = None

for res in socket.getaddrinfo(mumbleHost, mumblePort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res

    
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error, msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error, msg:
        s.close()
        s = None
        continue
    break

if s is None:
    mumbleConnect = False
    
else:
    mumbleConnect = True
    s.close()

headerFile = open(scriptPath + 'header.html', 'r')
footerFile = open(scriptPath + 'footer.html', 'r')

# TERRARIA HTML CODE
content = '<div class="serverType" id="terraria">Terraria</div>\n<div class="serverName">' + terrariaHost + '</div>\n'
if terrariaConnect:
    content = content + '<div class="serverStatus" id="online">ONLINE</div>\n'
else:
    content = content + '<div class="serverStatus" id="offline">OFFLINE</div>\n'

content = content + '<div class="timestamp">Last checked ' + str(datetime.now()) + '</div>'

# MUMBLE HTML CODE
content = content + '</div>\n<div class="serverList">\n<div class="serverType" id="mumble">Mumble</div>\n<div class="serverName">' + mumbleHost + '</div>\n'
if mumbleConnect:
    content = content + '<div class="serverStatus" id="online">ONLINE</div>\n'
else:
    content = content + '<div class="serverStatus" id="offline">OFFLINE</div>\n' 
content = content + '<div class="timestamp">Last checked ' + str(datetime.now()) + '</div>'     

# MINECRAFT CODE    

#content = content + '</div>\n<div class="serverList">\n<div class="serverType" id="minecraft">Minecraft</div>\n<div class="serverName">' + minecraftHost + '</div>\n'
#if minecraftConnect:

htmlToOutput = headerFile.read() + content + footerFile.read()

htmlFile = open(scriptPath + 'index.html','w')
htmlFile.write(htmlToOutput)

sys.exit()






