import requests
from bs4 import BeautifulSoup

# # Get method를 이용해서 해당 URL의 모든 HTML을 받아온다.
ndm_result = requests.get(
    "https://www.nature.com/search?journal=npjdigitalmed")

# 이렇게 받아온 텍스트는 너무 지저분한데. 우리가 보고자 하는건 HTML이니 형식에 맞게 분류해주자. Soup을 만들어준다.
# URL에서 HTML 데이터를 뽑아내온다고 생각하자.
ndm_soup = BeautifulSoup(ndm_result.text, 'html.parser')

# pagination이란 ol 안에 li들이 페이지들이다. 가져옵시다.
pagination = ndm_soup.find('ol', {'class', 'pagination'})

# Mutating sequence. 맨 앞쪽의 previous와 next를 빼버리자
pages = pagination.find_all('li')[1:-1]

# 마지막 페이지를 찾아오자. 정수를 String으로 가져올텐데, 이거를 정수로 바꾸어줍시다. int() 함수를 이용해
maxPage = int(pages[-1]['data-page'])
print(maxPage)
