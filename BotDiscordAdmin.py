"""
Dans un premier temps pour accéder aux imports ci-dessous il faut télécharger les bibliothèques...
De ce fait pour ceux qui sont sur Windows --> Téléchargement automatique avec la commande : py -3 -m pip install -U discord.py (depuis un invite de commande CMD)
Pour ceux qui sonr sur Linux/MacOs --> Téléchargement automatique avec la commande : python3 -m pip install -U discord.py (depuis un terminal)
Enfin si votre IDE était déjà ouvert pendant le téléchargement des packages relancer le !
"""
import discord
from discord.ext import commands #import des bibliothèques Commande/Bot

bot = commands.Bot(command_prefix="!",description="Bot d'administration") #définition du préfix de la commande par exemple dans le cas actuel pour éxécuter une commande il faudra commencer avec "!"

@bot.event #Event qui permet de retourner une fonction def dans l'invite de commande ou le terminal mais pas sur le Discord
async def on_ready():
    print("En fonction!") #retourne la chaine "En fonction" pour dire que le bot discord est actif PS: Facultatif
@bot.command()
async def commande(ctx): #ctx : contexte/ on créer une définition "commande" bien entendu avec le prefix "!"
    serverName = "Leonidas" #Nom du Bot 
    await ctx.send(f"{serverName}:\n!clear (nombre)\n!commande") #listage des commandes

@bot.command()
async  def clear(ctx, nombre : int): #définition d'une commande clear avec l'atribut --> nombre
    messages = await ctx.channel.history(limit=nombre + 1).flatten()
    for message in messages:
        await message.delete() #delete du/des messages
@bot.command()
async def kick(ctx, user : discord.User, *reason):#définition d'un commande de kick avec l'atribut --> raison
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} a été kick pour : {reason} ")
@bot.command()
async def ban(ctx, user : discord.User, *reason):#définition d'une commande de ban avec l'atribut --> raison (même def que pour le kick juste un changement au niveau des méthodes(ban/kick)
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} a été ban pour la raison suivante: {reason} ")

@bot.command()
async def uban(ctx, user, *reason):#définition d'un commande unban avec l'atribut --> raison
    reason = " ".join(reason)
    UserName, UserId = user.split("#") #fonction pour séparer le UserId de son TAG qui permet d'avoir un str et un int
    BannedUser = await ctx.guild.bans()
    for i in BannedUser:
        if i.user.name == UserName and i.user.author == UserId:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} a été unban, bon retour parmi nous :wink: ")
    else:
        await ctx.send(f"{user} n'a pas été trouvé dans la liste des bans !")
@bot.command()#définition d'une commande qui permet de parcourir la liste des bannis 
async def bans(ctx):
    ids = [] #création d'une liste des bans
    bans = await ctx.guild.bans()
    for i in bans:
        ids.append(str(i.user.id))
    await ctx.send("La liste des bans est la suivante:")
    await ctx.send("\n".join(ids))


bot.run("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") #Token discord renségné sur le site : https://discord.com/developers/applications
#/!\ ne jamais donner son token discord 
