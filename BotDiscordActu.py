import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="Bot d'actu hack")
fichier = open("DataTable.csv","r") #Data table
descripteur = fichier.readline()
ligne = fichier.readline()
openclassroom,github,cybrary,eccouncil,offensivesecurity,sans,hackerhouse,infosecinstitute = ligne.split(",") #CSV : Coma separated virgule
@bot.event
async def on_ready(): #fonction d'activation --> validation de la mise en marche
    print("En fonction!")

@bot.command()
async def actu(ctx):
    await ctx.send("https://www.lemondeinformatique.fr/intrusion-hacking-et-pare-feu-36.html%22")

@bot.command()
async def serverInfo(ctx): #fonction déscriptive du serveur 
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPeople = server.member_count
    serverName = server.name
    message = f"Le serveur {serverName} contient {numberOfPeople} personnes. \n La description du serveur {serverDescription}. \n Ce serveur possède {numberOfTextChannels} salons écrit ainsi que {numberOfVoiceChannels} salons vocaux."
    await ctx.send(message)

@bot.command()
async def commande(ctx): #lisstage des commandes 
    await ctx.send("!actu\n!serverInfo\n!chinese\n!say")

@bot.command() #fonction de répétition --> inutile
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))

@bot.command()
async def site(ctx): #fonction qui permet de questionner un user pour le rediriger vers le site demander bien sur le lien est placé dans la table de donnée
    await ctx.send("Sur quel site voulez vous naviguer?\nOpenClassroom\nGitHub\nCybrary\nEccouncil\nOffensiveSecurity\nSANS\nHackerHouse\nInfosecInstitute")

    def checkMessage(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    message = await bot.wait_for("message", timeout = 10, check = checkMessage)

    if message.content == "openclassroom":
        await ctx.send(f"site : OpenClassroom\n"+ openclassroom)
    elif message.content.lower() == "github":
        await ctx.send(f"site : GitHub\n" + github)
    elif message.content.lower() == "cybrary":
        await ctx.send("site : Cybrary\n" + cybrary)
    elif message.content.lower() == "eccouncil":
        await ctx.send("site : Eccouncil" + eccouncil)
    elif message.content.lower() == "offensivesecurity":
        await ctx.send("site : OffensiveSecurity\n" + offensivesecurity)
    elif message.content.lower() == "sans":
        await ctx.send("site : SANS\n" + sans)
    elif message.content.lower() == "hackerhouse":
        await ctx.send("site : HackerHouse\n" + hackerhouse)
    elif message.content.lower() == "infosecinstitute":
        await ctx.send("site : InfosecInstutute\n" + infosecinstitute)

bot.run("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") #Token discord 
