from flask import Flask, render_template, request
from DATA.posting_data import get_companies
from DATA.skill_list import get_skill_stack
from DATA.recommend_projects import get_recommended_projects
from modules.utils import count_matching_elements
from modules.company_recommendation_module import compare_company_posting, recommended_companies, desired_company_results, recommended_projects, recommended_skill_projects, calculate_matching_score
from modules.user_info_module import process_user_input

app = Flask(__name__)


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

@app.route("/result_detail/<company_name>/<job_title>", methods=["GET"])
def result_detail(company_name, job_title):
    companies_data = get_companies()  # get_companies() 함수를 호출하여 회사 채용 공고 데이터 가져옴

    if company_name in companies_data:
        company_postings = companies_data[company_name]
        target_posting = None
        for posting in company_postings:
            if posting["title"] == job_title:
                target_posting = posting
                break

        if target_posting:
            result_info = {
                "company_name": company_name,
                "job_title": job_title,
                "required_skills": target_posting["required_skills"],
                "preferential_skills": target_posting["preferential"]
            }
            return render_template("result_detail.html", **result_info)
        else:
            error_message = "해당 회사 및 직무 정보를 찾을 수 없습니다."
            return render_template("error.html", error_message=error_message)
    else:
        error_message = "해당 회사 정보를 찾을 수 없습니다."
        return render_template("error.html", error_message=error_message)



if __name__ == '__main__':
    app.run(debug=True)