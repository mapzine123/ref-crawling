from running_task import running_task

# txt 파일을 통해서 data 가져옴
with open('static/crolling_data.txt', 'r') as file:
    data = file.read()

# 데이터 처리
running_task(data)