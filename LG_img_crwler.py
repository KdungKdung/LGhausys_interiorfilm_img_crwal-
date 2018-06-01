from  bs4 import BeautifulSoup as bs
import requests
import re
import urllib.request




zin_interior_film  = requests.get('http://www.lghausys.co.kr/rn/productcategory/search_for_product.jsp')
soup = bs(zin_interior_film.text, 'html.parser')

#soup_model_link = soup.findAll('a').get('href')
#a태그에서 href만 가져온다. a가 배열이니까 이렇게하면 안돼고 for문으로 가져와준다.

soup_model_link = soup.findAll('a')
array = []

passArry = [] #크롤링을 하지 못한 목록

p = re.compile("mid_category=B04")
#compile 정규표현을 위한 컴파일 된 패턴객체 만들어준다.(정규편표힌저장)
#인테리이필름의 카테고리는 B04

for x in soup_model_link:
    temp = x.get('href')
    if p.search(temp) != None:
        array.append('http://www.lghausys.co.kr'+temp)




#arry에 B04가 포함 된 하이퍼링크를 저장해준다.

#print(array)


'''
<div class="page__view page__view--typA" id="js-prd-view" style="background-image:url('/upload/product/201804/20180410/15E0519E-BF90-5756-58CA-CE3EF45D6E85.jpg');"> <!-- [D] style에 해당 이미지 -->
<div class="prd-view__btns">
<!-- [D] data-src=""에 확대 혹은 질감 이미지 URL -->
<button class="prd-view__btn prd-view__btn--zoomin" data-src="/upload/product/201804/20180410/5E9E220A-14B9-2DE1-9A53-E98D1D0633B4_thumb_l.jpg" type="button">확대<span class="sr-only">레이어 열기</span></button>
</div>
</div>
'''
# ' 로 스프릿해서 [1]의 값이 URL부분이다.
count = 0
for img_index in array :


    print(array[count])
    count +=1
    tmep_url = requests.get(img_index)
    soup = bs(tmep_url.text, 'html.parser')



    soup_title = soup.find('h3', {"class": "page__tit"})

    print("현재타이틀\n" + str(soup_title))



    soup_img = soup.find('div', {"class": "page__view page__view--typA"})

    print("출력해보면 : "+str(soup_img))
    if soup_img is None:
        print("패스한다.")
        passArry.append(soup_title)
        continue
    #이미지가 없을 경우 패스!
    print("시작\n" + str(soup_img))

    img_url = 'http://www.lghausys.co.kr'+str(soup_img).split("'")[1]
    a = "img\\"
    b = soup_title.text+'.jpg'
    urllib.request.urlretrieve(img_url, a+b)




print("크롤링하지못한 목록은 ")
print(passArry)
