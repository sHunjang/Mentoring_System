import re

def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    result = len(intersection) / len(union)
    return result

def calc_similarity_percentage(user_skills, company_skills):
    intersection = user_skills.intersection(company_skills)
    required_percentage = len(intersection) / len(company_skills) * 100
    return required_percentage

# 기업 별 채용 조건
companies = {
    "SK": [
        {
            "title": "Application Engineering",
            "required_skills": ["java", "springboot", "sql"],
            "preferential": ["프로그래밍 언어 및 DB 활용", "MSA", "AWS Resource", "Native App."]
        },
        {
            "title": "SoftWare Engineering",
            "required_skills": ["java", "springboot"],
            "preferential": ["금융 및 경제학 관련 지식", "Native App. 개발"]
        }
    ],
    "Toss": [
        {
            "title": "Server Developer",
            "required_skills": ["java", "spring framework"],
            "preferential": ["redis", "kafka", "elk", "네트워크프로그래밍"]
        },
        {
            "title": "iOS Developer",
            "required_skills": ["object-C", "swift"],
            "preferential": ["SDK 개발"]
        }
    ],
    "Coupang": [
        {
            "title": "Senior, Backend engineer (SCM)",
            "required_skills": ["java", "python", "spring"],
            "experience": "경력5년이상",
            "preferential": ["Spring boot", "컴퓨터 과학 석사학위"]
        }
    ],
    "Saltlux": [
        {
            "title": "Web_Developer",
            "required_skills": ["java", "jsp"],
            "preferential": ["정보처리기사", "챗봇구축경험자"]
        }
    ],
    "Wins" : [
        {
            "title" : "SW Developer",
            "required_skills" : ["java", "rdb", "nosql"],
            "preferential" : ["Elastic Search", "python", "hadoop"],
        }
    ],
    "삼진" : [
        {
            "title" : "Embedded SW Developer",
            "required_skills" : ["c", "c++"],
            "experience" : "신입",
            "preferential" : ["임베디드SW", "영어가능자"]
        }
    ],
    "신세계아이앤씨" : [
        {
            "title" : "SW Develop & Operation ",
            "required_skills" : ["java", "c", "c++", "python", "mysql", "R"],
            "experience" : "경력3년이상",
            "preferential" : ["AI챗봇", "doker", "kubernetes", "container기반서비스"]
        }
    ],
    "미디어로그" : [
        {
            "title" : "SW Developer",
            "required_skills" : ["java"],
            "experience" : "신입",
            "preferential" : ["대졸"]
        }
    ],
    "현대이지웰" : [
        {
            "title" : "SW Developer",
            "required_skills" : ["java", "jsp", "jquery", "spring", "strutus2", "mybatis"],
            "experience" : ["신입", "경력2년이상"],
            "preferential" : ["대졸"]
        }
    ],
    "비지에프리테일" : [
        {
            "title" : "하계 채용연계형 인턴",
            "required_skills" : ["java", "jsp", "javascript", "nexacro", "html5"],
            "experience" : ["신입"],
            "preferential" : ["대졸", "학점3점이상"]
        }
    ],
    "넥슨" : [
        {
            "title" : "탐지응용팀 백엔드 개발자",
            "required_skills" : ["python", "kafka", "apache flink", "react(next.js)", "vue", "mysql", "redis"],
            "experience" : ["신입"],
            "preferential" : ["lac경험자", "데이터분석", "실시간스트림처리"]
        }
    ],
    "한국소니전자" : [
        {
            "title" : "설비 소프트웨어 개발",
            "required_skills" : ["c#", "visualbasic"],
            "experience" : ["신입"],
            "preferential" : ["컴퓨터/시스템공학", "jlpt n4이상"]
        }
    ],
    "NHN KCP" : [
        {
            "title" : "PG정산시스템 개발 및 운영",
            "required_skills" : ["java", "c", "oracle"],
            "experience" : ["신입", "경력2년"],
            "preferential" : ["대용량데이터처리"]
        }
    ],
    "테스트뱅크" : [
        {
            "title" : "Backend Developer",
            "required_skills" : ["mysql", "git"],
            "experience" : ["신입"],
            "preferential" : ["golang", "docker", "DB"]
        }
    ],
    "페이타랩" : [
        {
            "title" : "Android Developer",
            "required_skills" : ["kotlin", "java"],
            "experience" : ["신입"],
            "preferential" : ["AOS"]
        },
        {
            "title" : "Web Front End Developer",
            "required_skills" : ["typescript", "javascript", "html", "css", "react", "webpack", "git"],
            "experience" : ["신입"],
            "preferential" : ["ui", "ux"]
        }
    ],
    "이니텍" : [
        {
            "title" : "Backend Developer",
            "required_skills" : ["golang", "fiber", "sentry", "jira"],
            "experience" : ["경력6년이상"],
            "preferential" : ["대졸"]
        }
    ],
    "카카오페이증권" : [
        {
            "title" : "워크플랫폼 개발자",
            "required_skills" : ["java", "kotlin", "springboot", "mysql"],
            "experience" : ["경력3년이상"],
            "preferential" : ["docker", "kubernetes"]
        }
    ],
    "DB Int" : [
        {
            "title" : "SW Engineer",
            "required_skills" : ["java", "c"],
            "experience" : ["신입"],
            "preferential" : ["개발경험", "자격증"]
        },
        {
            "title" : "Infra Engineer",
            "required_skills" : ["네트워크"],
            "experience" : ["신입"],
            "preferential" : ["OSI 7 Layer", "TCP/IP", "Routing & Switching", "케이블링", "packet"]
        },
    ],
    "카카오엔터테인먼트" : [
        {
            "title" : "Android Developer",
            "required_skills" : ["java", "kotlin"],
            "experience" : ["경력4년이상"],
            "preferential" : ["RxJava", "RxKotlin", "coroutine", "MVVM", "MVI", "Epub", "ExoPlayer Custom"]
        },
        {
            "title" : "iOS Developer",
            "required_skills" : ["swift", "object-c", "git"],
            "experience" : ["경력10년이하"],
            "preferential" : ["xib", "storyboard", "autolayout"]
        }
    ],
    "카카오뱅크" : [
        {
            "title" : "Server Developer",
            "required_skills" : ["java", "springframework", "restAPI"],
            "experience" : ["경력3년이상"],
            "preferential" : ["kafka", "rabbitmq", "nosql"]
        }
    ],
    "sk쉴더스" : [
        {
            "title" : "빅데이터 엔진 개발",
            "required_skills" : ["scala", "spark", "hadoop", "hive"],
            "experience" : ["경력5년이상"],
            "preferential" : ["docker", "kubernetes", "대규모 실시간 스트리밍 데이터 처리"]
        }
    ],
    "파인더스" : [
        {
            "title" : "GPT 챗봇 개발자",
            "experience" : ["신입"],
            "required_skills" : ["pytorch", "python", "tensorflow", "json"],
            "preferential" : ["챗봇", "NLG"]
        }
    ],
    "이스트게임즈" : [
        {
            "title" : "Web Full Stack Developer",
            "experience" : ["신입"],
            "required_skills" : ["django", "react", "spring", "python", "java", "javascript"],
            "preferential" : ["typescript", "restAPI", "Graphql", "springframework", "AWS"]
        }
    ],
    "KT NexR" : [
        {
            "title" : "Front End Developer",
            "experience" : ["경력8년이상"],
            "required_skills" : ["javascript", "figma", "vue.js", "html5", "css", "javascript"],
            "preferential" : ["hadoop", "webpack", "rollup"]
        }
    ]
}

user_info = {}

user_info["name"] = input("이름을 입력하세요: ")
experience = input("경력 여부를 입력하세요(경력이 있는 경우 몇년차인지): ")
user_info["experience"] = experience
user_skills = input("기술 스택을 입력하세요 (쉼표로 구분): ").split(", ")
user_info["skills"] = set(user_skills)
user_info["desired_company"] = input("희망 기업을 입력하세요(없을 경우 'enter' 입력): ")
user_info["certification"] = input("취득한 자격증을 입력하세요 (없으면 'enter' 입력) : ").split(", ")

def experience_check(experience):
    if experience != '신입':
        experience_year = re.sub(r'[^0-9]', '', experience)
        user_info["experience_year"] = int(experience_year)
    else:
        user_info["experience_year"] = experience
    return user_info["experience_year"]


language_scores = {}
while True:
    language_ability = input("외국어 역량을 입력하세요 (종료하려면 'enter' 입력) : ")
    if language_ability == '':
        break

    score = input("점수를 입력하세요 : ")
    language_scores[language_ability] = int(score)

user_info["language_scores"] = set(language_scores)

project = {}
while True:
    project_name = input("활동한 프로젝트 이름을 입력하세요(종료하려면 'enter' 입력) : ")
    if project_name == '':
        break
    project_skill = input("프로젝트에 활용한 기술을 입력하세요 : ")
    project[project_name] = project_skill

user_info["projects"] = set(project)

activity = {}
while True:
    activity_name = input("참석한 대외활동 내역을 입력하세요(종료하려면 'enter' 입력) : ")
    if activity_name == '':
        break
    activity_subject = input("대외활동의 주제를 입력하세요 : ")
    activity[activity_name] = activity_subject

user_info["activities"] = set(activity)

user_desired_company = user_info['desired_company']


#기업 별 채용 공고와 사용자 정보를 비교하여 비율을 나누기 위한 변수 선언
required_score = 60 #기업의 필수 조건 비율을 나누기 위한 변수
preferential_score = 40 #기업의 우대 사항 비율을 나누기 위한 변수
comparison_score = 0 #기업의 채용 정보와 사용자의 정보를 비교한 뒤의 비율 변수
user_skills_list = []
company_required_list = []
company_preferential_list = []

# 사용자가 희망 기업을 선택하지 않은 경우 기업을 추천
def recommend_company_mentoring(name, companies, skills, experience):
    recommend_company = []
    print(f"'{name}'님의 입력 정보를 토대로 취업 가능한 기업을 추천합니다.")
    for company, postings in companies.items():
        for posting in postings:
            company_required_skills = set(posting.get('required_skills', []))
            if jaccard_similarity(skills, company_required_skills) >= 0.5:
                recommend_company.append(company)
    if recommend_company:
        print(f"현재 '{name}'님의 기술 스택이 부합하는 기업 리스트입니다:")
        print(recommend_company)
        for company in recommend_company:
            postings = companies[company]
            for posting in postings:
                company_preferential_skills = set(posting.get('preferential', []))
                if jaccard_similarity(skills, company_preferential_skills) >= 0.5:
                    print(f"추천 기업 '{company}'의 '{posting['title']}'의 취업률을 높이기 위해서 역량을 향상시켜보세요.")
                    print(f"{posting['preferential']}")
                    if 'recommand_project' in posting:
                        print("추천 프로젝트:")
                        for skill, project in posting['recommand_project'].items():
                            print(f"{skill}: {project}")
    else:
        print(f"현재 '{name}'님의 정보에 부합하는 기업이 없습니다.")

# 사용자가 입력한 희망 기업에 대한 매칭 후 비율 멘토링
def desired_company_mentoring(name, user_desired_company, companies, skills):
    if user_desired_company in companies:
        print(f"==========='{name}'님의 희망기업 '{user_desired_company}'의 채용 공고입니다.============")
        for company in companies[user_desired_company]:
            print(f"{user_desired_company}의 모집 분야는 {company['title']}입니다.")
            experience_check(company.get('experience', '신입'))
            company_required_skills = set(company.get('required_skills', []))
            if jaccard_similarity(skills, company_required_skills) >= 0.5:
                Qualifications = calc_similarity_percentage(skills, company_required_skills)
                print(f"필수 기술 요구사항에 {user_info['name']}님이 {company['title']}의 지원 자격에 {Qualifications}% 충족합니다.")
                company_preferential_skills = set(company.get('preferential', []))
                if jaccard_similarity(skills, company_preferential_skills) >= 0.5:
                    preferential = calc_similarity_percentage(skills, company_preferential_skills)
                    print(f"우대 사항에 {user_info['name']}님이 {company['title']}의 우대 사항에 {preferential}% 충족합니다.")
                    print(f"{user_desired_company}의 취업률을 높이기 위해서 역량을 향상시켜보세요.")
                    print(f"{company['preferential']}")
                    if 'recommand_project' in company:
                        print("추천 프로젝트:")
                        for skill, project in company['recommand_project'].items():
                            print(f"{skill}: {project}")
                else:
                    print(f"{user_desired_company}가 우대하는 부분에 대한 기술이 부족하거나 없습니다.")
                    print(f"{user_desired_company}의 취업률을 높이기 위해서 역량을 향상시켜보세요.")
                    print(f"{company['preferential']}")
                    if 'recommand_project' in company:
                        print("추천 프로젝트:")
                        for skill, project in company['recommand_project'].items():
                            print(f"{skill}: {project}")
                return
            else:
                print(f"{user_desired_company}의 채용 조건 중 필수 기술 요구사항에 충족하지 못합니다.")
                print(f"다음은 필수 기술 요구사항입니다: {company.get('required_skills', [])}")
        print(f"{user_desired_company}의 채용 조건 중 지원 자격에 충족하지 못합니다.")
        print(f"{companies[user_desired_company][0].get('required_skills', [])}에 대한 준비가 조금 더 필요합니다.")
    else:
        print("해당 기업의 채용공고가 없습니다.")




if user_desired_company == '':
    recommend_company_mentoring(user_info['name'], companies, user_info['skills'], user_info['experience'])
else:
    desired_company_mentoring(user_info['name'], user_info['desired_company'], companies, user_info['skills'])