import configuration
import requests


#функция создания заказа
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,  # подставляем полный url
                         json=body)  # тут тело

#response = post_create_order(data.order_body);
#print(response.status_code)
#print(response.json())
#track = response.json()['track']

#функция получения заказа по треку заказа
def get_accept_order(track2):
    #print(track2) #вывод на экран track заказа
    return requests.get(configuration.URL_SERVICE + configuration.ACCEPT_ORDER +str(track2))

#print(response.json())










