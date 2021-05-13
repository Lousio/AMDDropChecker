#!/bin/sh
import discord
from discord.ext import commands
from multiprocessing.connection import Listener

TOKEN = 'YOURBOTTOKEN'  # Discord bot token, should be put
# into an .env file but I don't care enough
bot = commands.Bot(command_prefix='!')  # command prefix if you need it

droproleid = '<@&YOURROLEID>' # Drop role ID for pinging it when it happens


# Setup connection with main.py
async def setupConnection():
    address = ('localhost', 6000)  # address for the socket
    listener = Listener(address, authkey='CHANGEKEY'.encode('utf-8'))  # listener initialisation
    conn = listener.accept()    # Accept connection
    print('connection accepted from', listener.last_accepted) # Print connection success
    while True:
        msg = conn.recv()   # Read message sent by other script
        if "Product-ID changed" in msg:     # If Product-ID is bad, DM owner to change it
            await dm(msg)
        else:                               # Otherwise post message normally in specified channel
            await signal(msg)
        # do something with msg
        if msg == 'close':                  # if close is in the message, close connection but we never send close
            listener.close()
            break


# This method sends a message in specified channel
async def signal(msg):
    global bot  # getting our bot variable from the global context
    channel = bot.get_channel(YOURCHANNELID)       # get channel as a variable
    msg = msg + '%s' % droproleid   # Make it ping the role
    await channel.send(msg)     # Send message in specified channel


# This method direct messages a specified user
async def dm(msg):
    global bot
    await bot.wait_until_ready()    # Make sure bot is ready
    user = await bot.fetch_user(YOURUSERID)     # Get user variable
    await user.send(msg)    # Send user the message


# Once bot is ready, print success message and start the connection
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    # await deleteDM()
    await setupConnection()


# Finally, we run the bot
bot.run(TOKEN)
