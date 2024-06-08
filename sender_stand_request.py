import configuration
import requests
import data

# Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


def receiving_order():
    track = post_new_order(data.order_body).json().get("track")
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))
