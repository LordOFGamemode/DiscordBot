import discord
def txt_to_list(file:str):
    fileinfo = open(file + '.txt')
    info = fileinfo.read()
    rt = info.split()
    fileinfo.close()
    return rt

class MyClient(discord.Client):
    async def on_ready(self):
        print("I am ready")


    async def on_message(self, message):
        if( message.author == client.user):
            return
        messagelog = '[LOG(' + str(message.channel) + ')](' + str(message.author)  + ') schreibt: ' + message.content
        f = open('LOG.txt', 'a')
        f.write(messagelog + '\n')
        f.close()
        print(messagelog)
        #message überprüfung
        blacklist = txt_to_list('BlackList')

        for word in blacklist:
            if (word in message.content):
                print(str(message.author) + ' war böse')
                await message.channel.send('@' + str(message.author) + ' sei nicht so böse!!!')







client = MyClient()
client.run('Nzg2NzU4MDEyODM1OTg3NDk3.X9LDfw.ZJZk_PXrDmIUm-_j4Gj8A8rBDxQ')