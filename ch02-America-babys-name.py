import pandas as pd

names1880 = pd.read_csv('datasets/babynames/yob1880.txt',names=['name','sex','births'])
names1880.head()

def concatAlldata():
    # 将所有数据都组装到一个dataframe里
    years = range(1880, 2011)
    pieces = []
    columns = ['name', 'sex', 'births']

    for year in years:
        path = 'datasets/babynames/yob%d.txt' %year
        frame = pd.read_csv(path,names=columns)
        frame['year']=year

if __name__ == '__main__':
    print(len(names1880))
    # 按照性别统计
    names1880.groupby('sex').births.sum()
    names1880.groupby('sex').name.sum()

