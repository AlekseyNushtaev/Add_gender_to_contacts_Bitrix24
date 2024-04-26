from fast_bitrix24 import Bitrix
from fast_bitrix24.server_response import ErrorInServerResponseException


class BitrixWorker:
    """Класс для работы с Bitrix24"""
    def __init__(self, webhook):
        self.bitrix = Bitrix(webhook)

    def get_contacts(self) -> list:
        """Функция для получения контактов из Bitrix24"""
        try:
            params = {"SELECT": ["ID", "NAME"]}
            contacts = self.bitrix.get_all("crm.contact.list", params)
            return contacts
        except ErrorInServerResponseException:
            pass

    def add_sex_field(self) -> None:
        """Функция для добавления поля SEX в контакты"""
        try:
            items = {
                "FIELD_NAME": "SEX",
                "EDIT_FORM_LABEL": "Пол",
                "LIST_COLUMN_LABEL": "Пол",
                "USER_TYPE_ID": "string",
                "XML_ID": "SEX",
                "SETTINGS": {"DEFAULT_VALUE": "Нет данных"}
            }
            self.bitrix.call("crm.contact.userfield.add", items)
        except ErrorInServerResponseException:
            pass

    def update_sex_field(self, id: int, sex: str) -> None:
        """Функция для записи значения в поле SEX контактов"""
        try:
            items = {
                "id": id,
                "fields": {"UF_CRM_SEX": sex}
            }
            self.bitrix.call("crm.contact.update", items)
        except ErrorInServerResponseException:
            pass


