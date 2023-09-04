import configparser
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from googletrans import Translator
import csv
from tqdm import tqdm
import os
from data_substring import remove_word
def running_task(data):
    # configparser 객체 생성 (properties 파일 읽기 목적)
    config = configparser.ConfigParser(allow_no_value=True)

    # properties 파일 읽기
    config.read("config.properties")

    # properties 값 가져오기
    word_length_min = int(config.get('word_config', 'word_length_min'))
    word_length_max = int(config.get('word_config', 'word_length_max'))
    result_derectory = config.get('directory_config', 'result_directory')

    # Natural Language Toolkit 라이브러리의 텍스트 토큰화에 사용되는 데이터 파일 다운
    nltk.download('punkt')

    data_count = int(input("몇개의 단어를 추출할까요 : "))
    print("저장될 파일명을 입력하세요")
    file_name = input("(확장자는 .csv입니다. 따로 입력하시지 않으셔도 됩니다.) :")
    print(f'저장 위치는 {result_derectory} 폴더입니다.')

    # configparser 객체 생성 (properties 파일 읽기 목적)
    config = configparser.ConfigParser(allow_no_value=True)

    # properties 파일 읽기
    config.read('config.properties')

    # properties 값 가져오기
    word_length_min = int(config.get('word_config', 'word_length_min'))
    word_length_max = int(config.get('word_config', 'word_length_max'))
    result_derectory = config.get('directory_config', 'result_directory')

    # data에서 특정 문자 패턴 제외
    data = remove_word(data)

    # 단어 하나하나를 토큰화
    tokens = word_tokenize(data)

    # 단어 중 5글자 이상인 것만 추출
    filtered_tokens = list(filter(lambda token: word_length_min <= len(token) <= word_length_max, tokens))

    # 단어 빈도 수 계산 (몇번 나왔는지)
    word_counts = Counter(filtered_tokens)

    # 상위 n개 단어만 추출
    top_words = word_counts.most_common(data_count)

    # 번역기
    translator = Translator()

    # 번역된 단어 배열
    word_and_trnaslated_text = []

    for word, count in tqdm(top_words):
        translated_text = translator.translate(word, src='en', dest='ko') # 영어를 한글로 번역
        word_and_trnaslated_text.append((count, word, translated_text.text)) # 나온 수, 영단어, 한글뜻 튜플

    # 만약 저장 디렉토리 없으면 만듬
    if not os.path.exists(result_derectory):
        os.mkdir(result_derectory)

    # 저장될 파일 경로와 이름
    file_path = os.path.join(result_derectory, file_name + ".csv")

    # CSV 파일로 저장
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['나온 수', '원본 단어', '번역된 텍스트'])

        for count, word, translated_text in word_and_trnaslated_text:
            csv_writer.writerow([count, word, translated_text])

    print("완료되었습니다.")

    print("저장된 폴더를 여시겠습니까?")
    isOpen = input("y 이외의 문자 입력시 폴더는 열리지 않습니다.")

    if isOpen.lower() == "y":
        os.startfile(result_derectory)