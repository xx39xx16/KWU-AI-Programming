# 모듈 파일
# 해당 파일 이름은 Homework2.py로 설정했음

def read_csv_file(filename="hw2.csv"):
    with open(filename, "r", encoding="UTF-8-sig") as file:
        lines = file.readlines()

    headers = lines[0].strip().split(',')
    players_data = [line.strip().split(',') for line in lines[1:]]

    return headers, players_data

def get_player_data(player_name, players_data):
    for data in players_data:
        if data[0] == player_name:
            return data
    return None

def sort_by_record(players_data, headers, record):
    try:
        index = headers.index(record)
    except ValueError:
        return []
    
    return sorted(players_data, key=lambda x: x[index], reverse=True)

def group_by_team(players_data):
    teams = {}
    for player in players_data:
        team_name = player[1]
        if team_name not in teams:
            teams[team_name] = []
        teams[team_name].append(player)
    return teams

def find_player_record(players_data, headers, player_name, record):
    player = get_player_data(player_name, players_data)
    if player:
        try:
            index = headers.index(record)
            return player[index]
        except ValueError:
            return None
    return None

def save_to_file(filename, data, headers=None):
    with open(filename, "w", encoding="UTF-8-sig") as file:
        if headers:
            file.write(",".join(headers) + "\n")
        for row in data:
            file.write(",".join(row) + "\n")

def save_grouped_to_file(filename, headers, grouped_data):
    with open(filename, "w", encoding="UTF-8-sig") as file:
        file.write(",".join(headers) + "\n")
        for team, players in grouped_data.items():
            for player in players:
                file.write(",".join(player) + "\n")


------------------------------------------------------------------------------
# 메인 파일
# 메인 파일 파일명은 hw2_1_2020741076.py 로 설정했음 

import Homework2 as kbo

def main():
    header, data = kbo.read_csv_file('hw2.csv')

    while True:
        print("1. 기록별 정렬 및 출력")
        print("2. 팀별 그룹화 및 출력")
        print("3. 선수별 특정 기록 조회")
        print("4. 종료")
        choice = input("선택: ")

        if choice == '1':
            record = input("정렬할 기록을 입력하세요: ")
            sorted_data = kbo.sort_by_record(data, header, record)
            for player_data in sorted_data:
                print(player_data)
            save_choice = input("저장하시겠습니까? (y/n): ")
            if save_choice.lower() == 'y':
                kbo.save_to_file(f"sorted_by_{record}.csv", sorted_data, header)

        elif choice == '2':
            grouped_data = kbo.group_by_team(data)
            for team, players in grouped_data.items():
                print(f"Team: {team}")
                for player in players:
                    print(player)
            save_choice = input("저장하시겠습니까? (y/n): ")
            if save_choice.lower() == 'y':
                kbo.save_grouped_to_file("grouped_by_team.csv", header, grouped_data)

        elif choice == '3':
            player_name = input("선수명을 입력하세요: ")
            record = input("조회할 기록을 입력하세요: ")
            player_record = kbo.find_player_record(data, header, player_name, record)
            if player_record:
                print(f"{player_name}의 {record}: {player_record}")
            else:
                print("선수 또는 기록을 찾을 수 없습니다.")

        elif choice == '4':
            break

if __name__ == '__main__':
    main()
