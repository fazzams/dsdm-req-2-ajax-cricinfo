import requests
import json

with open('topstats.csv', 'w') as f:
    for i in range(1,3):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?genre=706;;page={i}'
        res = requests.get(url)
        data = json.loads(res.text)

        for news in data:
            f.write(news['headline'])
            f.write('\n')

