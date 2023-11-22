from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")

# 웹 드라이버 설치 및 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL 입력 받기
url = input("워드 클라우드를 생성할 웹사이트의 URL을 입력하세요: ")
driver.get(url)

# 페이지에서 본문 텍스트 가져오기 
conan_data = driver.find_element(By.XPATH, '//*[@id="JqFElvLbD"]/div[2]/div/div/div/div/div/div[1]/div[7]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[11]/div/div/div/div/div[1]/div/div[23]/div').text  

# 필요없는 단어들 목록 만들기
s_words = wordcloud.STOPWORDS.union({'네이버','카페','지부','온리전','공식','사이트는','셈','티켓값이','교보문고','감청의 권'})

# 워드 클라우드 생성
output_filename = "conan_data_sherlock.png"
sherlock_data = Image.open("/Users/kimsolbi/Desktop/AIP/hw3/sherlock.png")
sherlock_mask = np.array(sherlock_data)

wordcloud_instance = wordcloud.WordCloud(
    background_color="white",
    max_words=2000,
    mask=sherlock_mask,
    stopwords=s_words,
    min_font_size=10,
    max_font_size=100,
    font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf',
    width=1000, 
    height=700
).generate(conan_data)

wordcloud_instance.to_file(output_filename)

plt.figure(figsize=(40,30))
plt.imshow(wordcloud_instance, interpolation="bilinear")
plt.axis("off")
plt.show()

driver.quit()
