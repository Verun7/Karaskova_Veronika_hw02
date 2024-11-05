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

# print(df_netflix["PRIMARYTITLE"])
print(df_netflix.iterrows()) 
#     netflix_dictionary["title"] = df_netflix["PRIMARYTITLE"]
