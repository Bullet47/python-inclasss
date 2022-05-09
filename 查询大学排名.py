from bs4 import BeautifulSoup
import requests
import csv


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"


def writeUlistfile(ulist):
    with open('Ulist.csv', 'w', newline='') as fout:
        writer = csv.writer(fout)
        for row in ulist:
            writer.writerow(row)


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    data = soup.find('div', attrs={'id': 'mainbox'}).find('table').find('tbody').find_all('tr')
    print(data)
    for tr in data:
        lst = []
        for td in tr.find_all('td'):
            print(td.string)
            lst.append(td.string)
        ulist.append(lst)
    del ulist[0]
    return ulist


def printUnivList(ulist, num):
    '''
    tplt="{0:>10}\t{1:{3}<10}\t{2:^10}"
    #print(tplt.format("排名","学校名称","地点",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
    '''
    for i in range(num):
        u = ulist[i]
        a = '' * (8 - len(u[0].encode('GBK'))) + u[0]
        b = u[1] + '' * (20 - len(u[1].encode('GBK')))
        c = u[2]
        print(a, b, c, sep='')


if __name__ == '__main__':
    url = 'https://www.cnur.com/rankings-2021'
    html = getHTMLText(url)
    uinfo = []
    uinfo = fillUnivList(uinfo, html)
    writeUlistfile(uinfo)
    #fillUnivList(uinfo, 20)
