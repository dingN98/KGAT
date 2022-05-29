import pandas as pd

# filepath = 'movies.csv'
filepath = '../0528/movies.csv'

csv_result = pd.read_csv(filepath,encoding='utf-8')
row_list = csv_result.values.tolist()
# print(row_list)
genre_list = []
movie_list = []

for line in row_list:
    movie_id = line[0]
    movie_name = line[1]
    genres = line[2].split('|')

    movie_list.append((movie_name,movie_id))

    for genre in genres:
        if genre not in genre_list:
            genre_list.append(genre)

print("电影数量 %s"%(len(movie_list)))
print("电影类别数量 %s"%(len(genre_list)))

# 写入
movies_index_path = 'movies_index.csv'
with open(movies_index_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("movieName,movieId\n")
    for line in movie_list:
        file_goal.write("%s,%s\n"%(line[0],line[1]))

genres_index_path = 'genres_index.csv'
genre_id = 1
with open(genres_index_path,'w',encoding='utf-8') as file_goal:
    file_goal.write("genreName,genreId\n")
    for genre in genre_list:
        file_goal.write("%s,%s\n"%(genre,genre_id))
        genre_id = genre_id + 1

file_goal.close()
