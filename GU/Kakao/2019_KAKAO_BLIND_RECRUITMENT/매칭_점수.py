from collections import defaultdict
import re

def solution(word, pages):
    count_info = defaultdict(int)
    link_info = defaultdict(list)
    match_score_info = defaultdict(float)
    word = word.lower()
    for page in pages:
        page = page.lower()
        
        # page이름 찾기
        page_name = re.search('<meta property="og:url" content="(\S+)"/>',page).group(1)
        
        # 단어 갯수 찾기
        count = 0
        for i in re.findall('[a-z]+', page):
            if i == word:
                count += 1
        # link 찾기
        link = re.findall('<a href="(\S+)">', page)
        
        # page 정보를 dict에 저장
        count_info[page_name] = count
        link_info[page_name] = link
    # 매치 점수 초기화
    for page in count_info:
        match_score_info[page] = count_info[page]
    #link 점수 계산
    for page in count_info:
        for link in link_info:
            if page in link_info[link]:
                match_score_info[page] += (count_info[link] / len(link_info[link]))
    max_score = -1
    min_idx = 0
    for idx, page in enumerate(match_score_info):
        if max_score < match_score_info[page]:
            min_idx = idx
            max_score = match_score_info[page]
    print(match_score_info)
    return min_idx

answer = solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
print(answer)