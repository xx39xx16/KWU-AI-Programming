
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
import numpy as np
import matplotlib.pyplot as plt

# 데이터셋 읽기 - 수정된 파일 경로
df = pd.read_csv('/Users/kimsolbi/Desktop/AIP/hw5/winequality-red.csv')

# 'quality' 열에 대한 원-핫 인코딩
y = pd.get_dummies(df['quality'])

# 'quality' 열을 제외한 나머지를 입력 데이터로 사용
X = df.drop('quality', axis=1)

# 데이터셋의 차원을 확인 (디버깅을 위해)
print(X.shape, y.shape)

# 데이터 정규화
# 성능 향상을 위해 정규화 부분을 추가해줌
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# train과 test set 나누기
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# k-폴드 교차 검증 설정
k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)
fold_no = 1  # fold_no 변수 초기화
acc_per_fold = []

# KFold 교차 검증 수행
for train, val in kf.split(X_train, y_train):
    # 훈련 데이터와 검증 데이터 분할
    X_train_fold, X_val_fold = X_train[train], X_train[val]
    y_train_fold, y_val_fold = y_train.iloc[train], y_train.iloc[val]
    # 모델 구축
    model = Sequential()
    model.add(Dense(64, input_shape=(X_train_fold.shape[1],), activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(y_train_fold.shape[1], activation='softmax'))
    model.summary()

    # 모델 컴파일
    model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

    # 체크포인트 및 얼리 스토핑 설정
    checkpointer = ModelCheckpoint('best_model_fold_{}.h5'.format(fold_no), save_best_only=True, monitor='val_loss', mode='min')
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, verbose=1)

    # 모델 학습
    history = model.fit(X_train_fold, y_train_fold, epochs=370, batch_size=36, validation_data=(X_val_fold, y_val_fold), callbacks=[early_stopping, checkpointer], verbose=1)

     # 성능 평가
    scores = model.evaluate(X_val_fold, y_val_fold, verbose=0)
    acc_per_fold.append(scores[1] * 100)
    fold_no += 1

# 교차 검증 결과 분석
average_accuracy = np.mean(acc_per_fold)
print(f'Average accuracy across all folds: {average_accuracy:.2f}%')

# 정확도 시각화
plt.figure(figsize=(10, 6))
plt.plot(range(1, k+1), acc_per_fold, marker='o', linestyle='-', color='b')
plt.title('Accuracy per Fold')
plt.xlabel('Fold Number')
plt.ylabel('Accuracy (%)')
plt.xticks(range(1, k+1))
plt.grid(True)
plt.show()
# 전체 데이터셋에 대한 모델 성능 평가
# 전체 데이터셋에 대해 동일한 모델 아키텍처를 사용하여 학습 및 평가를 수행합
model = Sequential()
model.add(Dense(64, input_shape=(X_scaled.shape[1],), activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(y.shape[1], activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
model.fit(X_scaled, y, epochs=100, batch_size=32, verbose=1)

# 최종 테스트 세트에서 성능 평가
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'Test Set Accuracy: {test_accuracy*100:.2f}%')
