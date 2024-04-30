import re
import os
import json

# The table of contents for pdf2 
toc = '''
1.행복으로 가는 길
2.권위 문제와 가족 청산
3.재미로 보는 갤 운영 이모저모
4.가짜 영성 가르침, 스승 진단해 드림
5.소중한 것을 살해해서 버렸다는 착각
6. 실전! 여자에 대한 증오, 열등감 청산
7. 너에 대한 하나님의 생각
8. 하나님은 내가 하나님과 함께 생각하는 마음이시다 
9. 가족이 나를 원망할 때
10. 감정청산과 가혹한 마음
11. 참수행의 어려움
12. 갤 사용 설명서 등
13. 우리 회사 최종 보스는 누구일까?
14. 에너지 기생충 / 뱀파이어 / 악연의 줄을 잘라보자 
15. 꿈이나 현실이나 똑같은 꿈입니다 1
16. 꿈이나 현실이나 똑같은 꿈입니다 2
'''


# The document content
with open('../modified_text/part3_modified.txt', 'r', encoding='utf-8') as file:
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
with open('../json_data/part3_data.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)