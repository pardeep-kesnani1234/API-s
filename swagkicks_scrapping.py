import requests
from bs4 import BeautifulSoup
import pandas as pd




All_brand_url = 'https://www.swag-kicks.com/collections/all'
all_brand_response = requests.get(All_brand_url)
r_session = requests.session()
r = r_session.get(url=All_brand_url)
#print(r)
brand_soup = BeautifulSoup(all_brand_response.text,'html.parser')

all_brands_css = 'div.Brands-filter select.coll-filter'
all_brands = brand_soup.select(all_brands_css)
#all_brands[0].text.strip().split('\n')[1:]
Brands = all_brands[0].text.strip().split('\n')[1:]


#['NIKE', 'TIMBERLAND', 'FILA', 'ADIDAS', 'AND 1', 'UNDER ARMOUR', '361 DEGREE', 'NEW BALANCE', 'SKECHERS', 'K-SWISS', 'ASICS', 'AMERICAN EAGLE', 'LEVIS', 'SPERRY', 'SALOMON', 'CONVERSE', 'GRACELAND', 'AVIA', 'KAPPA', 'LACOSTE', 'VANS', 'COMFY SNEAKERS']

#Brands[3]

# for seq in range(10):
#     print(seq)

product_name1 =  []
product_price1 =  []
product_size1 =  []
product_condition1 =  []


for  i in range(2):

    page = i+1


    url = 'https://www.swag-kicks.com/search?page='+str(page)+'&q='+Brands[3]+'&type=product'

    r = requests.get(url)

    r_session = requests.session()

    r = r_session.get(url=url)

    #print(r)


    soup = BeautifulSoup(r.text,'html.parser')

    #print(soup)

    #li.product h2.product-name a





    product_name_css = 'li.product h2.product-name a'
    product_name = soup.select(product_name_css)
    #product_name[1].text.strip()

    product_price_css = 'li.product div.special-price span.money'
    product_price = soup.select(product_price_css)
    #product_price[1].text.strip()


    product_size_css = 'li.product div.price li.custom-varient h5'
    product_size = soup.select(product_size_css)
    #product_size[1].text.strip()


    product_condition_css = 'li.item div.price li.custom-varient-2 h5'
    product_condition = soup.select(product_condition_css)
    #roduct_condition[1].text.strip()



    for i in range(len(product_name)):
        ##print("Product "+str(i+1)+" "+product_name[i].text.strip())
        product_name1.append(product_name[i].text.strip())
        product_price1.append(product_price[i].text.strip())
        product_size1.append(product_size[i].text.strip())
        product_condition1.append(product_condition[i].text.strip())

    # product_price_css = 'li.product div.special-price span.money'
    # product_price = soup.select(product_price_css)
    # product_price[1].text.strip()
    # for i in range(len(product_price)):
    #     print("Product "+str(i+1)+" "+product_price[i].text.strip())
    #     product_price1.append(product_price[i].text.strip())

    # #li.product div.special-price span.money


    # #li.product div.price li.custom-varient h5
    # product_size_css = 'li.product div.price li.custom-varient h5'
    # product_size = soup.select(product_size_css)
    # product_size[1].text.strip()
    # for i in range(len(product_size)):
    #     print("Product "+str(i+1)+" "+product_size[i].text.strip())
    #     product_size1.append(product_size[i].text.strip())


    # #li.item div.price li.custom-varient-2 h5

    # product_condition_css = 'li.item div.price li.custom-varient-2 h5'
    # product_condition = soup.select(product_condition_css)
    # product_condition[1].text.strip()
    # for i in range(len(product_condition)):
    #     print("Product "+str(i+1)+" "+product_condition[i].text.strip())
    #     product_condition1.append(product_condition[i].text.strip())



    #product_name1
    #product_price1
    #product_condition1
    #product_size1


df = pd.DataFrame({'Product Name':product_name1,'Product Prize': product_price1,'Product Condition':product_condition1,'Product Size':product_size1},columns=['Product Name','Product Prize','Product Condition','Product Size'])


df.to_csv('SwagKicks.csv',index=False)




#div.toolbar-bottom div.collection-sorting-row


# url = 'https://www.swag-kicks.com/search?page='+page+'&q='+Brands[3]+'&type=product'

# r = requests.get(url)

# r_session = requests.session()

# r = r_session.get(url=url)

# #print(r)


# soup = BeautifulSoup(r.text,'html.parser')

# all_brands_css = 'div.toolbar-bottom div.collection-sorting-row'
# all_brands = soup.select(all_brands_css)

# #soup 
# all_brands
