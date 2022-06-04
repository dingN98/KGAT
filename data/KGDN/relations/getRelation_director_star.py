import pandas as pd
import json
import re

# filepath = '../testData/metadata.json'
filepath = '../fullData/metadata.json'
relation_stars_list = []
relation_directors_list = []

with open(filepath,'r',encoding='utf-8') as f:
    for line in f:
        line = line.strip("\n")
        data = json.loads(line)

        movie_name = data["title"]
        movie_name = re.sub(r'[^a-zA-Z0-9 ()]', '', movie_name)
        director = data["directedBy"]
        director = re.sub(r'[^a-zA-Z0-9 ()]', '', director)
        stars = data["starring"].split(",")
        stars = [re.sub(r'[^a-zA-Z0-9 ()]', '', i.strip()) for i in stars]

        relation_directors = "%s,%s"%(movie_name,director)
        relation_directors_list.append(relation_directors)

        for star in stars:
            relation_stars = "%s,%s"%(movie_name,star)
            relation_stars_list.append(relation_stars)

print("导演关系的长度 %s"%(len(relation_directors_list)))
print("演员关系的长度 %s"%(len(relation_stars_list)))


# 写入
file_goal_path = 'movies_relations_stars.csv'
with open(file_goal_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("movieName,starName\n")
    for relation in relation_stars_list:
        file_goal.write("%s\n"%(relation))

file_goal_path = 'movies_relations_directors.csv'
with open(file_goal_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("movieName,directorName\n")
    for relation in relation_directors_list:
        file_goal.write("%s\n"%(relation))

file_goal.close()

# csv_result = pd.read_csv(filepath,encoding='utf-8')
# row_list = csv_result.values.tolist()
# # print(row_list)
# relation_list = []
# for line in row_list:
#     movie_name = line[1]
#     genres = line[2].split('|')
#     for genre in genres:
#         relation = "%s,genre,%s"%(movie_name,genre)
#         relation_list.append(relation)
#     # print(genres)
# print("关系的长度 %s"%(len(relation_list)))

