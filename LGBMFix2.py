import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
import warnings
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings('ignore')

##데이터 불러오기
train_df = pd.read_csv('C:/Users/HP/Desktop/competition_data/train.csv')
"""train_aug_df = pd.read_csv('C:/Users/HP/Desktop/competition_data/train_new.csv')
test_df = pd.read_csv('C:/Users/HP/Desktop/competition_data/test.csv')
train_df = pd.concat([train_df, train_aug_df])"""

##필요없는 COLUMN 삭제
train_df = train_df.drop(['index'], axis = 1)
"""test_df = test_df.drop(['index', 'country'], axis = 1)"""

label_encoder = LabelEncoder()
train_df['country'] = label_encoder.fit_transform(train_df['country'])

##결측치 대치
##train_df.interpolate(method = 'linear', inplace = True)
train_df.mode()

##데이터 정보 출력
##train_df = train_df.astype('int')
train_df.head()
train_df.info()

train_df.to_csv("submissiondata.csv",index = False)

##train을 target과 feature로 나누기
feature=train_df.drop(['nerdiness'], axis=1)
target=train_df['nerdiness']
"""X_train=train_df.drop(['nerdiness'], axis=1)
Y_train=train_df['nerdiness']"""

##train_df를 훈련 셋과 테스트 셋으로 나누기
X_train,X_test,Y_train,Y_test = train_test_split(feature,target, test_size=0.2, random_state=55)

##하이퍼 파라미터
"""lgbm_clf = LGBMClassifier(
            n_estimators=1000, 
            num_leaves=50, 
            subsample=0.8, 
            min_child_samples=600, 
            max_depth=200
        )"""

lgbm_clf = LGBMClassifier(n_estimators=1000)

##모델 학습
lgbm_clf.fit(X_train, Y_train)
"""lgbm_clf.fit(X_train, Y_train)"""

##예측 실행
lgbm_pred = lgbm_clf.predict(X_test)


# 제출 파일 생성
"""submission = pd.read_csv('C:/Users/HP/Desktop/competition_data/sample_submission.csv')
submission
submission['nerdiness'] = lgbm_pred
submission
submission.to_csv("baseline.csv", index = False)"""

print("정확도 : {0: .4f}".format(accuracy_score(Y_test,lgbm_pred)))