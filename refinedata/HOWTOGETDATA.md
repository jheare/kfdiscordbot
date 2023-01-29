# HOW TO EXTRACT AND FORMAT DATA FOR SEARCH

## Steps for Main

1. Copy final.json from CelestAI's github repo - https://github.com/RainbowBatch/kfdb
2. Run ./gettingbulkofdata/getbulkdata.py - This initially formats all of the data for you
3. 

## Steps for Deep Dive

1. Copy raw_entities from CelestAI's github repo - https://github.com/RainbowBatch/kfdb
2. Run ./gettingdeepdivetopics/subjects.py - This initially extracts and _starts_ the formatting process for all the data
3. Run ./formattingaliases/formattingaliases.py - This cleans up the aliases in the deep dive topics (i.e. "Alex\r\n": 132, becomes Alex)

## To combined

1. Copy your deepdivetopics and formatteddata into ./combinejson and run combinedata.py