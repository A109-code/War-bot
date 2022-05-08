import discord
import time
import datetime
import random
import os
import requests
import json
from replit import db
import random as r
from discord.ext.commands import Bot
from random import uniform
from keep_alive import keep_alive
from discord.ext import commands
from timer import timer
from discord_components import DiscordComponents, Button, ButtonStyle
import asyncio

intents = discord.Intents.default()
intents.members = True
bot = Bot(command_prefix='!', intents=intents)
client=discord.Client(intents=intents)
my_secret = os.environ['!F!J']
display_shop = {"🪖 soldier 🪖": 100, "⛵ sailor ⛵":100,"<:pistol:891380898275135498>gun<:pistol:891380898275135498>":50, "<:machinegun:891401257514860555>machine gun<:machinegun:891401257514860555>":75,"<:assaultrifle:891408408371167242>assault rifle<:assaultrifle:891408408371167242>":85,"<:sniperrifle:891407196200509440>sniper rifle<:sniperrifle:891407196200509440>":100,"🛥 boat 🛥":200,"🛳️ ship 🛳️":1000}
shop = {"soldier": 100, "sailor":100,"gun":50, "machine gun":75,"assault rifle":85,"sniper rifle":100,"boat":200,"ship":1000}

RedInven=[]
if "RedInven" in db.keys():
	RedInven = db["RedInven"]
else:
		db["RedInven"]=RedInven
BlueInven=[]
if "BlueInven" in db.keys():
		BlueInven = db["BlueInven"]
else:
	db["BlueInven"]=BlueInven
	BlueBuilds={}
if "playerstats" in db.keys():
	playerstats = db["playerstats"]
else:
	playerstats = {}
	db["playerstats"] = playerstats
async def STUFF(message):
	response = requests.get("https://www.boredbutton.com/random")
	json_data=json.loads(response)

	await client.delete_message(message)
	return(json_data)
	messssss='%alarm {1.mention}30 Red Trench Complete!'.format(message,text_channel)

async def dm(userID):
	await client.wait_until_ready()
	user = await client.fetch_user(userID)
	await user.send('Filler Text')

class UpdateRCur():
	if "RedMoney" in db.keys():
		global RedCurrency
		RedCurrency = db["RedMoney"]
	else:
		db["RedMoney"]=1000
		RedCurrency=db["RedMoney"]
	def redMin(amountRed):
		global RedCurrency
		RedCurrency-=amountRed
		db["RedMoney"] = RedCurrency
	def redAdd(amountRPlus):
		global RedCurrency
		RedCurrency+=amountRPlus
		db["RedMoney"]=RedCurrency
class UpdateBCur():
	if "BlueMoney" in db.keys():
		global BlueCurrency
		BlueCurrency = db["BlueMoney"]
	else:
		db["BlueMoney"]=1000
		BlueCurrency=db["BlueMoney"]
	def blueMin(amountB):
		global BlueCurrency
		BlueCurrency-=amountB
		db["BlueMoney"] = BlueCurrency
	def blueAdd(amountBPlus):
		global BlueCurrency
		BlueCurrency+=amountBPlus
		db["BlueMoney"]=BlueCurrency
		
class UpdateBInven:
	def blueIMin(item):
		BlueInven.remove(item)
		db["BlueInven"] = BlueInven
	def blueIAdd(item):
		BlueInven.append(item)
		db["BlueInven"]=BlueInven
	async def blueIo(*args):
		oldkey=''
		items={}
		for key in BlueInven:
			keytester=key
			multipleN=0
			if keytester==oldkey:
				pass
			else:
				for key in BlueInven:
					if keytester==key:
						multipleN+=1
				items[keytester]=multipleN
				oldkey=keytester
		return(items)
class UpdateRInven:
	def redIMin(item):
		RedInven.remove(item)
		db["RedInven"] = RedInven
	def redIAdd(item):
		RedInven.append(item)
		db["RedInven"]=RedInven
	async def redIo(*args):
		oldkey=''
		items={}
		for key in RedInven:
			keytester=key
			multipleN=0
			if keytester==oldkey:
				pass
			else:
				for key in RedInven:
					if keytester==key:
						multipleN+=1
				items[keytester]=multipleN
				oldkey=keytester
		return(items)
@bot.command()
async def rolemembers(ctx,role_id):
	role = ctx.guild.get_role(role_id)
	return len(role.members)

@commands.command(pass_context=True)
async def getteam(self, ctx):
	role = discord.utils.get(ctx.guild.roles,name="Blue Team")
	if role in self.roles:
		say = 'Blue'
		return say
	else:
		role = discord.utils.get(ctx.guild.roles,name="Red Team")
		if role in self.roles:
			say = 'Red'
			return say
		else:
			say = 'N/A'

class UpdateRbuilds:
	if "RedBuilds" in db.keys():
		global RedBuilds
		RedBuilds = db["RedBuilds"]
	else:
		db["RedBuilds"]={}
		RedBuilds=db["RedBuilds"]
	async def redMin(item,ctx):
		try:
			del RedBuilds[item]
			db["RedBuilds"] = RedBuilds
		except KeyError:
			await ctx.send("YOU DON'T HAVE THAT BUILD, BUDDY!")
		else:
			return
	def redAdd(item):
		#this just gets all of the previous builds and their number
		if item in RedBuilds:
			oldkey=''
			items={}
			for key in RedBuilds:
				keytester=key
				multipleN=0
				if keytester==oldkey:
					pass
				else:
					for key in RedInven:
						if keytester==key:
							multipleN+=1
					items[keytester]=multipleN
					oldkey=keytester
			x=items.get(item)
			x+=1
			name=str(item+" "+str(x))
			RedBuilds[name]={}
		else:
			RedBuilds[item]={}
		db["RedBuilds"]=RedBuilds
	def blueItemAdd(item,what,howmuch):
		if item in RedBuilds:
			if what in item:
				for i in range(howmuch):
					UpdateRInven.redImin(what)
				item[what]+=howmuch
			else:
				item[what]=howmuch
	def redItemMin(item,what,howmuch):
		if item in RedBuilds:
			if what in item:
				for i in range(howmuch):
					UpdateRInven.RedIAdd(what)
				item[what]-=howmuch
			else:
				pass
	async def redIo(*args):
		items={}
		things=[]
		for key in RedBuilds:
			build=key
			for key in build:
					things.append(build)
			items[build]=things
		return(items)
class UpdateBbuilds:
	if "BlueBuilds" in db.keys():
		global BlueBuilds
		BlueBuilds = db["BlueBuilds"]
	else:
		db["BlueBuilds"]={}
		BlueBuilds=db["BlueBuilds"]
	async def blueMin(item,ctx):
		try:
			del BlueBuilds[item]
			db["BlueBuilds"] = BlueBuilds
		except KeyError:
			await ctx.send("YOU DON'T HAVE THAT BUILD, BUDDY!")
		else:
			return
	def blueAdd(item):
		#this just gets all of the previous builds and their number
		if item in BlueBuilds:
			oldkey=''
			items={}
			for key in BlueBuilds:
				keytester=key
				multipleN=0
				if keytester==oldkey:
					pass
				else:
					for key in BlueInven:
						if keytester==key:
							multipleN+=1
					items[keytester]=multipleN
					oldkey=keytester
			x=items.get(item)
			x+=1
			name=str(item+" "+str(x))
			BlueBuilds[name]={}
		else:
			BlueBuilds[item]={}
		db["BlueBuilds"]=BlueBuilds
	def blueItemAdd(item,what,howmuch):
		if item in BlueBuilds:
			#if what in item:
				#for i in range(howmuch):
					#UpdateBInven.blueImin(what)
				#item[what]+=howmuch
			#else:
			pass
		print(BlueBuilds)
		#BlueBuilds.get(item)=
		UpdateBInven.blueImin(item.content)
	def blueItemMin(item,what,howmuch):
		if item in BlueBuilds:
			if what in item:
				for i in range(howmuch):
					UpdateBInven.blueIAdd(what)
				item[what]-=howmuch
			else:
				pass
	async def blueIo(*args):
		items={}
		things=[]
		for key in BlueBuilds:
			build=key
			for item in BlueBuilds[build]:
				print(item)
				print(build)
				things.append(build)
			items[build]=things
		return(items)

@commands.command(pass_context=True)
async def ModRole(self, ctx):
	role = discord.utils.get(ctx.guild.roles,name="Moderators")
	if role in self.roles:
		say = 'Mod'
		return say
	else:
		say = 'non-mod'
		return say
		
@client.event
async def shop_person(message,ident,item,author,itemcount):
	userinput = await client.wait_for("message")
	await shop_input(userinput,ident,item,author,itemcount)
	
@client.event
async def buildadd_person(message,ident,item,author,itemcount):
	userinput = await client.wait_for("message")
	await buildadd_input(userinput,ident,item,author,itemcount)
	
@client.event
async def buildadd_input(message,ident,item,author,itemcount):
	if message.author.name != ident:
		await buildadd_person(message,ident,item,author,itemcount)
	if message.content.lower() == "y":
		Complete=''
		rolewhat=await getteam(message.author,message)
		if rolewhat=='Blue':
			UpdateBbuilds.blueItemAdd(itemcount,item,1)
			Complete="Complete!"
		elif rolewhat=='Red':
			UpdateBbuilds.blueItemAdd(itemcount,item,1)
			Complete="Complete!"
		else:
			await message.channel.send("sorry, you can't use that command.")
			return
		await message.channel.send(Complete)
	elif message.content.lower() == "n":
		await message.channel.send('Action Canceled!')
	else:
		await message.channel.send("I don't understand your wording! START OVER!")
		
@client.event
async def howmuch(message,ident,author):
	num = await client.wait_for("message")
	if message.author.name != ident:
		howmuch(message,ident,author)
	else:
		return(num)
		
@client.event
async def shop_input(message2,ident,item,author,itemcount):
	if message2.author.name != ident:
		await shop_person(message2,ident,item,author,itemcount)
	if message2.content.lower() == "y":
		Complete=''
		rolewhat=await getteam(message2.author,message2)
		if rolewhat=='Blue':
			BlueMoneyTest=BlueCurrency
			BlueMoneyTest-=shop.get(item)*int(str(itemcount.content))
			if not BlueMoneyTest < 0:
				for itemcount in range(int(str(itemcount.content))):
					UpdateBCur.blueMin(shop.get(item))
					UpdateBInven.blueIAdd(item)
				Complete="Purchase Complete! Your team now has "
				Complete+=str(db["BlueMoney"])
				Complete+=" dollars."
			else:
				await message2.channel.send("You don't have enough money!")
				return
		elif rolewhat=='Red':
			RedMoneyTest=RedCurrency
			RedMoneyTest-=shop.get(item)*int(itemcount.content)
			if not RedMoneyTest < 0:
				for itemcount in range(int(itemcount.content)):
					UpdateRCur.redMin(shop.get(item))
					UpdateRInven.redIAdd(item)
				Complete="Purchase Complete! Your team now has "
				Complete+=str(db["RedMoney"])
				Complete+=" dollars."
			else:
				await message2.channel.send("You don't have enough money!")
				return
		else:
			await message2.channel.send("sorry, you can't use that command.")
			return
		await message2.channel.send(Complete)
	elif message2.content.lower() == "n":
		await message2.channel.send('Purchase Canceled!')
	else:
		await message2.channel.send("I don't understand your wording! START OVER!")

@bot.event
async def bot_status():
	activity = discord.Game(name="!war", type=3)
	await Bot.change_presence(self=client,activity=activity)

@commands.command(pass_context=True)
async def Role(self, ctx):
	role = discord.utils.get(ctx.guild.roles,name="Blue Team")
	if role in self.roles:
			say = 'Blue'
			return say
	else:
		role = discord.utils.get(ctx.guild.roles,name="Red Team")
		if role in self.roles:
			say = 'Red'
			return say
		else:
			say = 'N/A'
pastdate=datetime.datetime.today()
async def midnight():
	global pastdate
	await asyncio.sleep(1)
	currentdate=datetime.datetime.today()
	if currentdate!=pastdate:
		BlueCurrency=db["BlueMoney"]
		RedCurrency=db["RedMoney"]
		BlueCurrency+=200
		RedCurrency+=200
		pastdate=currentdate
		
@client.event
async def on_ready():
	res=DiscordComponents(client)
	print('We have logged in as {0.user}'.format(client))
	await midnight()

@client.event
async def on_message(message):
	msg = message.content
	global BlueCurrency
	global RedCurrency
	if "simulate" in db.keys():
		simulate=db["simulate"]
	else:
		simulate = False
		db["simulate"] = simulate
	BlueCurrency=db["BlueMoney"]
	RedCurrency=db["RedMoney"]
	if message.author == client.user:
		return
	if message.content.startswith('!simulateai'):
		simulate = db["simulate"]
		if message.content.endswith == message.content.startswith:
			i = 0
		else:
			i = 1
		bool1 = msg.split('!simulateai',i)[i]
		if bool1 == '':
			await message.channel.send(db["simulate"])
			return
		bool1 = message.content.split('simulateai ',1)[1]
		if bool1.lower() == 'false': 
			db["simulate"] = False
			simulate = db["simulate"]
		if bool1.lower() == 'true':
			db["simulate"] = True
			simulate = db["simulate"]
			await message.channel.send('simulateai is now')
			await message.channel.send(simulate)
			return
	if simulate:
		if message.content.startswith('!start'):
			await message.channel.send('!hi')
			db[simulate] = False
	if message.content.startswith('!threaten'):
		await message.channel.send('You have succesefuly threatened nobody!')
	if message.content.startswith('!war') or message.content.startswith('!War'):
		await message.channel.send('War has already started, dummy!')
	if message.content.startswith('!sus'):
		await message.channel.send('When the imposter is sus! 😳')
	if message.content.startswith('!hi'):
		time.sleep(0.5)
		await message.channel.send('!how are you?')
	if message.content.startswith("!I'm"):
		time.sleep(0.5)
		ran1 = round(uniform(0,1))
		if ran1 == 0:
			await message.channel.send("!I'm alright, but my boss fired me.")
		elif ran1 == 1:
			await message.channel.send("!I'm great, I recently got a new house!")
	if message.content.startswith('!Oh'):
		time.sleep(1)
		await message.channel.send('*sigh*')
		time.sleep(2)
		await message.channel.send('Bye, I guess')
		time.sleep(0.5)
		await message.channel.send(':(')
		time.sleep(1)
		await message.channel.send('Why are you so casual about this?')
	if message.content.startswith('!Thats'):
		time.sleep(0.5)
		await message.channel.send('Ok, bye!')
	if message.content.startswith('!shop') and message.channel.id==834501702420791356:
		embed = discord.Embed(title="Shop", description="Buy stuff here!")
		#lol this is so broken
		for key, value in display_shop.items():
			title=key
			cost="Costs "
			cost+=str(value)
			cost+=" dollars."
			description=cost
			embed.add_field(name=title, value=description)
		await message.channel.send(embed=embed)
		return
	if message.content.startswith('!buy') and message.channel.id==834501702420791356:
		item=message.content.split("!buy ",1)[1]
		if item in shop:
			await message.channel.send('How much would you like to buy?')
			ident = message.author.name
			itemcount=await howmuch(message,ident,message.author)
			sendm='Are you sure you wanna buy that? it costs '
			sendm+=str(shop.get(item)*int(itemcount.content))
			sendm+=' dollars. Type [y] for yes, [n] for no.'
			await message.channel.send(sendm)
			await shop_person(message,ident,item,message.author,itemcount)
		else:
			await message.channel.send('we actually dont have that')
	if message.content.startswith('!build '):
		buildwhat = msg.split('!build ',1)[1]
		if buildwhat.lower()=='trench':
			say = await Role(message.author,message)
			if say == 'Blue':
				await message.channel.send("Timer started!")
				await timer(15)
				msg = 'Blue Trench Complete!'
				UpdateBbuilds.blueAdd("Blue Trench")
			elif say == 'Red':
				await message.channel.send("Timer started!")
				await timer(15)
				msg = 'Red Trench Complete!'
			else:
				msg = "you can't use this command!"
			channel = 834493073391616054
			await channel.send(msg)
		else:
			await message.channel.send('I dunno what your talking about')
	if message.content.startswith("!easter") or message.content.startswith("!eater"):
		await message.channel.send("🥚 Eater eggs! 🥚🥚 Eater eggs! 🥚")
	if message.content.startswith('!message'):
		await message.channel.send('this is the pure message:')
		await message.channel.send(message)
		await message.channel.send('this is the translated message:')
		await message.channel.send(message.content)
	if message.content.startswith('!bluemoney'):
		money_display=db["BlueMoney"]
		await message.channel.send(money_display)
	if message.content.startswith('!redmoney'):
		money_display=db["RedMoney"]
		await message.channel.send(money_display)
	if message.content.startswith("!restoremod"):
		mod = await ModRole(message.author,message)
		print(mod)
		if mod=="Mod":
			await message.channel.send("Money Restored")
			db["BlueMoney"]=1000
			db["RedMoney"]=1000
			UpdateBCur()
			UpdateRCur()
		else:
			await message.channel.send("Sorry, only moderators can use this command.")
	if message.content.startswith("!blueinven"):
		embed1 = discord.Embed(title="Blue Inventory", description="Blue Team Bought these things:", color = discord.Colour(0x30b7ff))
		List1=await UpdateBInven.blueIo()
		for key,value in List1.items():
			title1=key
			title1+=' x'
			title1+=str(value)
			embed1.add_field(name=title1,value='------------------------------')
		await message.channel.send(embed=embed1)
	if message.content.startswith("!redinven"):
		embed2 = discord.Embed(title="Red Inventory", description="Red Team Bought these things:", color = discord.Colour(0xff3030))
		List2=await UpdateRInven.redIo()
		for key,value in List2.items():
			title2=key
			title2+=' x'
			title2+=str(value)
			embed2.add_field(name=title2,value='------------------------------')
		await message.channel.send(embed=embed2)
	await bot_status()
	if message.content.startswith("!modclear"):
		mod = await ModRole(message.author,message)
		if mod=="Mod":
			await message.channel.send("Inventory Cleared")
			BlueInven.clear()
			RedInven.clear()
		else:
			await message.channel.send("Sorry, only moderators can use this command.")
	if message.content.startswith('!organize'):
		await UpdateBInven.blueIo(message)
	if message.content.startswith('!equip'):
		try:
			equip=message.content.split(' ',2)
			equip.remove('!equip')
			equiptowhat=equip[0]
			equipwhat=equip[1]
			whatrole=await getteam(message.author,message)
			if whatrole=='Blue':
				inven=BlueInven
				if equiptowhat in inven:
					sendw1=equiptowhat
					sendw1+=" has equipped the weapon "
					sendw1+=equipwhat
					sendw1+='.'
					await message.channel.send(sendw1)
				else:
					await message.channel.send("YOU DON'T HAVE THE REQUIRED THINGS, YOU LIAR.")
					return
				if equiptowhat.lower()=='soldier':
					if equipwhat.lower()=='gun':
						UpdateBInven.blueIAdd('Weaponized Soldier')
						bought='Weaponized Soldier'
					if equipwhat.lower()=='machine gun':
						UpdateBInven.blueIAdd('Machine Gunner')
						bought='Machine Gunner'
					if equipwhat.lower()=='assault rifle':
						UpdateBInven.blueIAdd('Assault Rifleman')
						bought='Assault Rifleman'
					if equipwhat.lower() == "sniper rifle":
						UpdateBInven.blueIAdd('Sniper')
						bought='Sniper'            
				else:
					await message.channel.send('something is going on...')
					return
				UpdateBInven.blueIMin(equipwhat)
				UpdateBInven.blueIMin(equiptowhat)
			elif whatrole=='Red':
				inven=RedInven
				if equiptowhat in inven:
					sendw1=equiptowhat
					sendw1+=" has equipped the weapon "
					sendw1+=equipwhat
					sendw1+='.'
					await message.channel.send(sendw1)
				else:
					await message.channel.send("YOU DON'T HAVE THE REQUIRED THINGS, YOU LIAR.")
					return
				if equiptowhat.lower()=='soldier':
					if equipwhat.lower()=='gun':
						UpdateRInven.redIAdd('Weaponized Soldier')
						bought='Weaponized Soldier'
					elif equipwhat.lower()=='machine gun':
						UpdateRInven.redIAdd('Machine Gunner')
						bought='Machine Gunner'
					elif equipwhat.lower()=='assault rifle':
						UpdateRInven.redIAdd('Assault Rifleman')
						bought='Assault Rifleman'
					elif equipwhat.lower()=='sniper rifle':
						UpdateRInven.redIAdd('Sniper')
						bought='Sniper'
					else:
						await message.channel.send("something is going on...")
						return
				UpdateRInven.redIMin(equipwhat)
				UpdateRInven.redIMin(equiptowhat)
				if whatrole=='Blue':
					UpdateBInven.blueIMin(bought)
				elif whatrole=='Red':
					UpdateRInven.redIMin(bought)
		except:
			await message.channel.send('Errorsss') 
	if message.content.startswith("!dm"):
		user_id=message.content.split(" ",1)[1]
		user_id=user_id.translate({ord(i): None for i in '<>@!'})
		print(user_id)
		await dm(user_id)
	if message.content.startswith("!somethingthatdidn't_work"):
		for a in shop:
			things=[]
			for i in shop:
				for h in range(1):
					things.append([Button(style=ButtonStyle.blue, label=a)])
				break
			await message.channel.send("Shop",components=things) #Blue button with button label of "Test"
			thing=[]
		res = await client.wait_for("button_click") #Wait for button to be clicked
		await res.respond(type=4, content=f'Button Clicked')
	if message.content.startswith("!bluebuilds"):
		embed = discord.Embed(title="Blue Builds",description="Blue Team Built these things:", color = discord.Colour(0x30b7ff))
		List=await UpdateBbuilds.blueIo()
		for key,value in List.items():
			embed.add_field(name=key,value=value)
		await message.channel.send(embed=embed)
	if message.content.startswith("!redbuilds"):
		embed = discord.Embed(title="Red Builds",description="Red Team Built these things:", color = discord.Colour(0xff3030))
		List=await UpdateRbuilds.redIo()
		for key,value in List.items():
			embed.add_field(name=key,value=value)
		await message.channel.send(embed=embed)
	if message.content.startswith("!buildadd"):
		build=message.content.split("!buildadd ",1)[1]
		print(build)
		role=await getteam(message.author,message)
		if role=="Blue":
			buildinven=await UpdateBbuilds.blueIo()
		elif role=="Red":
			buildinven=await UpdateRbuilds.redIo()
		else:
			await message.channel.send("Your not on a team, please contact a moderator or admin to help you out!")
			return
		if build in buildinven.keys():
			await message.channel.send('What things what you like to put into your build?')
			ident = message.author.name
			item=await howmuch(message,ident,message.author)
			await message.channel.send('Are you sure you wanna do that?')
			await buildadd_person(message, ident, build, message.author, item.content)
		else:
			await message.channel.send("Bro you didn't even build that thing yet SMH")
	if message.channel.id==909303344709922886 and "!assign" in message.content.lower():
		bluecount = await rolemembers(message.channel,834493684938571776)
		redcount = await rolemembers(message.channel,834493740840255539)
		if bluecount > redcount:
			role = discord.utils.get(message.guild.roles,name="Red Team")
		elif redcount > bluecount:
			role = discord.utils.get(message.guild.roles,name="Blue Team")
		elif redcount == bluecount:
			wt=r.randint(1,2)
			if wt==1:
				role = discord.utils.get(message.guild.roles,name="Blue Team")
			elif wt==2:
				role = discord.utils.get(message.guild.roles,name="Red Team")
			else:
				await message.channel.send("AN ERROR HAS OCCURRED. PLEASE IMMEDIATELY DM A STAFF. ERROR CODE:1")
				return
		print(role)
		await message.channel.send(f"You are on {role}.")
		await message.author.add_roles(role)
	if message.content.startswith("!help"):
		embed=discord.Embed(title="Help Function",description='Tells you all the commands!', color = discord.Colour(0x32a852))
		embed.add_field(name = "!help",value = "This command")
		embed.add_field(name = "!war",value = "Try it out, its kinda fun easter egg!")
		embed.add_field(name = "!shop",value = "Shows the shop! Can only be used in <#834501702420791356>.")
		embed.add_field(name="!buy [item]",value="buys items from the shop! Can only be used in <#834501702420791356>.")
		embed.add_field(name="!build [item]",value="Build things! Only trench for now, but will expand in the future.")
		await message.channel.send(embed=embed)
	if message.content.startswith("!hash"):
		await message.channel.send('<#892958145868083230>')
	if message.content.lower().startswith("!initiateplayerstats"):
		if await ModRole(message.author, message) == "Mod":
			for i in [m for m in message.guild.members if not m.bot]:
				whichteam = await Role(i, message)
				name = str(i)
				playerstats[name] = [100, whichteam]
				db["playerstats"] = playerstats
			print(playerstats)
			await message.channel.send("Playerstats successfully initiated. Here is the current value: " + str(playerstats))
		else:
			await message.channel.send("You are not allowed to use that command!")
keep_alive()
client.run(my_secret)
