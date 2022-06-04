import pandas as pd
import json

# filepath = '../testData/ratings.json'
filepath = '../fullData/ratings.json'
relation_list = []
with open(filepath,'r',encoding='utf-8') as f:
    for line in f:
        line = line.strip("\n")
        data = json.loads(line)

        user = data["user_id"]
        movie = data["item_id"]
        rating = data["rating"]
        relation_rating = "%s,%s,%s"%(user,movie,rating)
        relation_list.append(relation_rating)

print("关系的长度 %s"%(len(relation_list)))

# 写入
file_goal_path = 'ratings.csv'
with open(file_goal_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("userId,movieId,rating\n")
    for relation in relation_list:
        file_goal.write("%s\n"%(relation))

file_goal.close()
