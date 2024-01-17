import pandas as pd
import os, re

companies = {
    "SK": [
        {
            "title": "Application Engineering",
            "required_skills": ["java", "springboot", "sql"],
            "preferential": ["프로그래밍 언어 및 DB 활용", "MSA", "AWS Resource", "Native"]
        },
        {
            "title": "SoftWare Engineering",
            "required_skills": ["java", "springboot"],
            "preferential": ["금융", "Native", "경제학"]
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
            "preferential": ["SDK"]
        }
    ],
    "Coupang": [
        {
            "title": "Senior, Backend engineer (SCM)",
            "required_skills": ["java", "python", "spring"],
            "experience": "경력5년이상",
            "preferential": ["springboot", "컴퓨터과학석사"]
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
            "preferential" : ["elasticsearch", "python", "hadoop"],
        }
    ],
    "삼진" : [
        {
            "title" : "Embedded SW Developer",
            "required_skills" : ["c", "c++"],
            "experience" : "신입",
            "preferential" : ["임베디드SW"]
        }
    ],
    "신세계아이앤씨" : [
        {
            "title" : "SW Develop & Operation ",
            "required_skills" : ["java", "c", "c++", "python", "mysql", "R"],
            "experience" : "경력3년이상",
            "preferential" : ["AI챗봇", "doker", "kubernetes"]
        }
    ],
    "미디어로그" : [
        {
            "title" : "SW Developer",
            "required_skills" : ["java"],
            "experience" : "신입",
            "preferential" : [""]
        }
    ],
    "현대이지웰" : [
        {
            "title" : "SW Developer",
            "required_skills" : ["java", "jsp", "jquery", "spring", "strutus2", "mybatis"],
            "experience" : ["신입", "경력2년이상"],
            "preferential" : [""]
        }
    ],
    "비지에프리테일" : [
        {
            "title" : "하계 채용연계형 인턴",
            "required_skills" : ["java", "jsp", "javascript", "nexacro", "html5"],
            "experience" : ["신입"],
            "preferential" : ["", "학점3점이상"]
        }
    ],
    "넥슨" : [
        {
            "title" : "탐지응용팀 백엔드 개발자",
            "required_skills" : ["python", "kafka", "apache flink", "react(next.js)", "vue", "mysql", "redis"],
            "experience" : ["신입"],
            "preferential" : ["lac", "데이터분석", "실시간스트림처리"]
        }
    ],
    "한국소니전자" : [
        {
            "title" : "설비 소프트웨어 개발",
            "required_skills" : ["c#", "visualbasic"],
            "experience" : ["신입"],
            "preferential" : ["컴퓨터공학", "시스템공학", "jlpt n4이상"]
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
            "preferential" : ["golang", "docker", "db"]
        }
    ],
    "페이타랩" : [
        {
            "title" : "Android Developer",
            "required_skills" : ["kotlin", "java"],
            "experience" : ["신입"],
            "preferential" : ["aos"]
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
            "preferential" : [""]
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
            "preferential" : [""]
        },
        {
            "title" : "Infra Engineer",
            "required_skills" : ["네트워크"],
            "experience" : ["신입"],
            "preferential" : ["osi7layer", "tcp/ip", "routing&switching", "케이블링", "packet"]
        },
    ],
    "카카오엔터테인먼트" : [
        {
            "title" : "Android Developer",
            "required_skills" : ["java", "kotlin"],
            "experience" : ["경력4년이상"],
            "preferential" : ["rxjava", "rxkotlin", "coroutine", "mvvm", "mvi", "epub", "exoplayercustom"]
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
            "preferential" : ["챗봇", "nlg"]
        }
    ],
    "이스트게임즈" : [
        {
            "title" : "Web Full Stack Developer",
            "experience" : ["신입"],
            "required_skills" : ["django", "react", "spring", "python", "java", "javascript"],
            "preferential" : ["typescript", "rest", "graphql", "springframework", "aws"]
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

def get_companies():
    return companies
