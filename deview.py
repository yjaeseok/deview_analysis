import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    skip_count = 0
    schedule = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

    print(str(max_pages))
    page = 1
    while page <= max_pages:
        print("request page ", page)
        url = "https://deview.kr/2017/pick/" + str(page)
        source_code = requests.get(url)
        soup = BeautifulSoup(source_code.text, 'lxml')
        
        # day1 정보 입력 여부 확인
        day1 = False
        h3s = soup.find_all('h3')
        for h3 in h3s:
            h3contents = str(h3.contents[0])
            if h3contents.startswith("DAY 1"):
                day1 = True

        # day1 이 입력 되어 있다면
        if day1:
            track_info_list = soup.find_all('dd', class_='track_info')
            for idx, track_info in enumerate(track_info_list):
                track_no_object = track_info.find('p', class_='track_no')
                if track_no_object is None:
                    continue
                track_no = str(track_no_object.contents[0])

                # 키노트 제외
                if 'ALL TRACKS' == track_no:
                    continue
                # Day 2 제외
                if idx >= 6:
                    continue

                schedule[idx][int(track_no[5]) - 1] = schedule[idx][int(track_no[5]) - 1] + 1
        else:
            skip_count = skip_count + 1

        page = page + 1

    print(str(schedule))
    print("skip_count", skip_count)


if __name__ == "__main__":
    spider(5121)
