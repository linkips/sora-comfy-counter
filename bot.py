import os
import discord
import pickle
client = discord.Client()

#function to store the counters to the file
def storecounts(sora,achan):
    f = open('countstore.bin','wb+')
    pickle.dump(soracount, f)
    pickle.dump(achancount, f)
    f.close()
    return

#global counters for the emotes
soracount = 0 
achancount = 0

#retrieves bot token from file
ftoken = open("token.txt",'r')
TOKEN = ftoken.readline()
ftoken.close()

#checks if counter file exists, if not, creates it
if not os.path.isfile('countstore.bin'):
    storecounts(0,0)
else: #reads file that stores the counter
    f = open('countstore.bin','rb')
    soracount = pickle.load(f)
    achancount = pickle.load(f)
    f.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    global soracount
    global achancount

    #local variables that will count the emotes within the message
    localsoracount = message.content.count(':soraComfy:')
    localachancount = message.content.count(':AchanComfy:')
    
    #hello
    if message.content.startswith('$hello'):
        if message.author.id == 210540406033612800:
            await message.channel.send('Hello creator!')
        else:
            await message.channel.send('Hello!')

    #displays how many times the comfy emotes have been used
    if message.content == '$comfycount':
        await message.channel.send(':soraComfy: has been used %d times.' % soracount)
        await message.channel.send(':AchanComfy: has been used %d times.' % achancount)
    
    #resets the counters, only the creator can do this
    if message.content == '$clearcounters':
        if message.author.id == 210540406033612800:
            soracount =0
            achancount =0
            storecounts(soracount,achancount)
            await message.channel.send('Counters reset.')
            return
        else:
            await message.channel.send("You're not allowed to do this!")
            

    #check for emotes
    if localsoracount > 0:
        soracount += localsoracount

    if localachancount > 0:
        achancount += localachancount
        
    #update file
    storecounts(soracount, achancount)
      
    return

    
client.run(TOKEN) 
