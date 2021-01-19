# pip install pandas
import pandas


"""
Pandas를 통해 Excel 파일을 불러옵니다. (통합하여 편하게 Excel로 통합)

in_file_path: 불러올 Excel 파일 관련 자료 경로
"""
def pandas_return_Excel_file(in_Excel_file_path):
    _df_contents = pandas.read_csv(in_Excel_file_path, header=None, encoding='CP949')
    return _df_contents


"""
가져온 DateFrame 자료에서 특정 조건이 맞는 데이터만 List로 저장하고 되돌려줍니다.

in_Date_frame: pandas_return_Excel_file()에서 불러온 자료
in_Search_date: 가져온 자료에서 별도의 리스트로 분류할 데이터
in_Search_date_Location: 데이터가 존재하는 위치(int, 0부터 순서대로)
"""
def pandas_return_Search_date_list_Excel_file(in_Date_frame, in_Search_date, in_Search_date_Location):
    select_date_list = in_Date_frame[in_Search_date_Location] == in_Search_date
    return in_Date_frame[select_date_list]
