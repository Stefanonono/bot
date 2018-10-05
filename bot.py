# Discord Bot

import os
import sys
import time
import random
import asyncio
import datetime

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from variables import tokenVar # pylint: disable=E0611

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

print("-----------------------------")
print("Loading...")

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="40"))
	print("Running")
	print("Bot username: " + bot.user.name)
	print("Bot user ID: " + bot.user.id)
	print("-----------------------------")


# Help commands
@bot.command()
async def imglist():
	images = os.listdir("media/img")
	imagesStr = ""
	for i in range(0,len(images)):
		imagesStr = imagesStr + images[i].replace(".jpg", "") + ", "
		print(imagesStr)
	embedHelpImg = discord.Embed(title="img command images:", description=imagesStr[:-2], colour=0xFFFFFF)
	embedHelpImg.set_author(name="JHbot", icon_url="media/swan.jpg")
	await bot.say(embed=embedHelpImg)



# Misc commands
@bot.command()
async def ping():
	await bot.say("Pong!")

@bot.command()
async def echo(*, content:str):
	await bot.say(content)

@bot.command()
async def source():
	embedGithub = discord.Embed(title="Github source code", url="https://github.com/jstri/bot")
	await bot.say(embed=embedGithub)

@bot.command()
async def aquaman():
	aquaman = datetime.datetime(2018, 12, 14, hour=18)
	await bot.say("Aquaman in " + str(aquaman - datetime.datetime.now()))



# Edit command
@bot.event
async def on_message_edit(msgB, msgA):
	global embedEdit
	user = msgB.author.name
	pfp = msgB.author.avatar_url
	msgBefore = msgB.content
	msgAfter = msgA.content
	if msgBefore != msgAfter:
		embedEdit = discord.Embed(title="Message edited by " + user)
		embedEdit.set_author(name="JHbot", icon_url=pfp)
		embedEdit.colour = 0xffff00
		embedEdit.add_field(name="Before", value=msgBefore, inline=False)
		embedEdit.add_field(name="After", value=msgAfter, inline=False)

@bot.command()
async def edit():
	await bot.say(embed=embedEdit)



# Info commands
@bot.command()
async def info(user: discord.Member):
	userColour = user.colour
	username = user.name
	userDisc = user.discriminator
	nickname = user.nick
	joinDate = user.joined_at
	madeDate = user.created_at
	profilePicture = user.avatar_url

	embedInfo = discord.Embed()
	embedInfo.colour = userColour
	embedInfo.add_field(name="Username:", value=username + "#" + userDisc, inline=True)	
	embedInfo.add_field(name="Nickname:", value=nickname, inline=True)
	embedInfo.add_field(name="Join date:", value=joinDate, inline=True)
	embedInfo.add_field(name="Account create date:", value=madeDate, inline=True)
	embedInfo.set_thumbnail(url=profilePicture)

	await bot.say(embed=embedInfo)

@bot.command(pass_context=True)
async def serverinfo(ctx):
	server = ctx.message.server 
	pic = server.icon_url
	memberCount = server.member_count
	createDate = server.created_at
	name = server.name

	embedServer = discord.Embed()
	embedServer.add_field(name="Server name: ", value=name)
	embedServer.add_field(name="Members: ", value=memberCount)
	embedServer.add_field(name="Created on: ", value=createDate)
	embedServer.set_thumbnail(url=pic)
	
	await bot.say(embed=embedServer)



# Image commands
@bot.command(pass_context=True)
async def img(ctx, image: str): # pylint: disable=E0102
	try:
		channel = ctx.message.channel
		await bot.send_file(channel, "media/img/" + image + ".jpg")
	except:
		await bot.say("Image not found")

@bot.command(pass_context=True)
async def graphics(ctx):
	channel = ctx.message.channel
	await bot.send_file(channel, "media/graphics/graphics1.jpg")
	await bot.send_file(channel, "media/graphics/graphics2.jpg")
	await bot.send_file(channel, "media/graphics/graphics3.jpg")

@bot.command(pass_context=True)
async def dab(ctx):
	channel = ctx.message.channel
	file = random.choice(os.listdir("media/dab"))
	await bot.send_file(channel, "media/dab/" + file)
	
@bot.command()
async def listnya():
	message = ""
	listdir = os.listdir("media/nya")
	for i in listdir:
		message += i
		message += ", "
	await bot.say(message)

@bot.command(pass_context=True)
async def nya(ctx):
	channel = ctx.message.channel
	file = random.choice(os.listdir("media/nya"))
	await bot.send_file(channel, "media/nya/" + file)



# Voice commands
@bot.command(pass_context=True)
async def tron(ctx):
	channel = ctx.message.author.voice.voice_channel
	voice = await bot.join_voice_channel(channel)
	player = voice.create_ffmpeg_player("media/audio/tron.mp3")
	player.start()
	await asyncio.sleep(53)
	server = ctx.message.server
	voice_client = bot.voice_client_in(server)
	await voice_client.disconnect()

@bot.command(pass_context=True)
async def nemo(ctx):
	channel = ctx.message.author.voice.voice_channel
	voice = await bot.join_voice_channel(channel)
	player = voice.create_ffmpeg_player("media/audio/nemo.mp3")
	player.start()
	await asyncio.sleep(6)
	server = ctx.message.server
	voice_client = bot.voice_client_in(server)
	await voice_client.disconnect()

@bot.command(pass_context=True)
async def cat(ctx):
	channel = ctx.message.author.voice.voice_channel
	voice = await bot.join_voice_channel(channel)
	player = voice.create_ffmpeg_player("media/audio/cat.mp3")
	player.start()
	await asyncio.sleep(3)
	server = ctx.message.server
	voice_client = bot.voice_client_in(server)
	await voice_client.disconnect()

@bot.command(pass_context=True)
async def girl(ctx):
	channel = ctx.message.author.voice.voice_channel
	voice = await bot.join_voice_channel(channel)
	player = voice.create_ffmpeg_player("media/audio/girl.mp3")
	player.start()
	await asyncio.sleep(14)
	server = ctx.message.server
	voice_client = bot.voice_client_in(server)
	await voice_client.disconnect()

@bot.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = bot.voice_client_in(server)
	await voice_client.disconnect()



# Events
@bot.event
async def on_message(msg):
	if "NYA" in msg.content.upper():
		await bot.add_reaction(msg, "😹")
	await bot.process_commands(msg)

@bot.event
async def on_member_join(member):
	embedJoin = discord.Embed(colour=0xFFFFFF)
	embedJoin.add_field(name="User Joined:", value=str(member))
	embedJoin.set_thumbnail(url=member.avatar_url)
	channel = member.server.default_channel
	await bot.send_message(channel, embed=embedJoin)

@bot.event
async def on_member_remove(member):
	embedLeave = discord.Embed(colour=0xFFFFFF)
	embedLeave.add_field(name="User Left:", value=str(member))
	embedLeave.set_thumbnail(url=member.avatar_url)
	channel = member.server.default_channel
	await bot.send_message(channel, embed=embedLeave)

@bot.event
async def on_reaction_add(reaction, user):
	if reaction.emoji == "📌" and reaction.count == 4:
		pinEmbed = discord.Embed(description=reaction.message.content)
		pinEmbed.set_author(name=str(reaction.message.author), icon_url=reaction.message.author.avatar_url)
		pinEmbed.set_footer(text="In #" + str(reaction.message.channel))
		try:
			pinEmbed.set_image(url=reaction.message.attachments[0]["url"])
		except IndexError:
			pass
		await bot.send_message(bot.get_channel("494911907644440577"), embed=pinEmbed) # ID = pins archive channel ID
	
bot.run(tokenVar)