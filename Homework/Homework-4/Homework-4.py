import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드 및 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'  # 맥북 용 폰트 설정 
df = pd.read_csv('hw2.csv', encoding='utf-8')

# 모든 숫자 데이터가 실제 숫자 데이터타입(float or int)으로 변환되도록 함
for column in df.columns[2:]:  # 첫 번째 열은 선수 이름, 두 번째 열은 팀명이므로 제외
    df[column] = pd.to_numeric(df[column], errors='coerce')

def sort_and_save():
    column_name = input("어떤 기록으로 정렬하시겠습니까? (예: HR): ")
    if column_name not in df.columns:
        print("잘못된 항목명을 입력하셨습니다.")
        return
    sorted_df = df[['선수명', column_name]].sort_values(by=column_name, ascending=False)
    print(sorted_df)
    sorted_df.to_csv(f"sorted_by_{column_name}.csv", index=False)

def group_and_save():
    for team, group in df.groupby('팀명'):
        print(f"팀명: {team}\n", group, "\n")
        group.to_csv(f"grouped_by_{team}.csv", index=False)

def show_player_stat():
    player_name = input("선수명을 입력하세요: ")
    column_name = input("확인하고 싶은 항목을 입력하세요 (예: AVG): ")
    if column_name not in df.columns:
        print("잘못된 항목명을 입력하셨습니다.")
        return
    player_row = df[df['선수명'] == player_name]
    if not player_row.empty:
        print(player_row[column_name].values[0])
    else:
        print("선수를 찾을 수 없습니다.")

def plot_pie_chart():
    # 팀별로 HR 개수 합산
    team_hr = df.groupby('팀명')['HR'].sum()
    
    # 합계 데이터를 출력하여 데이터 확인
    print(df[['팀명', 'HR']])
    print(team_hr)

    # 합계가 0이 아닌 팀만 선택 (데이터에서 누락된 값이나 0 값이 있는지 확인하기 위함)
    team_hr = team_hr[team_hr != 0]

    # 파이 차트 그리기
    fig, ax = plt.subplots()
    team_hr.plot.pie(autopct='%1.1f%%', startangle=90, ax=ax, labels=team_hr.index)
    ax.set_title('HR by Team')
    ax.set_ylabel('')  # y 레이블 제거
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, labels=team_hr.index)

    # 차트 보이기
    plt.show()

while True:
    print("1: 특정 기록으로 선수 데이터 정렬")
    print("2: 팀별 데이터 그룹 및 저장")
    print("3: 선수명과 항목으로 데이터 조회")
    print("4: 팀별 HR 파이 차트 출력")
    print("0: 종료")
    choice = input("원하는 기능의 번호를 입력하세요: ")

    if choice == "1":
        sort_and_save()
    elif choice == "2":
        group_and_save()
    elif choice == "3":
        show_player_stat()
    elif choice == "4":
        plot_pie_chart()
    elif choice == "0":
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
