from bitrix24 import Bitrix24, BitrixError

Red = "\033[31m"
Yellow = "\033[33m"
Green = "\033[32m"
reset = '\033[0m'


class Btx:
    def __init__(self, webhook, input_data):
        self.bx24 = Bitrix24(webhook)
        self.input_data = input_data
        self.products = input_data['products']
        self.client = input_data['client']
        self.phone_client = input_data['client']['phone']
        self.delivery_code = input_data['delivery_code'][1:]
        self.delivery_address = input_data['delivery_address']
        self.delivery_date = input_data['delivery_date']

    def add_deal_delivery_date(self) -> bool:
        try:
            self.bx24.callMethod(
                'crm.deal.userfield.add',
                fields={
                    "ID": 1,
                    'XML_ID': 1,
                    "FIELD_NAME": "DELIVERY_DATE",
                    'USER_TYPE_ID': 'string',
                },
            )
            return True
        except BitrixError:
            return False

    def add_deal_delivery_code(self) -> bool:
        try:
            self.bx24.callMethod(
                'crm.deal.userfield.add',
                fields={
                    "ID": 2,
                    'XML_ID': 2,
                    "FIELD_NAME": "DELIVERY_CODE",
                    'USER_TYPE_ID': 'string',
                },
            )
            return True
        except BitrixError:
            return False

    def add_deal_field_delivery_address(self) -> bool:
        try:
            self.bx24.callMethod(
                'crm.deal.userfield.add',
                fields={
                    "ID": 3,
                    'XML_ID': 3,
                    "FIELD_NAME": "DELIVERY_ADDRESS",
                    'USER_TYPE_ID': 'string',
                },
            )
            return True
        except BitrixError:
            return False

    def update_deal_field_delivery_address(self, deal_id: int) -> bool:
        try:
            self.bx24.callMethod(
                'crm.deal.update',
                id=deal_id,
                fields={
                    'UF_CRM_DELIVERY_ADDRESS': self.input_data['delivery_address']
                },
            )
            return True
        except BitrixError as error:
            print(error)
            return False

    def update_deal_field_delivery_date(self, deal_id: int) -> bool:
        try:
            self.bx24.callMethod(
                'crm.deal.update',
                ID=deal_id,
                fields={
                    'UF_CRM_DELIVERY_DATE': self.input_data['delivery_date']
                },
            )
            return True
        except BitrixError as error:
            print(error)
            return False

    def update_deal_field_delivery_code(self, deal_id: int) -> bool:
        try:
            self.bx24.callMethod(
                'crm.deal.update',
                id=deal_id,
                fields={
                    'UF_CRM_DELIVERY_CODE': self.delivery_code
                },
            )
            return True
        except BitrixError as error:
            print(error)
            return False

    def add_deal(self) -> bool:
        try:
            self.bx24.callMethod(
                'crm.deal.add',
                fields={
                    "TITLE": self.input_data['title'],
                    "ADDITIONAL_INFO": self.input_data['description'],
                }
            )
            print(f'{Green}Сделка создана{reset}')
            return True
        except BitrixError as error:
            print(error)
            return False

    def get_client(self) -> dict:
        client = self.bx24.callMethod(
            'crm.contact.list',
            order={'STAGE_ID': 'ASC'},
            filter={'PHONE': self.phone_client},
            select=['ID', 'NAME', 'LAST_NAME', 'PHONE']
        )
        return client[0]

    def add_client(self) -> bool:
        try:
            self.bx24.callMethod(
                'crm.contact.add',
                fields={
                    'NAME': self.client['name'],
                    'LAST_NAME': self.client['surname'],
                    'PHONE': [{"VALUE": self.phone_client}],
                    'ADDRESS': self.client['address'],
                }
            )
            print(f'{Yellow}Клиент успешно создан!{reset}')
            return True
        except BitrixError as error:
            print(error)
            return False

    def add_deal_client(self, client_id: str, deal_id: int) -> bool:
        try:
            self.bx24.callMethod(
                'crm.deal.contact.add',
                id=deal_id,
                fields={'CONTACT_ID': client_id}
            )
            return True
        except BitrixError as error:
            print(error)
            return False

    def check_contact_for_b24(self) -> bool:
        contact = self.bx24.callMethod(
            'crm.contact.list',
            order={'STAGE_ID': 'ASC'},
            filter={'PHONE': f'{self.phone_client}'},
            select=['ID', 'NAME', 'LAST_NAME', 'HAS_PHONE', 'PHONE']
        )
        if contact:
            print(f'Клиент с номером {self.phone_client} его id: {contact[0]["ID"]} имя: {contact[0]["NAME"]}')
            return True
        else:
            print(f'Клинета с номером {self.phone_client} не существует его необходимо добавить в базу')
            return False

    def get_client_id(self) -> str:
        contact = self.bx24.callMethod(
            'crm.contact.list',
            filter={'PHONE': f'{self.phone_client}'},
            select=['ID']
        )
        return contact[0]['ID']

    def get_last_deal_id(self) -> int:
        deal_id = self.bx24.callMethod(
            'crm.deal.list',
            order={"ID": "DESC"},
            select=['ID']
        )
        return int(deal_id[0]["ID"])

    def get_deal_id_by_code(self) -> int:
        deal_id = self.bx24.callMethod(
            'crm.deal.list',
            filter={'DELIVERY_CODE': self.delivery_code},
            select=['ID']
        )
        return int(deal_id[0]['ID'])

    def is_duplicate_deal_item(self) -> bool:
        deal_id = self.bx24.callMethod(
            'crm.deal.list',
            filter={'UF_CRM_DELIVERY_CODE': self.delivery_code},
            select=['UF_CRM_DELIVERY_CODE']
        )
        if not deal_id:
            print("У клиента нет сделки с таким кодом!")
            return False
        if deal_id[0]["UF_CRM_DELIVERY_CODE"] == self.delivery_code:
            print('У клиента есть сделка с таким кодом!')
            return True
        else:
            print("У клиента нет сделки с таким кодом!")
            return False

    def add_products(self, id_deal: int) -> bool:
        try:
            self.bx24.callMethod(
                "crm.deal.productrows.set",
                ID=id_deal,
                rows={
                    1: {'PRODUCT_ID': 1, 'PRODUCT_NAME': self.products[0], 'QUANTITY': 1, 'PRICE': 100},
                    2: {'PRODUCT_ID': 3, 'PRODUCT_NAME': self.products[1], 'QUANTITY': 1, 'PRICE': 1200},
                    3: {'PRODUCT_ID': 5, 'PRODUCT_NAME': self.products[2], 'QUANTITY': 1, 'PRICE': 1800}
                },

            )
            return True
        except BitrixError as error:
            print(error)
            return False

    def is_there_any_address(self) -> bool:
        deal_id = self.bx24.callMethod(
            'crm.deal.list',
            filter={'DELIVERY_ADDRESS': self.delivery_address},
            select=["UF_CRM_DELIVERY_ADDRESS"]
        )
        if deal_id[0]['UF_CRM_DELIVERY_ADDRESS'] == self.delivery_address:
            return True
        else:
            return False

    def is_there_any_date(self) -> bool:
        deal_id = self.bx24.callMethod(
            'crm.deal.list',
            filter={'DELIVERY_DATE': self.delivery_date},
            select=["UF_CRM_DELIVERY_DATE"]
        )
        if deal_id[0]['UF_CRM_DELIVERY_DATE'] == self.delivery_date:
            return True
        else:
            return False

    def is_there_any_products(self, deal_id: int) -> bool:
        deal_id = self.bx24.callMethod(
            "crm.deal.productrows.get",
            id=deal_id,
        )
        list_product = []
        for i in deal_id:
            list_product.append(i['PRODUCT_NAME'])
        if list_product == self.products:
            return True
        else:
            return False

    def is_duplicate_deal(self) -> bool:
        duplicate = self.bx24.callMethod(
            "crm.deal.list",
            filter={"TITLE": self.input_data['title']},
            select=['ID', "TITLE"]
        )
        if duplicate:
            return True
        else:
            return False

    def get_all_products_in_deal(self, deal_id):
        products = self.bx24.callMethod(
            "crm.deal.productrows.get",
            ID=deal_id,
        )
        my_products = []
        for item in products:
            my_products.append(item["PRODUCT_NAME"])
        print(my_products)