import json

python_dict = {"name": "Lily", "age": 20, "city": "Busan", "isLogin": True}
# dumps(): 딕셔너리를 JSON 문자열로 변환
json_str = json.dumps(python_dict)
print(json_str)
# python_dict: 파이썬의 딕셔너리 객체
# json_str: JSON 형식의 텍스트 데이터


# loads(): JSON 문자열을 Python 객체로 변환
json_obj = json.loads(json_str)
print(json_obj)
print(json_obj["name"])