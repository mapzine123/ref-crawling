# ref-crolling
URL이나 TXT 파일에서 영어 단어의 빈도 수를 파악해 해당 텍스트에서 많이 나온 영단어를 오름차순으로 번역해 csv 파일으로 변환해주는 프로그램 입니다.

# 파일 구조
ref-crolling
  ㄴ result 폴더 : 결과물이 저장될 폴더입니다.
  ㄴ static 폴더
      ㄴ `crolling_data.txt` : 번역하고 싶은 영어 본문을 여기에 복사하고 저장한 후 crolling_from_txt 파일을 실행합니다.
      ㄴ `remove_patterns.txt` : 제외하고싶은 단어 모음입니다. \b\d+\b는 숫자로만 된 문자를 무시합니다.
 
# 설정 변경
`config.properties`
  ㄴ `word_length_min` : 번역할 단어의 최소 길이
  ㄴ `word_length_max` : 번역할 단어의 최대 길이
  ㄴ `result_directory` : 번역된 파일이 저장될 폴더 (사용자 설정시 절대 경로로 할 것) ex) D:\DEV

# 의존성
`configparser` = 6.0.0
`requests` = 2.31.0
`beautifulsoup4` = 4.12.2
`nltk`=3.8.1
`googletrans` = 4.0.0-rc1
`tqdm` = 4.66.1

# 의존성 설치 (필요 시 터미널에 복사 / 붙여넣기)
pip install configparser==6.0.0 requests==2.31.0 beautifulsoup4==4.12.2 nltk==3.8.1 googletrans==4.0.0-rc1 tqdm==4.66.1

