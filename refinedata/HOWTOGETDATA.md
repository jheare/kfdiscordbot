# HOW TO EXTRACT AND FORMAT DATA FOR SEARCH

## Just Using The Master File

It lives in masterrefinefolder and it'll spit out DISCORD_FINAL which is the json file formatted to work with Whoosh

## Manually/Step-by-step

So you want to extract and format the data manually? Cool. Here's the step-by-step so you can extract and mess about with each stage at your leisure

### Steps for Main

1. Copy final.json from CelestAI's github repo - https://github.com/RainbowBatch/kfdb
2. Run ./gettingbulkofdata/getbulkdata.py - This initially formats all of the data for you
3. 

### Steps for Deep Dive

1. Copy raw_entities from CelestAI's github repo - https://github.com/RainbowBatch/kfdb
2. Run ./gettingdeepdivetopics/subjects.py - This initially extracts and _starts_ the formatting process for all the data
3. Run ./formattingaliases/formattingaliases.py - This cleans up the aliases in the deep dive topics (i.e. "Alex\r\n": 132, becomes Alex)

### To Combine

1. Copy your refinedaliases and formatteddata into ./combinejson and run combinedata.py

### To Format

1. Copy combineddatea into formatforsearch and run formatforsearch.py