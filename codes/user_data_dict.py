import re

def user_data():
    user_info = {}

    user_info["name"] = input("이름을 입력하세요: ")
    experience = input("경력 여부를 입력하세요(경력이 있는 경우 몇년차인지): ")
    user_info["experience"] = experience
    user_info["skills"] = input("기술 스택을 입력하세요 (쉼표로 구분): ").split(", ")
    user_info["desired_company"] = input("희망 기업을 입력하세요(없을 경우 'enter' 입력): ")
    user_info["certification"] = input("취득한 자격증을 입력하세요 (없으면 'enter' 입력) : ").split(", ")

    if experience != '신입':
        experience_year = re.sub(r'[^0-9]', '', experience)
        user_info["experience_year"] = int(experience_year)

    language_scores = {}
    while True:
        language_ability = input("외국어 역량을 입력하세요 (종료하려면 'enter' 입력) : ")
        if language_ability == '':
            break

        score = input("점수를 입력하세요 : ")
        language_scores[language_ability] = int(score)

    user_info["language_scores"] = language_scores

    project = {}
    while True:
        project_name = input("활동한 프로젝트 이름을 입력하세요(종료하려면 'enter' 입력) : ")
        if project_name == '':
            break
        project_skill = input("프로젝트에 활용한 기술을 입력하세요 : ")
        project[project_name] = project_skill

    user_info["projects"] = project

    activity = {}
    while True:
        activity_name = input("참석한 대외활동 내역을 입력하세요(종료하려면 'enter' 입력) : ")
        if activity_name == '':
            break
        activity_subject = input("대외활동의 주제를 입력하세요 : ")
        activity[activity_name] = activity_subject

    user_info["activities"] = activity

    return user_info

user_info_dict = user_data()

# Print the user data
print(user_info_dict)
