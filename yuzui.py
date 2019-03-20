import requests
from bs4 import BeautifulSoup
import  sys
"""
下载笔趣网小说余罪：我的刑侦笔记
本代码仅供学习交流使用，不用作任何商业用途
                                          BY：WorldZhang
"""
class downloadfiction(object):
    def __init__(self):
        self.target = "http://www.biqule.com/book_57141/"
        self.names = []
        self.url = []
        self.nums = 0

    """
    获得下载链接和章节名称
    """
    def downloadurl(self):
        req = requests.get(url=self.target)
        req.encoding = 'GB2312'
        html = req.text
        bf = BeautifulSoup(html)
        div = bf.find_all('div',class_='article-list')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a)
        for each in a:
            self.names.append(each.string)
            self.url.append(self.target+each.get('href'))

    """
    获得下载内容
    """
    def downloadcontent(self,target):
        req = requests.get(url=target)
        req.encoding = 'GB2312'
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div',id='content')
        texts = texts[0].text.replace('\xa0' * 4, '\n')
        return texts

    """
    保存成文件
    """
    def savefile(self,path,name,text):
        wirte_flag=True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')
            f.close()

if __name__ == '__main__':
    dl = downloadfiction()
    dl.downloadurl()
    print("余罪正在下载...")
    for i in range(dl.nums):
        dl.savefile('余罪.txt',dl.names[i],dl.downloadcontent(dl.url[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('《余罪》下载完成')




