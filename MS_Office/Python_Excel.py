# pip install openpyxl : Microsoft Office의 Excel 제품군에 대한 접근 라이브러리 설치
import openpyxl


"""
MySQL Database로 요청한 Query 명령어를 실행합니다.

in_Excel_file_Path: 데이터를 불러올 Excel 파일의 경로
in_Sheet_name: 시트 이름
"""
def open_return_Excel_file(in_Excel_file_Path, in_Sheet_name):
    # 불러온 Excel 파일을 읽기 전용으로 가져옵니다.
    select_Workbook = openpyxl.load_workbook(in_Excel_file_Path, data_only=True)
    # Excel 파일에 있는 시트를 가져옵니다.
    select_Worksheet = select_Workbook[in_Sheet_name]
    # 시트에 포함된 데이터를 되돌려줍니다.
    return select_Worksheet.rows
