from flask import Flask, render_template, request
import User_Input_func


app = Flask(__name__)

# 사용자와 기업의 기술 스택을 set 형식으로 지정 후 비교하기 위한 함수
def count_matching_elements(list1, list2):
    return len(set(list1) & set(list2))



