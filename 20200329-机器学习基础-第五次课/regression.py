"""
使用svm实现回归算法
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR


def load_data():
    # 加载数据
    df = pd.read_csv('./data_reg.csv')
    x = df[['AT', 'V', 'AP', 'RH']]
    y = df[['PE']]
    
    # 数据预处理
    sc =StandardScaler()
    x_pro = sc.fit_transform(x)
    # 数据分割
    x_train, x_test, y_train, y_test = train_test_split(x_pro, y, test_size=0.3, random_state=123)
    return x_train, x_test, y_train, y_test

def get_svr():
    return SVR(gamma='auto')

def train(svr, x, y):
    svr.fit(x, y.values.ravel())

def get_score(svr, x, y):
    return svr.score(x, y)

def main():
    x_train, x_test, y_train, y_test = load_data()
    svr = get_svr()
    train(svr, x_train, y_train)
    score = get_score(svr, x_test, y_test)
    print('score:', score)



if __name__ == '__main__':
    main()
