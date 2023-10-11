from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import wordcloud
import matplotlib.pyplot as plt
from selenium.webdriver.common.by import By


# 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 헤드리스 모드 설정 / 크롬 창 따로 안 띄우도록 설정

# 웹 드라이버 설치 및 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL 입력 받기
url = input("워드 클라우드를 생성할 웹사이트의 URL을 입력하세요: ")
driver.get(url)

# 페이지에서 본문 텍스트 가져오기 
conan_data = driver.find_element(By.XPATH, '//*[@id="JqFElvLbD"]/div[2]/div/div/div/div/div/div/div[1]/div[5]/div/div[3]/div/div/div/div/div/div/div/div/div[10]/div/div/div/div/div/div/div[1]/div/div[23]/div').text

# 필요없는 단어들 목록 만들기
s_words = wordcloud.STOPWORDS.union({'네이버','카페','지부','온리전','공식','사이트는','셈','티켓값이','교보문고','감청의 권'})

# 워드 클라우드 생성
image = wordcloud.WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', width=1000, height=700, stopwords=s_words).generate(conan_data)

plt.figure(figsize=(40,30))
plt.imshow(image)
plt.show()

driver.quit()
