import pandas as pd
import json

filepath = 'metadata.json'
# filepath = '../0528/movies.csv'
relation_list = []
with open(filepath,'r',encoding='utf-8') as f:
    for line in f:
        line = line.strip("\n")
        data = json.loads(line)

        movie_name = data["title"]
        directed_by = data["directedBy"]
        avg_rating = data["avgRating"]

        relation_directed_by = "%s,directedBy,%s"%(movie_name,directed_by)
        relation_avg_rating = "%s,avgRating,%s"%(movie_name,avg_rating)

        relation_list.append(relation_directed_by)
        relation_list.append(relation_avg_rating)

        starring = data["starring"].split(", ")
        for star in starring:
            relation_starring = "%s,starring,%s"%(movie_name,star)
            relation_list.append(relation_starring)

print("关系的长度 %s"%(len(relation_list)))
# 写入
file_goal_path = 'movies_relations_stars.csv'
with open(file_goal_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("movieName,relation,entityName\n")
    for relation in relation_list:
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

