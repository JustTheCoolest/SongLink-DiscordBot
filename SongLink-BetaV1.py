# In this beta version, only converting Spotify links to YouTube Music links is supported

import discord, requests
client = discord.Client()

@client.event
async def on_ready():
    print('\nWe have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.content.startswith('https://open.spotify.com/track/'):
        data=requests.get('https://api.song.link/v1-alpha.1/links?url=spotify%3Atrack%3A'+message.content[31:53]).json()
        await message.channel.send(data["linksByPlatform"]['youtubeMusic']['url']+'\n`Bot made possible by SongLink`')

client.run('Insert your Discord Bot token here')
