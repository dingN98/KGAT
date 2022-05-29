import pandas as pd

# filepath = 'movies.csv'
filepath = '../0528/movies.csv'
# with open(filepath,'r') as f:
#     for line in f:
#         print(line)


csv_result = pd.read_csv(filepath,encoding='utf-8')
row_list = csv_result.values.tolist()
# print(row_list)
relation_list = []
for line in row_list:
    movie_name = line[1]
    genres = line[2].split('|')
    for genre in genres:
        relation = "%s,genre,%s"%(movie_name,genre)
        relation_list.append(relation)
    # print(genres)
print("关系的长度 %s"%(len(relation_list)))
# 写入
file_goal_path = 'movies_relations.csv'
with open(file_goal_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("movieName,relation,genre\n")
    for relation in relation_list:
        file_goal.write("%s\n"%(relation))


file_goal.close()

