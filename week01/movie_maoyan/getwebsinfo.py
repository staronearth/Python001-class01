import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
class getwebsinfo:
    def __init__(self):
        super().__init__()
    def getweb(self,weburl):
        #获取网页的信息
        headers={}
        headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        headers['cookie']='__mta=176026525.1593240535203.1593240644015.1593242949907.4; _csrf=4be9262c230ad84d682a87f945edd67894d4f268bb1f4808061e8ccd819be6fe; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593242949; uuid_n_v=v1; mojo-uuid=6bfda18a9a66c605f9b2b47d55f19f88; uuid=3A5CBD10B84211EAB11C23537EB4C64B0436B67683E64E3E96EC3DDD88A54825; _lxsdk_cuid=172f489361ac7-0949cdbf8424cf-71415a3a-100200-172f489361bc8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593240533,1593240614,1593240644; mojo-session-id={"id":"7447e72e22ceb8210f0f69ec9e5ac740","time":1593242948858}; mojo-trace-id=1; _lxsdk=3A5CBD10B84211EAB11C23537EB4C64B0436B67683E64E3E96EC3DDD88A54825; _lxsdk_s=172f4adfb23-4b5-d8c-909%7C52130765%7C3; lt=PBR3YhVtVGfpnKi1cHX4mj96wdAAAAAA5woAAFyoV39r4Ygq_45WqHPcvscdAN-yKTtnx7ChK7Tb_wgijpDrIVi63lr6zRjggUfZ4Q; lt.sig=TQg_-RbzplQzNXESUQO73Nh-iNo'
        response = requests.get(weburl,headers=headers)
        return response
    def responseurlinfo(self,response):


        bs_info = bs(response.text,'html.parser')

        film_list=[]
        for tags in bs_info.find_all('div' , attrs={'class':'channel-detail movie-item-title'}):
            for atag in tags.find_all('a',):
                film_list.append('https://maoyan.com'+atag.get('href'))
        return film_list

    def getfilminfo(self,filmurl):
        responses = self.getweb(filmurl)
        selector=lxml.etree.HTML(responses.text)

        film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
        film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[@class="text-link"]/text()')
        film_time = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    
        return [film_name,film_type,film_time]
