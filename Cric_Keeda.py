import bs4, requests, os, sys

def Start():
    url = 'http://www.cricbuzz.com/'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    sel = soup.select('a[tracklabel="Match"]')
    for s in sel:
        print(s.text)
        print()


if __name__=='__main__':
    print("...................Live Cricket Score.....................")
    print()
    Start()