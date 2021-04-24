import discord, requests
client = discord.Client()


@client.event
async def on_ready():
    print('\nWe have logged in as {0.user}'.format(client))


class SongLinkAPI:
    data=None

    @classmethod
    def data_collection(cls,msg,encode,start_str,len_start,id_size):
        if start_str in msg:
            id_start=msg.find(start_str)+len_start
            cls.data=requests.get('https://api.song.link/v1-alpha.1/links?url='+encode+msg[id_start:id_start+id_size]).json()
            return True

    @classmethod
    def data_output(cls,ch,platform):
        return ch.send(cls.data["linksByPlatform"][platform]['url']+'\n`Bot made possible by SongLink`')


@client.event
async def on_message(message):
    
    if (SongLinkAPI().data_collection(message.content,'spotify%3Atrack%3A','https://open.spotify.com/track/',31,22)
        or SongLinkAPI().data_collection(message.content,'https%3A%2F%2Fmusic.youtube.com%2Fwatch%3Fv%3D','youtu.be/',9,11)):
        
        await SongLinkAPI().data_output(message.channel,'youtubeMusic')
        await SongLinkAPI().data_output(message.channel,'amazonMusic')


client.run('Enter your Discord bot token here')
