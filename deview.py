import requests, random
from bs4 import BeautifulSoup


def spider(max_pages):
    skipCount = 0
    schedule = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

    print(str(max_pages))
    page = 1
    while page <= max_pages:
    #if page <= max_pages:
    #    page = 3890
        print("request page ", page)
        url = "https://deview.kr/2017/pick/" + str(page)
        sourceCode = requests.get(url)
        soup = BeautifulSoup(sourceCode.text, 'lxml')

        day1 = False

        h3s = soup.find_all('h3')
        for h3 in h3s:
            h3contents = str(h3.contents[0])
            if h3contents.startswith("DAY 1"):
                day1 = True

        if day1:
            track_infos = soup.find_all('dd', class_='track_info')
            print("length : ", len(track_infos))

            for idx, track_info in enumerate(track_infos):
                track_no_object = track_info.find('p', class_='track_no')
                if track_no_object is None:
                    continue
                track_no = str(track_no_object.contents[0])
                if 'ALL TRACKS' == track_no:
                    continue
                if idx >= 6:
                    continue

                schedule[idx][int(track_no[5]) - 1] = schedule[idx][int(track_no[5]) - 1] + 1
        else:
            skipCount = skipCount + 1

        page = page + 1

    print(str(schedule))
    print("skipCount", skipCount)

if __name__ == "__main__":
    spider(5121)

    #random.randrange(1, 5121))
