import pandas as pd
import json

# filepath = '../metadata.json'
filepath = '../fullData/metadata.json'

director_list = []
director_list_tmp = []
star_list = []
star_list_tmp = []

director_id = 1
star_id = 1

with open(filepath,'r',encoding='utf-8') as f:
    for line in f:
        line = line.strip("\n")
        data = json.loads(line)

        director = data["directedBy"]
        stars = data["starring"].split(",")
        stars = [i.strip() for i in stars]

        if director not in director_list_tmp:
            director_list_tmp.append(director)
            director_list.append((director,director_id))
            director_id = director_id + 1

        for star in stars:
            if star not in star_list_tmp:
                star_list_tmp.append(star)
                star_list.append((star,star_id))
                star_id = star_id + 1


print("导演数量 %s"%(len(director_list)))
print("演员数量 %s"%(len(star_list)))

# 写入
directors_index_path = 'directors_index.csv'
with open(directors_index_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("directorName,directorId\n")
    for line in director_list:
        file_goal.write("%s,%s\n"%(line[0],line[1]))

stars_index_path = 'stars_index.csv'
with open(stars_index_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("starName,starId\n")
    for line in star_list:
        file_goal.write("%s,%s\n"%(line[0],line[1]))

file_goal.close()
