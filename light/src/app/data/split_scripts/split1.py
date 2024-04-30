import re
import os
import json

# The table of contents
toc = '''1. 궁금하니 ? 알려줄게 , 차크라 …
2. 정신에도 프로그램 탑재가 필요해
3. 새 프로그램 탑재시 기존 프로그램과의 충돌
4. 자기 비난 프로그램을 속성으로 깨보자
5. 내 생각이 내 것이며 나는 옳다는 믿음을 깨보자
6. 버릴 것 좀 버리고 미련하게 살지 말자
7. 구도자를 위한 수행원리와 수행법 정리
8. 용서하기가 왜 그렇게 힘들까
9. 실전 ! 용서하기 1 편
10. 실전 ! 용서하기 2 편
11. 실전 ! 용서하기 3 편
12. 무의식 속에는 무엇이 있을까 1 편
13. 무의식 속에는 무엇이 있을까 2 편
14. 무의식 속에는 무엇이 있을까 ? 3 편
15. 무의식 속에는 무엇이 있을까 ? 4 편
16. 구도자가 피해야 할 지뢰밭
17. 무의식 속에는 무엇이 있을까 ? 5 편
18. 무의식 속에는 무엇이 있을까 ? 6 편
19. 실전 ! 용서하기 4 편
20. 실전 ! 용서하기 5 편
21. 실전 ! 용서하기 6 편 - 돈 용서하기
22. 실전 ! 용서하기 7 편 - 돈에게 용서받기
23. 실전 ! 용서하기 8 편 - 사랑받고 싶어하는 마음
24. 실전 ! 용서하기 9 편 - 어느 무서운 마을의 우물
25. 실전 ! 용서하기 10 편 - 원망하는 찌질이
26. 의심을 올리는 마음과 견성의 중요성
27. 상실감에 대하여
28. 시공간을 붕괴시키는 자
29. 지금의 세상이 어느날 갑자기 끝난다면
30. 끌어당김 1
31. 끌어당김 2
32. 수행법에 대해 반복되는 질문 답변
33. 이야니 - 가슴차크라 열기
34. 이야니 이야기 관련 추가 잡설 - 전생 등
35. 감정을 정면 돌파하기
36. 인성과 신성의 얕은 간격
37. 한국인 = 거지옷 입은 왕족
38. 교착상태 & 열등감 청산하기
39. 우울증 없애는 법
40. 음식에 대한 이야기
41. 기적수업 문구 모음
42. 생각의 노예
43. 자살충동 , 죽고싶은 마음
44. 아무 문제 없다
45. 솜사탕 나라 , 솜사탕 공장
46. 덕 좀 보려는 마음
47. 고마운 줄 모르는 마음
48 . 빠른 수행을 위한 조언
49. 미쳐버린 무의식과 특별한 관계 1
50. 미쳐버린 무의식과 특별한 관계 2
51. 미쳐버린 무의식과 특별한 관계 3
52. 가정폭력 , 때리고 맞는 관계
53. 우리 모두가 버린 작은 여자아이
54. 용자를 위한 속성 수행법
55. 애착 , 의존 , 사랑
56. 남자란 어떤 존재인가
57. 여자의 형상을 이용하여 공격하기
58. 도전, 용서실습
'''

# The document content
with open('../modified_text/part1_modified.txt', 'r', encoding='utf-8') as file:
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
os.makedirs('../data', exist_ok=True)
with open('../data/part1_data.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)