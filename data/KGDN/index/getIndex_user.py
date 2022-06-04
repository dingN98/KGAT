import pandas as pd
import json

# filepath = '../testData/ratings.json'
filepath = '../fullData/ratings.json'

user_list = []

with open(filepath,'r',encoding='utf-8') as f:
    for line in f:
        line = line.strip("\n")
        data = json.loads(line)

        user = data["user_id"]
        user_list.append(user)

user_list = list(set(user_list))
print("用户数量 %s"%(len(user_list)))

# 写入
users_index_path = 'user_index.csv'
with open(users_index_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("userId\n")
    for line in user_list:
        file_goal.write("%s\n"%(line))

file_goal.close()
