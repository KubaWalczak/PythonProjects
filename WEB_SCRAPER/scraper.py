import requests
from bs4 import BeautifulSoup
import pprint


links = []
subtext = []
for i in range(1, 3):
    res = requests.get(f'https://news.ycombinator.com/news?p={i}')
    soup = BeautifulSoup(res.text, "html.parser")
    links1 = soup.select('.titlelink')
    subtext1 = soup.select('.subtext')
    links.append(links1)
    subtext.append(subtext1)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['points'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    dict = {}
    for linkss in links:  # have to unpack double list
        for idx, item in enumerate(linkss):
            title = linkss[idx].getText()
            href = linkss[idx].get('href', None)
            dict.update({title: href})
            for elem in subtext:  # have to unpack double list
                vote = elem[idx].select('.score')

                if vote:
                    points = int(vote[0].getText().replace(' points', ''))
                    if points > 99:
                        hn.append({'title': title, 'links': href, 'points': points})

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
