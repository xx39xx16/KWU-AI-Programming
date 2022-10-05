import numpy as np

with open('hw2.csv','r', encoding='utf-8') as csv_file:
    data=[]
    for line in csv_file:
        data.append(line.strip().split(',')) #파일 불러오기 및 리스트 설정

#선수명 입력시 세부 항목들의 값 출력
q1= input("선수명을 입력해주세요 : ")
for b in data:
    if q1 in b:
        print(b[1:15])

#선수명과 특정 항목 입력시 해당 값 출력
q2= input("선수명을 입력해주세요 : ")
q3= input("알고 싶은 특정 항목을 입력해주세요 : ")
nametype = data[0]
for b in data:
    if q2 in b:
        c = nametype.index(q3)
        print(b[c])

#특정 항목을 선택하면 선수명과 항목값을 매칭하여 내림차순으로 정렬
d= np.array(data)
q4 = input("특정 항목을 선택해주세요 : ")
s = nametype.index(q4)
name = d[1:,0]
ability = d[1:,s]
name_list = name.tolist()
ability_list = ability.tolist()
ability_list = list(map(int,ability_list))

couple=dict(zip(name_list, ability_list))
print(sorted(couple.items(), key=lambda s:s[1], reverse = True))
