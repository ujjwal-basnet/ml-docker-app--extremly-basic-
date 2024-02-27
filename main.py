from sklearn import datasets 
from sklearn.model_selection import tain_test_split 
from sklearn.ensemble import RandomForestClassifier
from skleran.metrics import accuracy_score
import joblib 

#load datasets 
iris = datasets.load_iris()
X =  iris.data 
y = iris.target 

#split data 
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.30)


rc = RandomForestClassifier()

#fit 
rc.fit(X_train ,  y_train)

#predict 
y_pred = rc.predict(X_test)

#model accuracy 
print(f"accuracy is :{accuracy_score(y_test , y_pred)} " ) 

# saving the trainned model 
joblib.dump(rc , 'iris_model.pkl')
print("model saved")