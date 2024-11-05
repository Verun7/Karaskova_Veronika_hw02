import pandas
import json
# for index, row in df_netflix.iterrows()

def find_nan(one_field):
    one_field = str(one_field)
    if one_field == "nan":
        return []
    else: 
        one_field_split = one_field.split(",") 
        one_field_split_strip = [item.strip()for item in one_field_split]
        return(one_field_split_strip)
    
df_netflix = pandas.read_csv("netflix_titles.tsv", sep="\t")
netflix_list_of_dictionary = []
# count_rounds = 0
# for row in df_netflix:
for index, row in df_netflix.iterrows():
    netflix_dictionary = {}
    netflix_dictionary["title"] = df_netflix["PRIMARYTITLE"]
    netflix_dictionary["directors"] = find_nan(df_netflix["DIRECTOR"])
    netflix_dictionary["cast"] = find_nan(df_netflix["CAST"])
    netflix_dictionary["genres"] = find_nan(df_netflix["GENRES"])
    decade = df_netflix["STARTYEAR"]
    # decade = int(decade)
    decade_rounded = (decade // 10) * 10
    netflix_dictionary["decade"] = decade_rounded
    # count_rounds += 1
    netflix_list_of_dictionary.append(netflix_dictionary)

with open("hw02_output.json", mode="w", encoding="utf-8") as file:
    json.dump(netflix_list_of_dictionary, file, ensure_ascii=False, indent=4)




