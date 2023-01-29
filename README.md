# kfdiscordbot
Making a Knowledge Fight Discord bot

## data

*(From 29th Jan 2023)*

__THE LASTEST EPISODE ON THIS REPO IS 739__

This was originally taken off of a GDrive file made by Anonymous Wonk Rexford Tugwell and then edited by CelestAI - https://www.reddit.com/user/CelestAI - on Reddit.

The OG spreadsheet got deleted.

The rest of the data is taken from CelestAI's github repo - https://github.com/RainbowBatch/kfdb

## folders

### search
This is where search lives. If you need to reindex then please use the file USEMETOINDEX. It will create an up-to-date search index for the actual engine. It's janky but it works! (Obv to be fixed later)

### misc
Misc just has me sketching out user stories and a potential schema

### refine data
_Updated to no longer be crimes against man and Gd (29/01/2023)_
If you want to pull and refine the data to be the latest available on RainbowBatch's repo just go to ./refinedata/masterrefinefolder/GETANDFORMATALLDATA.py. It'll spit out DISCORD_FINAL - but this is also the final format required to make the search engine work (that's a whole 'nother thing here - https://github.com/oddpotato/kfdiscordsearch)

The HOWTOGETDATA file in that folder will tell you what to do if you for some reason want to pull and format everything manually and step-by-step

**__IMPORTANT NOTE__**

If for some reason the data isn't coming out how you want it, please check the OG repo because I have no control over that and occasionally the data formatting gets changed which means this repo will also need updating

**__Sub-folder 'whatsmissing'__**

This is what episodes have no people data, no themes data, and no notable bits. These _do_ have deep dive data as that's just automatically extracted from episode transcripts. The rest of the data should be added but that might have to manually which...eep.

## 'the plan' such as it is

The data is formatted - we have a working Whoosh engine that's being hooked up to a website in the kfdiscordsearch repo and now I want to get this up and running as a Discord bot in EC2. Unsure as to how EC2 will feel about this but as of 29-01-2023 that's the plan.

(Small note on search engine - it's held together by a very complex Rube Goldberg machine involving Elastic File System hosting the indexed data for lambda because I don't want to learn ElasticSearch on my Saturdays yet...I'll get there)

## the janky bit

## get bot

https://discord.com/api/oauth2/authorize?client_id=1031221257846398986&permissions=395137068032&scope=bot

^^^^ That's the link to invite the discord bot to your server