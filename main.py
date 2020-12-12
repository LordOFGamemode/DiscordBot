import discord
def txt_to_list(file:str):
    fileinfo = open(file + '.txt')
    info = fileinfo.read()
    rt = info.split()
    fileinfo.close()
    return rt
regeln_channel_id = 786781198608236564
class MyClient(discord.Client):
    async def on_ready(self):
        print("I am ready")
        regeln_channer = client.get_channel(regeln_channel_id)
        await  regeln_channer.send("Regeln:\n\n► Pornografischen, Rassistischen, sexistische und nicht jugendfreie \nInhalte/Nicknames sind Verboten. \n\n► Kein unnötiger Spam, illegale Posts und Trolls.\n\n► Jegliche Werbung für eigene Zwecke ist verboten.\n\n► Solltest du gegen die Regeln verstoßen, werden Teammitglieder eine \nangemessene Strafe aussprechen. Hierbei benötigen sie keine Beweise, um \ndies durchzuführen.\n\n► Den Anweisungen der Teammitglieder ist Folge zu leisten.\n\n► Wir haben jeder Zeit die Berechtigung die Regeln zu ändern.\n\n► Hier gelten die allgemeinen Discord Richtlinien - \nhttps://discord.com/new/guidelines\n\nWenn du diese Regeln acceptierst reagiere mit 👍")


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
        print(str(message.channel.id))
        if(str(message.channel) == 'admin'):
            if(message.content == '!log'):
                file = discord.File('LOG.txt')
                await message.channel.send(file=file, content='Hier ist der log')
        for word in blacklist:
            if (word in message.content):
                await message.delete()
                print(str(message.author) + ' war böse')
                await message.channel.send('@' + str(message.author) + ' sei nicht so böse!!!')

    async def on_reaction_add(self, reaction, user):
        roles = discord.utils.get(user.guild.roles, name='Member')
        if str(reaction.emoji) == "👍":
            await user.add_roles(roles)





client = MyClient()
client.run('Nzg2NzU4MDEyODM1OTg3NDk3.X9LDfw.ZJZk_PXrDmIUm-_j4Gj8A8rBDxQ')