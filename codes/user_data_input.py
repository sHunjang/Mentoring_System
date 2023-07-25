import re

def user_data(name, experience, skills, desired_company, certification, language_scores):
    # 사용자의 정보 입력
    name = input("이름을 입력하세요: ")
    experience = input("경력 여부를 입력하세요(경력이 있는 경우 몇년차인지): ")
    skills = input("기술 스택을 입력하세요 (쉼표로 구분): ").split(", ")
    desired_company = input("희망 기업을 입력하세요(없을 경우 'enter' 입력): ")
    certification = input("취득한 자격증을 입력하세요 (없으면 'enter' 입력) : ").split(", ")

    #사용자가 경력이 있는 경우 년차를 저장
    if experience != '신입':
        experience_year = re.sub(r'[^0-9]', '', experience)


    # 사용자로부터 외국어 역량을 key값과 점수 value값을 입력 받음
    language_scores = {}
# 사용자로부터 외국어 역량과 점수를 입력받음
    while True:
        language_ability = input("외국어 역량을 입력하세요 (종료하려면 'enter' 입력) : ")
        if language_ability == '':
            break

        score = input("점수를 입력하세요 : ")

        # language_scores 딕셔너리에 외국어 역량, 점수 저장
        language_scores[language_ability] = int(score)


    # 사용자가 활동한 프로젝트를 key값으로 받고, 해당 프로젝트에 활용한 기술을 value로 입력 받음
    project = {}
    while True:
        project_name = input("활동한 프로젝트 이름을 입력하세요(종료하려면 'enter' 입력) : ")
        if project_name == '':
            break
        project_skill = input("프로젝트에 활용한 기술을 입력하세요 : ")
        project[project_name] = project_skill


    # 사용자가 참석한 대외 활동을 key값으로 받고 해당 대외활동의 주제를 value값으로 받음
    activity = {}
    while True:
        activity_name = input("참석한 대외활동 내역을 입력하세요(종료하려면 'enter' 입력) : ")
        if activity_name == '':
            break
        activity_subject = input("대외활동의 주제를 입력하세요 : ")
        activity[activity_name] = activity_subject



    # 사용자의 정보 출력
    print("이름 : ", name)
    if experience != '신입':
        print("경력 : ", "경력 " + experience_year + "년차")
    else:
        print("경력 : 신입")
    print("기술 스택 : ", skills)
    print("희망 기업 : ", desired_company)
    print("어학 역량 : ", language_scores)
    print("활동한 프로젝트 : ", project)
    print("대외 활동 내역 : ", activity)
    print("기술 스택 : ", skills)
    print("희망 기업 : ", desired_company)
    print("어학 역량 : ", language_scores)
    print("활동한 프로젝트 : ", project)
    print("대외 활동 내역 : ", activity)
    print("자격증 : ", certification)

