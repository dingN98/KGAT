import pandas as pd

filepath = 'movies.csv'
# with open(filepath,'r') as f:
#     for line in f:
#         print(line)


csv_result = pd.read_csv(filepath)
row_list = csv_result.values.tolist()
# print(row_list)
genre_list = []
genre_id = 0
for line in row_list:
    genres = line[2].split('|')
    for genre in genres:
        if genre not in genre_list:
            genre_list.append(genre)
            print("%s %s"%(genre,genre_id))
            genre_id = genre_id + 1
    # print(genres)

# 写入
file_goal_path = 'movies_genres.txt'
genre_id = 0
with open(file_goal_path,'w') as file_goal:
    for genre in genre_list:
        file_goal.write("%s %s\n"%(genre,genre_id))
        genre_id = genre_id + 1

file_goal.close()

