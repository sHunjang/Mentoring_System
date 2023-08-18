from flask import Flask, render_template, request
import re

app = Flask(__name__)

#기업 별 채용 조건
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

recommend_projects = {
    "웹 개발": {
        "프론트엔드": ["react", "angular", "vue.js"],
        "백엔드": ["node.js", "express.js", "django", "ruby on rails"],
        "추천 프로젝트": ["간단한 블로그 플랫폼", "할 일 관리 앱", "쇼핑 목록 관리 앱", "날씨 앱"]
    },
    "모바일 앱 개발": {
        "Android": ["java", "kotlin"],
        "iOS": ["swift", "objective-c"],
        "추천 프로젝트": ["간단한 메모 앱", "사진 공유 앱", "간단한 퍼즐 게임"]
    },
    "데이터 분석과 머신러닝": {
        "언어/도구": ["python", "jupyter notebook"],
        "추천 프로젝트": ["데이터 시각화", "간단한 분류기 구현", "선형 회귀 분석", "텍스트 분석"]
    },
    "인공지능과 딥러닝": {
        "언어/도구": ["python", "tensorflow", "pytorch"],
        "추천 프로젝트": ["이미지 분류기", "간단한 챗봇", "강화 학습을 이용한 게임 에이전트"]
    },
    "게임 개발": {
        "게임 엔진": ["unity"],
        "언어/도구": ["c#"],
        "추천 프로젝트": ["간단한 2D 플랫폼 게임", "간단한 퍼즐 게임", "아케이드 게임"]
    },
    "데이터베이스 관리 시스템": {
        "언어/도구": ["sql", "mysql", "postgresql"],
        "추천 프로젝트": ["간단한 블로그", "온라인 상점의 상품 관리 시스템", "학생 성적 관리 시스템"]
    },
    "블록체인": {
        "언어/도구": ["ethereum", "solidity"],
        "추천 프로젝트": ["간단한 스마트 계약 구현", "간단한 탈중앙화 애플리케이션(DApp)"]
    },
    "인터넷 of Things (IoT)": {
        "언어/도구": ["arduino", "raspberry pi", "c", "c++"],
        "추천 프로젝트": ["간단한 홈 오토메이션 시스템", "온도 및 습도 모니터링 시스템"]
    }
}

def count_matching_elements(list1, list2):
    return len(set(list1) & set(list2))

def process_user_input(user_form_data):
    user_info = {
        "name": user_form_data["name"],
        "experience": user_form_data["experience"],
        "skills": user_form_data["skills"].split(", "),
        "desired_company": user_form_data["desired_company"],
        "certification": user_form_data["certification"].split(", ")
    }
    
    language_scores = {}
    for language_ability, score in user_form_data.items():
        if language_ability.startswith("language_ability") and score:
            language_scores[language_ability] = score
    user_info["language_scores"] = language_scores
    
    project = {}
    for key, value in user_form_data.items():
        if key.startswith("project_name") and value:
            project_skill_key = f"project_skill_{key.split('_')[-1]}"
            project_skill = user_form_data.get(project_skill_key, "")
            if project_skill:
                project[value] = project_skill
    user_info["projects"] = project
    
    activity = {}
    for key, value in user_form_data.items():
        if key.startswith("activity_name") and value:
            activity_subject_key = f"activity_subject_{key.split('_')[-1]}"
            activity_subject = user_form_data.get(activity_subject_key, "")
            if activity_subject:
                activity[value] = activity_subject
    user_info["activities"] = activity
    
    result = {
        "user_info": user_info,
        "recommended_companies": recommended_companies(user_info),
        "desired_company_results": desired_company_results(user_info),
        "recommended_projects": recommended_projects(user_info)
    }
    return result

def compare_company_posting(company_posting, user_info):
    company_required_skills = set(company_posting.get('required_skills', []))
    company_preferential_skills = set(company_posting.get('preferential', []))
    
    matching_required_skills = count_matching_elements(user_info['skills'], company_required_skills)
    matching_preferential_skills = count_matching_elements(user_info['skills'], company_preferential_skills)
    
    required_score = (matching_required_skills / len(company_required_skills)) * 100
    preferential_score = (matching_preferential_skills / len(company_preferential_skills)) * 100
    
    preferential_skills = list(company_preferential_skills)
    
    return required_score, preferential_score, preferential_skills

def recommended_companies(user_info):
    recommended_companies = []
    for company, postings in companies.items():
        for posting in postings:
            required_score, preferential_score, preferential_skills = compare_company_posting(posting, user_info)
            if required_score >= 50:
                recommended_companies.append({
                    "company": company,
                    "required_score": required_score,
                    "preferential_score": preferential_score,
                    "preferential_skills": preferential_skills
                })
    recommended_companies.sort(key=lambda x: x['preferential_score'], reverse=True)
    return recommended_companies

def desired_company_results(user_info):
    desired_company = user_info["desired_company"]
    if desired_company in companies:
        desired_company_results = {}
        postings = companies[desired_company]
        for posting in postings:
            required_score, preferential_score, preferential_skills = compare_company_posting(posting, user_info)
            desired_company_results[posting["title"]] = {
            "required_score": required_score,
            "preferential_score": preferential_score,
            "preferential_skills": preferential_skills
        }

        return desired_company_results
    else :
        return None

def recommended_projects(user_info):
    user_skills = user_info['skills']
    recommended_projects_list = []

    for project_category, project_info in recommend_projects.items():
        category_skills = []

        for subcategory_skills in project_info.values():
            if isinstance(subcategory_skills, list):
                category_skills.extend(subcategory_skills)

        matching_skills = set(user_skills) & set(category_skills)
        if len(matching_skills) > 0:
            recommended_projects_list.append({
                "category": project_category,
                "matching_skills": list(matching_skills),
                "projects": project_info["추천 프로젝트"]
            })

    return recommended_projects_list


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_form_data = request.form.to_dict()
        result = process_user_input(user_form_data)
        if result is not None:
            return render_template("result.html", result=result)
        else:
            error_message = "결과를 찾을 수 없습니다."
            return render_template("index.html", error_message=error_message)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)