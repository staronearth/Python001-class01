from getwebsinfo import * 
import pandas as pd
#获取猫眼网页信息
getwebinfo = getwebsinfo()
urls = tuple(f'https://maoyan.com/films?showType=10&offset={page*30}' for page in range(4))
total_list=[]
for url in urls:
    response = getwebinfo.getweb(url)
    file_list=getwebinfo.responseurlinfo(response)
    # print(file_list)

    for film_url in file_list:
        total_list.append(getwebinfo.getfilminfo(film_url))
    # print(total_list)

moive = pd.DataFrame(data=total_list)

moive.to_csv('./movie.csv', encoding='utf8' , index=False ,header=False)
