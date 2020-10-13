from requests import get
import pandas as pd
import json

df = pd.read_csv("input.csv")
key = ''
separator = '+'
address = []
name = []
place_id = []
keyword_searched = []
website = []

print("The process is now running")

for i in range(len(df['Keyword'])):
    x = df['Keyword'][i].split()
    query = separator.join(x)
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + query + '&key=' + key
    response = get(url)
    json_dictionary = response.json()
    json_lists = json_dictionary.get("results")
    for j in range(len(json_lists)):
        keyword_searched.append(df['Keyword'][i])
        json_dict = json_lists[j]
        address.append(json_dict.get('formatted_address'))
        name.append(json_dict.get('name'))
        place_id.append(json_dict.get('place_id'))

for i in range(len(place_id)):
    url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=' + place_id[i] + '&fields=website&key=' + key
    response = get(url)
    json_dictionary = response.json()
    json_lists = json_dictionary.get("result")
    json_website = json_lists.get("website")
    website.append(json_website)


output_dictionary = {'Keyword Searched For' : keyword_searched, 'Name' : name, 'Address' : address, 'Place_ID' : place_id, 'Website' : website}
output_df = pd.DataFrame(output_dictionary)
print("The process has finished")
output_df.to_csv('output.csv')

