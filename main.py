from ndm import extract_ndm, extract_ndm_articles

# 페이지 숫자를 가져오는 함수를 만들었습니다.
max_extract_page = extract_ndm()

# 다음으로 할 일은 페이지 갯수만큼 돌아보면서 각 페이지의 요소들을 가져오는 겁니다. 그러니 ndm에 새로운 function을 만들어줍니다.
extract_ndm_articles(max_extract_page)
# 이렇게 하면 각 페이지들의 URL을 가져올 수 있겠죠?

