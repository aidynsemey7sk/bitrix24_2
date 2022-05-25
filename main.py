from Btx import Btx

my_js = {
    "title": "New Deal 1",
    "description": "Some description",
    "client": {
        "name": "Aika",
        "surname": "Zaika",
        "phone": "+70550130100",
        "address": "st. Mira, 287, Moscow"
    },
    "products": ["Candy", "Carrot", "Potato"],
    "delivery_address": "st. Mira, 211, Ekaterinburg",
    "delivery_date": "2021-01-01:16:00",
    "delivery_code": "#sda*&gsabhd126"
}

btx = Btx('https://b24-hzzdt4.bitrix24.kz/rest/1/wknstxkqfqabscgn/', my_js)

my_btx_url = 'https://b24-hzzdt4.bitrix24.kz/rest/1/wknstxkqfqabscgn/'

# print(btx.get_deal_list())
# print(btx.add_client())
# print(btx.get_client())
# print(btx.add_deal_client())
# print(btx.check_contact_for_b24())
# print(btx.add_deal())
# print(btx.get_client_id())
# print(btx.get_deal_id('#sda*&gsabhd126'))
# print(btx.is_duplicate_deal_item())
# print(btx.add_fields())
# print(btx.add_deal_custom_fields())
print(btx.get_all_deal_fields())


def main(url, js):
    bitrix24 = Btx(url, js)
    if bitrix24.check_contact_for_b24():
        # Проверяем есть ли такой клиент
        print('Клиент есть в системе')
        pass
    else:
        # Добавляем клиента в систему
        print('Клиента нету в системе')
        bitrix24.add_client()
        # Создаем сделку
        bitrix24.add_deal()
        # получаем id клиента и id сделки
        client_id = bitrix24.get_client_id()
        deal_id = bitrix24.get_deal_id()
        # Связываем сделку с клиентом
        bitrix24.add_deal_client(client_id, deal_id)



    # получаем id клиента и id сделки
    client_id = bitrix24.get_client_id()
    deal_id = bitrix24.get_deal_id()




# main(my_btx_url, my_js)
