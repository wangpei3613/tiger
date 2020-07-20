import requests
from lxml import html
def getPage(url):
    headers = {
        "Host": "m.qcc.com",
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36'

    }
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        return res.content.decode('utf-8')
    else:
        return None
#输入查询内容获得的公司字典
def getList(url):
    chtmlText = getPage(url)
    etree = html.etree
    cpage = etree.HTML(chtmlText)
    citems = cpage.xpath('//a[@class="a-decoration"]')
    company_dict = dict()

    for i in citems:
        print(i.xpath('./@href'))
        item = i.xpath('./div/div/div[@class="list-item-name"]//text()')
        company_dict["".join(item).strip()] = i.xpath('./@href')
        print("".join(item).strip())
    return company_dict;

#输入选择的公司查询出改公司的具体内容,写入文件
def getBaseInfo(url,flag):
    dhtmlText = getPage(url)
    etree = html.etree
    dpage = etree.HTML(dhtmlText)
    companyname = dpage.xpath('//div[@class="company-name"]/text()')
    operator = dpage.xpath('//a[contains(@class,"oper")]//text()')
    print("公司名称      "+"".join(companyname).strip())
    print("法定代表人    " + "".join(operator).strip())
    return;

if __name__ == '__main__':
    while True:
        company = input("请输入查询内容\n");
        curl = f'https://m.qcc.com/search?key={company}'
        cdict = getList(curl)
        flag = input("请输入具体查询内容\n");
        durl = f'https://m.qcc.com{cdict[flag][0]}'
        getBaseInfo(durl,flag)