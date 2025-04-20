from data_loader import load_financial_data
from analyzer import analyze_ratios_and_changes
from reporter import generate_report
from pprint import pprint
import os

# 기본 데이터 디렉토리
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# 1. 데이터 불러오기
financial_data = load_financial_data(DATA_DIR)

# 2. 분석 수행
analysis_result = analyze_ratios_and_changes(financial_data)
pprint(analysis_result)

# 3. Gemini API를 이용한 요약 보고서 생성
generate_report(analysis_result, company_name="A회사")
