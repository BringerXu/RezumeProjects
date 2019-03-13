import urllib
import re
from collections import namedtuple
from bs4 import BeautifulSoup

user=namedtuple('user','last_name middle_name first_name')
#zhengyix=user('xu')
def format_receive(last_name,middle_name,first_name):
    return Last_name+' '+middle_name+' '+first_name

class USER():
    def __init__(self,part):
        self.input = part
        self.all = self._search()
        self.duplicate = len(self.all)
        self.name = self.collect(0)
        self.ucinetid = self.collect(1)
        self.level = self.collect(2)
        self.major = self.collect(3)

    def _search(self):
        format_part = urllib.urlencode([('basic_keywords',self.input)])
        search_format ='http://directory.uci.edu/?'+format_part+'&modifier=Starts+With&basic_submit=Search&checkbox_students=Students&form_type=basic_search'
        response = urllib.urlopen(search_format)
        soup = BeautifulSoup(response,"html.parser")
        try:
            result = soup.select(".resultData")[:4]
        except:
            raise
        else:
            if result == []:
                for href in soup.find_all('a'):
                    result.append(href['href'])
                subsearch=re.findall('\/index\.php\?uid=.*?basic_search',str(result))
                if subsearch == None:
                    return 'Your input do not exist'
                else:
                    sub_result=[]
                    for sub_url in subsearch:
                        format_subsearch='http://directory.uci.edu'+sub_url
                        sub_response=urllib.urlopen(format_subsearch)
                        sub_soup=BeautifulSoup(sub_response,'html.parser')
                        sub_result.append(sub_soup.select(".resultData")[:4])
                    return sub_result
            else:
                single_result=[result]
                return single_result
    
    def collect(self,index):
        result=[]
        for a in range(self.duplicate):
            result.append(self.all[a][index].text)
        return result

    def _printtest(self):
        print(self.all)
        print(self.duplicate)
        print(self.name)
        print(self.ucinetid)
        print(self.level)
        print(self.major)

zinanxu=USER('zinan xu')

zinanxu._printtest()