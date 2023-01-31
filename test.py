# import requests
# import json

# jsontosend = {
#   "{\"fields\": [\"topics_tostring\",\"people_tostring\",\"alex_says_tostring\"], \"queries\": [\"Steve\",\"Reset\",\"NONK\",\"Fuck\",\"shit\"]}"
# }

# personsearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
# print(personsearch.text)

# jsonnormal = {
#     "fields": ["people_tostring", "topics_tostring"],
#     "queries": ["Steve", "NONK"]
# }

# personnormaljson = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsonnormal))
# print(personnormaljson.text)

first_name = "Emma"
second_name = "Watson"

print ("The first name: " + str(first_name))
print ("The second name: " + str(second_name))

list = [first_name, second_name]
string = "\n * ".join(list)

print ("The appended string: " + string)