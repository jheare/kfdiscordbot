import discord
from discord import app_commands
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
import json

load_dotenv()

# TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}! This is a slash command!",
    ephemeral=True)

@bot.tree.command(name="say")
@app_commands.describe(arg = "What should I say?")
async def say(interaction: discord.Interaction, arg: str):
    if arg == "Boop be doop":
        await interaction.response.send_message(f"{interaction.user.name}! said `{arg}`")
    else:
        await interaction.response.send_message("You're no fun")

@bot.tree.command(name="findepisode")
@app_commands.describe(person = "Who do you want to learn about?")
async def say(interaction: discord.Interaction, person: str):
    tofind = person.lower()
    arr_of_eps = []
    with open(r'KFEpisodeData.json', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        for x in data:
            if tofind in data[x]:
                arr_of_eps.append(x)
    if len(arr_of_eps) == 0:
        string_to_return = "isn't found in any episodes!"
    else:
        string_to_return = "is found in episodes " + ', '.join(str(x) for x in arr_of_eps)
    await interaction.response.send_message(f"`{person}` `{string_to_return}`")
    # await interaction.response.send_message(f"`{person}` is in episode 3")






# @bot.command(name='99')
# async def nine_nine(ctx):
#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]

#     response = random.choice(brooklyn_99_quotes)
#     await ctx.send(response)

bot.run(os.getenv('DISCORD_TOKEN'))