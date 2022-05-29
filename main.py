from Btx import Btx
from data import my_data_list

my_btx_url = 'https://b24-hzzdt4.bitrix24.kz/rest/1/wknstxkqfqabscgn/'


def main(url, js):
    bitrix24 = Btx(url, js)

    # Проверяем есть ли такой клиент
    if bitrix24.check_contact_for_b24():

        print('Клиент есть в системе')

        # Проверяем есть ли такая сделка у клиента по delivery_code
        if bitrix24.is_duplicate_deal_item():

            print('Сделка с таким кодом существует, проверим поля!')
            deal_id = bitrix24.get_deal_id_by_code()

            if not bitrix24.is_there_any_date():
                print('Не совпало поле даты обновляем все поля')
                bitrix24.update_deal_field_delivery_address(deal_id)
                bitrix24.update_deal_field_delivery_date(deal_id)
                bitrix24.add_products(deal_id)
            else:
                print('Поле даты совпало, ничего не делаем')
            if not bitrix24.is_there_any_address():
                print('Не совпало поле адреса обновляем все поля')
                bitrix24.update_deal_field_delivery_address(deal_id)
                bitrix24.update_deal_field_delivery_date(deal_id)
                bitrix24.add_products(deal_id)
            else:
                print('Поле адреса совпало, ничего не делаем')
            if not bitrix24.is_there_any_products(deal_id):
                print('Не совпали продукты обновляем все поля')
                bitrix24.update_deal_field_delivery_address(deal_id)
                bitrix24.update_deal_field_delivery_date(deal_id)
                bitrix24.add_products(deal_id)
            else:
                print('Продукты совпали, ничего не делаем')
        else:
            print('Сделки нет')
            print('Создадим сделку ... ')

            if bitrix24.is_duplicate_deal():
                print('Сделка с таким названием существует')
                return False
            bitrix24.add_deal()
            deal_id = bitrix24.get_last_deal_id()

            # Обновим данные в пользовательских полях
            bitrix24.add_deal_field_delivery_address()
            bitrix24.add_deal_delivery_date()
            bitrix24.add_deal_delivery_code()

            bitrix24.update_deal_field_delivery_address(deal_id)
            bitrix24.update_deal_field_delivery_date(deal_id)
            bitrix24.update_deal_field_delivery_code(deal_id)

            # Получаем id клиента
            client_id = bitrix24.get_client_id()

            # Связываем сделку с клиентом
            bitrix24.add_deal_client(client_id, deal_id)

            # Добавляем товары
            if bitrix24.add_products(deal_id):
                print('Поле продукты обновлено')
            else:
                print('Поле продукты не обновлено')

    else:
        print('Клиента нет в системе!')

        # создадим пользовательские поля
        bitrix24.add_deal_field_delivery_address()
        bitrix24.add_deal_delivery_date()
        bitrix24.add_deal_delivery_code()

        # Добавляем клиента в систему
        bitrix24.add_client()

        # Создаем сделку
        if bitrix24.is_duplicate_deal():
            print('Сделка с таким названием существует')
            return False
        bitrix24.add_deal()

        # получаем id клиента и id сделки
        client_id = bitrix24.get_client_id()
        deal_id = bitrix24.get_last_deal_id()

        # Связываем сделку с клиентом
        bitrix24.add_deal_client(client_id, deal_id)

        # Обновим данные в пользовательских полях
        bitrix24.update_deal_field_delivery_address(deal_id)
        bitrix24.update_deal_field_delivery_date(deal_id)
        bitrix24.update_deal_field_delivery_code(deal_id)
        # Добавляем товары

        bitrix24.add_products(deal_id)


# Данные в js формате приходят
for item_js in my_data_list:
    main(my_btx_url, item_js)
