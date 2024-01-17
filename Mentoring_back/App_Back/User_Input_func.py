def user_data(user_input_data):
    user_data = {
        "name" : user_input_data['name'],
        "experience" : user_input_data['experience'],
        "skills" : user_input_data['skills'],
        "desired_company" : user_input_data['desired_company'],
        "certifications" : user_input_data['certifications']
    }
    
    language = {}
    for key, value in user_input_data.items():
        if key.startswith("language_name") and value:
            language_scores_key = f"language_scores_{key.split('_')[-1]}"
            language_scores = user_input_data.get(language_scores_key, "")
            if language_scores:
                language[value] = language_scores
    user_data["languages"] = language

    
    project = {}
    for key, value in user_input_data.items():
        if key.startswith("project_name") and value:
            project_skill_key = f"project_skill_{key.split('_')[-1]}"
            project_skill = user_input_data.get(project_skill_key, "")
            if project_skill:
                project[value] = project_skill
    user_data["projects"] = project
    
    activity = {}
    for key, value in user_input_data.items():
        if key.startswith("activity_name") and value:
            activity_subject_key = f"activity_subject_{key.split('_')[-1]}"
            activity_subject = user_input_data.get(activity_subject_key, "")
            if activity_subject:
                activity[value] = activity_subject
    user_data["activities"] = activity
    
    result = {
        "user_data": user_data
    }
    
    return result