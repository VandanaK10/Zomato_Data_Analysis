import pandas as pd
df = pd.read_csv("zomato.csv")
df2=df.drop(columns=['url', 'phone', 'rest_type', 'dish_liked', 'reviews_list', 'menu_item', 'listed_in(city)'])
df3=df2.rename(columns={'approx_cost(for two people)':'two_people_cost','listed_in(type)':'type_of_restaurant'})
df4=df3.rename(columns={'rate':'rating'})
df4=df4.dropna(subset=['location'])
df4=df4.dropna(subset=['cuisines','two_people_cost'])
df4['two_people_cost']=df4['two_people_cost'].str.replace(',', '').astype(int)
df4['two_people_cost']=df4['two_people_cost']/2
df4=df4.rename(columns={'two_people_cost':'cost_per_person'})
import numpy as np
def handlerate(value) :
    if(value== 'NEW' or value=='-'):
        return np.nan
    else:
        value = str(value).split('/')
        value = value [0]
        return float(value)
        
df4['rating'] = df4['rating'].apply(handlerate)
df4['rating']=df4['rating'].fillna(df4['rating'].mean)
df4['online_order']=df4['online_order'].astype("string")
df4['book_table']=df4['book_table'].astype("string")
df4['location']=df4['location'].astype("string")
df4['cuisines']=df4['cuisines'].astype("string")
df4.drop_duplicates(inplace=True)
df4['name']=df4['name'].str.title()
df4['location']=df4['location'].str.title()
df4['cuisines']=df4['cuisines'].str.title()
df4['type_of_restaurant']=df4['type_of_restaurant'].str.title()
df4.drop(columns=['type_of_restuarant'],inplace=True)
df4.info()
df4.to_csv("zomato_data_analysis.csv", index=False)