import pymysql
from pymysql import cursors
import requests
from bs4 import BeautifulSoup
import pandas as pd


def create_connection():
    connection = pymysql.connect(host='sql6.freemysqlhosting.net',
                            user='sql6439983',
                            password='FD5pgPYpWQ',
                            database='sql6439983',
                            cursorclass=pymysql.cursors.DictCursor)
    return connection    
​
# create new table using execute command
# table query
query = '''CREATE TABLE `SWAGKICKS_DB` (
    `Product_Name` varchar(255) NOT NULL,
    `Product_Prize` varchar(255) NOT NULL,
    `Product_Condition` varchar(255) NOT NULL,
    `Product_Size` varchar(255) NOT NULL
    
) ENGINE=InnoDB  ;'''

# Table Create in Database
connection = create_connection()
with connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()


#connection = create_connection()
def run_query(q1,q2):
    connection = create_connection()        
    with connection:
            with connection.cursor() as cursor:
                cursor.execute(q1,q2)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

q1 = "INSERT INTO SWAGKICKS_DB(Product_Name, Product_Prize, Product_Condition,Product_Size) VALUES(%s,%s,%s,%s)"

# q2 = ('ADIDAS NIKE','Rs.3,999.00','Condition: 9/10','Size: EUR 39')
# run_query(q1,q2)

#run_query(q1)





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
        run_query(q1,(product_name[i].text.strip(),product_price[i].text.strip(),product_size[i].text.strip(),product_condition[i].text.strip()))
        print(product_name[i])

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

print("done")
#df = pd.DataFrame({'Product Name':product_name1,'Product Prize': product_price1,'Product Condition':product_condition1,'Product Size':product_size1},columns=['Product Name','Product Prize','Product Condition','Product Size'])


#df.to_csv('SwagKicks.csv',index=False)
