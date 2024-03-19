import requests

def test_get_all_deliveries(url: str):
    res = requests.get(url).json()
    assert(res == [{'deliveries_id': 1, 'name': 'Яндекс еда',
     'descrption': 'Крупнейший сервис быстрой доставки еды из ресторанров',
     'count_users': '30000000', 'city': 'Moscow'},
    {'deliveries_id': 2, 'name': 'Delivery club',
     'descrption': 'Мобильная и десктопная платформа для доставки еды',
     'count_users': '15000000', 'city': 'Tomsk'},
    {'deliveries_id': 3, 'name': 'Chibbis',
     'descrption': 'Один из трёх крупнейших агрегаторов доставок еды в России',
     'count_users': '10000000', 'city': 'Arhangelsk'}])


def test_get_delivery_by_id(url: str):
    res = requests.get(url).json()
    assert(res == {'deliveries_id': 1, 'name': 'Яндекс еда',
     'descrption': 'Крупнейший сервис быстрой доставки еды из ресторанров',
     'count_users': '30000000', 'city': 'Moscow'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/deliveries/'
    test_get_delivery_by_id(URL + '1')
    test_get_all_deliveries(URL)