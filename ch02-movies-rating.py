import matplotlib.pyplot as plt
import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=mnames)
data = pd.merge(pd.merge(users, ratings), movies[1:1000])
data[data.user_id == 1]         #查看用户id为1，对所有电影的评分.

#不同性别对不同电影的平均评分.

mean_ratings_by_gender = data.pivot_table(values='rating',index='title',columns='gender', aggfunc='mean')
mean_ratings_by_gender.head(10)     #查看前10条数据

#mean_ratings_by_gender增加一列，男女的平均评分差.
mean_ratings_by_gender['diff'] = mean_ratings_by_gender.F - mean_ratings_by_gender.M
mean_ratings_by_gender.head()

#哪些电影是男女评分差异最大的（男性评分高女生评分低，女性高男性低）.
sorted_by_diff= mean_ratings_by_gender.sort_values(by='diff',ascending=True)




# 不同电影的评分次数.
total_rating_by_title = data.groupby('title').size()
total_rating_by_title[0:10]

# 评分次数最多的10部电影.
top_10_total_rating = total_rating_by_title.sort_values(ascending=False).head(10)

# 评分最高的10大电影(注：最高分为5.0)
mean_ratings_by_title = data.pivot_table(values='rating',index='title',aggfunc='mean')
top_10_mean_ratings = mean_ratings_by_title.sort_values(by='rating',ascending=False).head(10)

# 统计出热门电影
hot_movie = total_rating_by_title[total_rating_by_title>1000]
print(len(hot_movie))
hot_movie

#热门电影的评分
hot_movie_mean_rating = mean_ratings_by_title[hot_movie]
print(len(hot_movie_mean_rating))
hot_movie_mean_rating

if __name__ == '__main__':
    print(len(users))
    print(users.head())
    print(len(movies))
    print(movies.head())
    print(len(ratings))
    print(ratings.head())

