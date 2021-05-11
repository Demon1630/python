import re
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}



def get_joke(url):

    r = requests.get(url=url,headers=headers)
    # print(r.text)
    # r.encoding(UTF-8, ignore)
    # r.encoding = 'utf-8'
    # r.encoding = 'utf-8'


    #获取用户ID   #需要加上？，强制一次，不然会匹配到开头的 <h2>和页面结尾的</h2>
    ids = re.findall('<h2>\n(.*?)\n</h2>',r.text,re.S)

    #获取用户级别
    levals = re.findall('<div class="articleGender.*?">(\d+?)</div>',r.text,re.S)

    #获取性别
    sexs = re.findall('class="articleGender(.*?)">.*?</div>',r.text,re.S)

    #获取段子内容
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',r.text,re.S)

    joke_list = []
    for id,leval,sex,content in zip(ids,levals,sexs,contents):

        info = {'id':id,'leval':leval,'sex':sex,'content':content,}
        # print(info)

        joke_list.append(info)

    # print(len(joke_list))


    for joke in joke_list:
        f = open('C:\\Users\\Administrator\\Desktop\\糗事百科.txt', 'a+',encoding='utf-8')  # 写入文件时后面要加上 encoding = 'utf-8',否则会报错

        try:
            f.write('\n\n'+'用户名：'+'\t'+joke['id']+'\n')
            f.write('用户级别：'+joke['leval']+'\n')
            f.write('用户性别：'+joke['sex']+'\n')

            a = joke['content'].replace('<br/>','\n').replace('<br>','\n').replace('\n','')

            f.write(a)
            f.close()
        except:
            pass

#生成前三十页url
# url_list = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,31)]
url_list = ['https://www.qiushibaike.com/text/page/'+str(i)+'/' for i in range(1,31)]

for url in url_list:

    get_joke(url)
    print(f'下载完成页面{url}')