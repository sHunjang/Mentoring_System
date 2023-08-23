from modules.company_recommendation_module import recommended_companies, desired_company_results, recommended_projects, recommended_skill_projects

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
        "recommended_projects": recommended_projects(user_info),
        "recommended_skill_projects" : recommended_skill_projects(user_info)
    }
    return result
