# Сергей Гацко, 8-я когорта - Финальный проект. Инженер по тестированию плюс.
import sender_stand_request
import data

#функция получения track заказа
def new_order_track ():
    response = sender_stand_request.post_create_order(data.order_body.copy())
    auth_track = response.json()["track"]
    return auth_track

# тест
def test_accept_order():
        # В переменную set_response сохраняется результат запроса на получение заказа:
    set_response = sender_stand_request.get_accept_order(new_order_track())
    #print(set_response.json()) #вывод на экран ответа сервера
    #print(set_response.status_code) #вывод на экран кода ответа сервера
        # Проверяется, что код ответа равен 200
    assert set_response.status_code == 200





