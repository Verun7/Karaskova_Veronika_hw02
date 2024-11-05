import pandas
import json


def find_nan_and_split(one_field):
    one_field = str(one_field)
    if one_field == "nan":
        return []
    else: 
        one_field_split = one_field.split(", ") 
        return(one_field_split)
    
df_netflix = pandas.read_csv("netflix_titles.tsv", sep="\t")
netflix_list_of_dictionary = []
for index, row in df_netflix.iterrows():
    netflix_dictionary = {}
    netflix_dictionary["title"] = row["PRIMARYTITLE"]
    netflix_dictionary["directors"] = find_nan_and_split(row["DIRECTOR"])
    netflix_dictionary["cast"] = find_nan_and_split(row["CAST"])
    genres = row["GENRES"]
    genres = str(genres)
    genres_split = genres.split(",")
    netflix_dictionary["genres"] = genres_split
    decade = row["STARTYEAR"]
    decade_rounded = (decade // 10) * 10
    netflix_dictionary["decade"] = decade_rounded
    netflix_list_of_dictionary.append(netflix_dictionary)

with open("hw02_output.json", mode="w", encoding="utf-8") as file:
    json.dump(netflix_list_of_dictionary, file, ensure_ascii=False, indent=4)