import requests
from lxml import html
def getPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
    }
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        return res.content.decode('utf-8')
    else:
        return None


if __name__ == '__main__':
    for i in range(1,53):
        url =f'https://m.tvmao.com/drama/VjNsWg==/episode/{(i-1)//3}-{i}'
        htmltetxt = getPage(url)
        etree = html.etree
        page = etree.HTML(htmltetxt)
        items = page.xpath('//div[@class="episode"]')
        for i in items:
            text = i.xpath('.//p/text()')
            with open('xianjian.txt.','a',encoding='utf-8') as f:
                f.write(text[0])
                f.write('\n')