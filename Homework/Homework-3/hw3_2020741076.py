from selenium import webdriver
from selenium.webdriver.common.by import By
import wordcloud
import matplotlib.pyplot as plt
driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B7%B9%EC%9E%A5%ED%8C%90+%EC%A7%B1%EA%B5%AC%EB%8A%94+%EB%AA%BB%EB%A7%90%EB%A0%A4%3A+%EC%88%98%EC%88%98%EA%BB%98%EB%81%BC%21+%EA%BD%83%ED%94%BC%EB%8A%94+%EC%B2%9C%ED%95%98%EB%96%A1%EC%9E%8E%ED%95%99%EA%B5%90+%ED%8F%89%EC%A0%90&oquery=%EA%B7%B9%EC%9E%A5%ED%8C%90+%EC%A7%B1%EA%B5%AC%EB%8A%94+%EB%AA%BB%EB%A7%90%EB%A0%A4%3A+%EC%88%98%EC%88%98%EA%BB%98%EB%81%BC%21+%EA%BD%83%ED%94%BC%EB%8A%94+%EC%B2%9C%ED%95%98%EB%96%A1%EC%9E%8E%ED%95%99%EA%B5%90+%ED%8F%89%EC%A0%90&tqi=h0RUSwprvxZssPP3oxNssssstZN-478940')
moviereview = driver.find_element(By.XPATH, r'//*[@id="main_pack"]').text #짱구 리뷰 가져오기
print(moviereview)
s_words=wordcloud.STOPWORDS.union({'바로재생 버튼','기존', '용의자중','6점', '지식iN', '블로그', '146명','선택해주세요','더보기','기본정보','29번째', '정보확인', '전 동영상', '버튼 문서', '내용', '나이별', '네이버TV NOW','그러던', '예', '관련문서','문서', '삭제됨', '평점', '동영상 바로재생','1점이 감소증가됨','내공', '저장소 네이버TV'})


image=wordcloud.WordCloud(font_path='C:/WINDOWS/FONTS/MALGUNSL.TTF',width=1000, height=700).generate(moviereview)


plt.figure(figsize=(40,30))
plt.imshow(image)
plt.show()

