import discord
from discord import app_commands
from discord.ext import commands

import asyncio

from cogs.dataformatters.findnicknames import FindNicknames
#from cogs.dataformatters.shortenmessage import ShortenMessage

import simplejson as json
import requests

class Search(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.searchurl = "http://fin.apps-kf-search-prod.s3-website-us-east-1.amazonaws.com/"
        self.footertext = "Want to see more detail? Check out the search engine"
        self.footericon = "https://pbs.twimg.com/profile_images/1071046862080221184/MaGfASpN_400x400.jpg"
        self.get_nicknames = FindNicknames()
        #self.shortenmessage = ShortenMessage()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Search cog is loaded')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(
            f"Synced {len(fmt)} commands to the server"
        )
        return

    #@commands.Command()
    @app_commands.command(name="episodebyperson", description="Find episodes featuring...")
    async def episodebyperson(self, interaction: discord.Interaction, person: str):
        await interaction.response.defer(ephemeral=False, thinking=True)
        if person == "Alex Jones":
            embed=discord.Embed(title="Please don't", description = "My poor little brain can't handle that.", url=self.searchurl)
            embed.set_image(url="https://media-cldnry.s-nbcnews.com/image/upload/mpx/2704722219/2022_10/1665605735247_n_hallie_brk_jones_billion_verdict_221012_1920x1080-c63t1h.jpg")
            await interaction.followup.send(embed=embed)
            return True
        get_name_array = self.get_nicknames.checknames(person)
        jsontosend = {
        "fields": ["people_tostring", "topics_tostring"],
        "queries": get_name_array
        }
        personsearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
        formatresp = json.loads(personsearch.text)
        formatbody = json.loads(formatresp['body'])
        episode_array = []
        for i in formatbody:
            episode_array.append(i)
        message = ""
        messagestring = ""
        if len(episode_array) == 1:
            messagestring = "\n * ".join(episode_array)
            message = f"`{person}` is in episode:"
        elif len(episode_array) > 1:
            messagestring = "\n * ".join(episode_array)
            message = f"`{person}` is in episodes:"
        else:
            embed=discord.Embed(title="Nothing found!", url=self.searchurl)
            embed.set_image(url="https://media.tenor.com/5U4tWWKQGDkAAAAM/alex-jones-crying.gif")
            await interaction.followup.send(embed=embed)
        embed=discord.Embed(title=message, description= "* " + messagestring, url=self.searchurl)
        if message != "":
            embed.set_footer(text=self.footertext, icon_url=self.footericon)
            await interaction.followup.send(embed=embed)

    @app_commands.command(name="alexsays", description="When did Alex say...")
    async def alexsays(self, interaction: discord.Interaction, alexsays: str):
        await interaction.response.defer(ephemeral=False, thinking=True)
        jsontosend = {
        "fields": ["alex_says_tostring"],
        "queries": [alexsays]
        }
        alexsayssearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
        formatresp = json.loads(alexsayssearch.text)
        formatbody = json.loads(formatresp['body'])
        episode_array = []
        for i in formatbody:
            episode_array.append(i)
        message = ""
        if len(episode_array) == 1:
            messagestring = "\n * ".join(episode_array)
            message = f"Alex says `{alexsays}` in episode:"
        elif len(episode_array) > 1:
            messagestring = "\n * ".join(episode_array)
            message = f"Alex says `{alexsays}` in episodes:"
        else:
            embed=discord.Embed(title="Nothing found!", url=self.searchurl)
            embed.set_image(url="https://media.npr.org/assets/img/2022/08/05/ap22216570430921-2dceca1166ed5d3a06b0c717f3a7da7c80c6c9c9-s1100-c50.jpg")
            await interaction.followup.send(embed=embed)
        embed=discord.Embed(title=message, description= "* " + messagestring, url=self.searchurl)
        if message != "":
            embed.set_footer(text=self.footertext, icon_url=self.footericon)
            await interaction.followup.send(embed=embed)

    @app_commands.command(name="topics", description="When do they talk about...")
    async def topics(self, interaction: discord.Interaction, topic: str):
        await interaction.response.defer(ephemeral=False, thinking=True)
        if topic == "Alex Jones":
            embed=discord.Embed(title="Please don't", description = "My poor little brain can't handle that.", url=self.searchurl)
            embed.set_image(url="https://media-cldnry.s-nbcnews.com/image/upload/mpx/2704722219/2022_10/1665605735247_n_hallie_brk_jones_billion_verdict_221012_1920x1080-c63t1h.jpg")
            await interaction.followup.send(embed=embed)
            return True
        jsontosend = {
        "fields": ["topics_tostring"],
        "queries": [topic]
        }
        topicsearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
        formatresp = json.loads(topicsearch.text)
        formatbody = json.loads(formatresp['body'])
        episode_array = []
        for i in formatbody:
            episode_array.append(i)
        message = ""
        messagestring = ""
        if len(episode_array) == 1:
            messagestring = "\n * ".join(episode_array)
            message = f"`{topic}` comes up in episode:"
        elif len(episode_array) > 1:
            messagestring = "\n* ".join(episode_array)
            message = f"`{topic}` comes up in episodes:"
        else:
            embed=discord.Embed(title="Nothing found!", url=self.searchurl)
            embed.set_image(url="https://static.independent.co.uk/2022/09/22/21/SEI126493450.jpg")
            await interaction.followup.send(embed=embed)
        embed=discord.Embed(title=message, description="* " + messagestring, url=self.searchurl)
        if message != "":
            embed.set_footer(text=self.footertext, icon_url=self.footericon)
            await interaction.followup.send(embed=embed)
        #await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Search(bot))