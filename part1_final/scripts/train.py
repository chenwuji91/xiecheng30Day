import sys
import xgboost as xgb
import numpy as np
from sklearn.datasets import load_svmlight_file

def load(filename):
    X,y = load_svmlight_file(filename)
    return X.toarray(),y

def train(X,Y,param):
    clf = xgb.XGBRegressor(**param)
    clf.fit(X,Y)
    return clf

def predict(clf,X):
    return clf.predict(X)

def output(outputfile,predlist):
    f = file(outputfile,"w+")
    f.write("val\n")
    for i in xrange(len(predlist)):
        f.write("%f\n"%predlist[i])
    f.close()

def run(trainfile,validfile,validout,testfile,testout,maxdepth,lr,nest):
    params = {
    "max_depth":int(maxdepth),
    "learning_rate":float(lr),
    "n_estimators":int(nest),
    #"subsample":0.9,
    #"colsample_bytree":0.8
    }
    train_x,train_y = load(trainfile)
    valid_x,valid_y = load(validfile)
    test_x,test_y = load(testfile)
#    model = train(train_x,train_y,params)
    newtrain_x = np.concatenate((train_x,valid_x))
    newtrain_y = np.concatenate((train_y,valid_y))
#    valid_pred = predict(model,valid_x)
#    getscore(valid_pred,valid_y)
    model = train(newtrain_x,newtrain_y,params)
    valid_pred = predict(model,valid_x)
#    getscore(valid_pred,valid_y)
    test_pred = predict(model,test_x)
    output(validout,valid_pred)
    output(testout,test_pred)
def getscore(predval,realval):
    print reduce(lambda x,y: x + y,map(lambda x,y:abs(y-x),predval,realval))/float(len(realval))

if __name__ == '__main__':
     run(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])


