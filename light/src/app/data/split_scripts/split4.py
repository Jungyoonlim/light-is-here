import re
import os
import json

# The table of contents for pdf2 
toc = '''
1. [기갤] [22.01.23] 영적 금렵구
2. [기갤] [22.04.25] 금렵구, 포털, 매트릭스 2
3. [기갤] [22.07.09] 금렵구, 포털, 매트릭스 3
4. [기갤] [22.07.09] 금렵구, 포털, 매트릭스 4
5. [기갤] [22.07.29] 금렵구, 포털, 매트릭스 5
6. 드라마 세션장면 최초공개 2
7. 드라마 세션장면 최초공개 3
8. 0824 기텍강독 - 기적수업의 유일한 주제 : <권위 문제> 1
9. 0824 기텍강독 - 기적수업의 유일한 주제 : <권위 문제> 2
10. 0824 기텍강독 - 기적수업의 유일한 주제 : <권위 문제> 3
11. 기텍강독 0727 바다와 물풍선
12. 기텍강독 0727 바다와 물풍선 2
13. 기텍강독 0727 바다와 물풍선 3
14. 무언가가 환상임을 입증하는 방법은
15. 뉴비들을 위한 공지 또 올립니다. 필독해주세요
16. 감정 청산 수행기 남기실 적에 조심하셔야 할 부분 - 필독해주세요 
17. 너 이래도 그게 너한테 소중하냐?
18. 1029 가슴을 열어라 - 의식교류의 중요성 1
19. 1029 가슴을 열어라 - 의식교류의 중요성 2
20. 1029 가슴을 열어라 - 의식교류의 중요성 3
21. 다 집어치고 도망가고 싶을 때
22. 육체, 감정체, 멘탈체, 에테르체
23. [돌고래] 0817 기텍강독 - 참수행의 시작과 질의응답 1
24. [돌고래] 0817 기텍강독 - 참수행의 시작과 질의응답 2
25. [돌고래] 0817 기텍강독: 참수행의 시작과 질의응답 3                        
26. [카페] 1111 갓수저 챌린지 제안
27. [돌고래] 0831 기텍강독 - 시크릿, 카르마 1
28. [돌고래] 0831 기텍강독 - 시크릿, 카르마 2
29. [돌고래] 0831 기텍강독 - 시크릿, 카르마 3
30. [카페]영혼의 파편화와 트라우마 청산
31. [세션] 귀한 사람은 귀한 삶을 사는 겁니다
32.기텍강독 1012-1 생각은 내 것이 아니다
33. 기텍강독 1012-2 모든 것이 다 옳다 vs모든것을 다 용서한다
34. 기텍강독 1005-1 왜 자기 마음을 마음대로 못쓸까
35. 기텍강독 1005-2 그래도 싫은 일을 어떻게 할까
36. 뭐를 문제로 여기는 마음이 문제라면 문제
37. 사람이 힘들 수 있다.
38. 누군가의 생각과 노력과 마음씀이 엄청 들어가있는거야 물건 하나가
39. 0203 세션엿보기 - <하겠다> 마음먹으면, 하기싫은 마음이 안올라오는게 정상입니다 
40. 0210 세션엿보기 - 빛과 우산
41. 0213 세션엿보기 - 아 나는 사랑스럽구나
42. 기텍강독 20221228 기적수업의 핵심개념 <희생> 1
43. 기텍강독 20221228 기적수업의 핵심개념 <희생> 2
44. 0224 세션엿보기 - 이보시게 페라리엔 고급유를 넣는거라네
45. 0224 세션엿보기 - 몸은 신성으로 가는 통로입니다
46. 스타워게즈와 구기종목
47. [세션] 0325 세션엿보기 - 내 귀가 모기 귀로구나
'''


# The document content
with open('../modified_text/part4_modified.txt', 'r', encoding='utf-8') as file:
    document_content = file.read()

# Extract the titles from the table of contents
titles = re.findall(r'\d+\.\s*(.*)', toc)

# Create a list to store the JSON data
json_data = []

# Find the content for each title in the document
for title in titles:
    # Create a regular expression pattern to match the title
    pattern = re.escape(title)
    
    # Find the index of the title in the document content
    title_index = document_content.find(title)
    
    if title_index != -1:
        # Find the index of the next title or the end of the document
        next_title_index = len(document_content)
        for next_title in titles[titles.index(title) + 1:]:
            next_index = document_content.find(next_title, title_index + len(title))
            if next_index != -1:
                next_title_index = min(next_title_index, next_index)
        
        # Extract the content between the current title and the next title
        content = document_content[title_index + len(title):next_title_index].strip()
        
        # Remove leading and trailing newline characters from the content
        content = content.strip('\n')
        json_data.append({'title': title, 'content': content})
    else:
        print(f"Content not found for title: {title}")

# Write the JSON data to a file in the data directory
with open('../json_data/part4_data.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)