from modules.posting_data import companies
from modules.utils import count_matching_elements
from modules.recommend_projects import recommend_projects
from modules.skill_list import skill_stack

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
                    "title" : posting["title"],
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

    for project_category, project_list in recommend_projects.items():
        for project_info in project_list:
            project_skills = project_info['기술']

            for subcategory_skills in project_info.values():
                if isinstance(subcategory_skills, list):
                    project_skills.extend(subcategory_skills)

            unmatched_skills = set(project_skills) - set(user_skills) 
            if len(unmatched_skills) > 0:
                recommended_projects_list.append({
                    "category": project_category,
                    "unmatched_skills": list(unmatched_skills),
                    "projects": project_info['내용']
                })

    return recommended_projects_list

def recommended_skill_projects(user_info):
    user_skills = user_info["skills"]
    recommended_projects = {}
    
    for skill, projects in recommend_projects.items():
        if any(s not in user_skills for s in skill_stack.get(skill, [])):
            recommended_projects[skill] = projects
    
    return recommended_projects
