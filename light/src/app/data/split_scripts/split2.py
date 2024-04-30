import re
import os
import json

# The table of contents for pdf2 
toc = '''
1.미친마음(병신) vs.바른마음(정신)
2.잡혀 죽을까봐 무서울 때 화가 납니다
3.신성을 되찾겠다는 요구
4.죽음의 공포, 청산해보자 
5.의식집중과 한마음
6.하나님 마음이 여러분께 원하는 것 
7.감정파헤쳐용서할때조심할점
8.가위눌림 답변
9.파동체 매트릭스의 구성
10.세상이라는 시체 한 구
11.하나님 멱살 잡기
12.솜사탕, 특별함, 권위문제
13.솜사탕 집단 역학
14.잡썰 + 영적에고
15.실체가 없지만 끼어들어서 내가 했다고 주장하는 에고 
16.없는 것을 있는 것으로 만들려는 욕구
17.감정이 전보다 잘 올라오지 않는다?
18.한의 저장고
19.바디스캔 해보자 -(1)
20.실전! 권위문제 청산해보자
21.아무것도 해야 할 것이 없다 
22.그리스도의식의 각성상태-(1) 
23.그리스도의식의 각성상태-(2) 
24.그리스도의식의 각성상태-(3) 
25.그리스도의식의 각성상태-(4) 
26.진지한 구도자가 가져야 할 자세 
27.성령은 우리를 어떻게 볼까요 
28.성령은 세상을 어떻게 볼까요
29.성행위와 죄책감
30.성, 섹스, 구원자게임-(1) 
31.갤을 위한 정화 기도
32. 죄책감을 느끼지 않겠다는 결정 
33.올바른 수행의 척도
34.독재자, 폭군 청산을 위한 기도 
35.뭐든지 내가 한 건 잘했다 
36.잠, 몸변화, 식습관 등
'''


# The document content
with open('../modified_text/part2_modified.txt', 'r', encoding='utf-8') as file:
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
with open('../json_data/part2_data.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)