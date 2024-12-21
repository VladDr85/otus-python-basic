from pydantic import ValidationError

from view.contacts.contacts_schemas import ContactIn
from .utils import open_contact_base, add_contact, dump_contact_base

class Contact:

    @staticmethod
    def validation(record):
        ContactIn(**record)

    @staticmethod
    def get_all_contacts() -> dict:
        return open_contact_base()

    @staticmethod
    def get_contacts_by_id(contact_id: int) -> dict:
        contact_base = open_contact_base()
        return contact_base[str(contact_id)]

    @staticmethod
    def add_contact(name: str, phone: str, email: str, status: str, city: str):
        try:
            new_contact = ContactIn(name=name, phone=phone, email=email, status=status, city=city)
            dict_contact = {
                'name': name,
                'phone': phone,
                'email': email,
                'status': status,
                'city': city
            }
            add_contact(dict_contact)
            return new_contact
        except ValidationError as e:
            return {"error": e.errors()}

    @staticmethod
    def delete_contact(contact_id_del: int):
        contact_base = open_contact_base()
        contact = {contact_id for contact_id in contact_base if int(contact_id) == contact_id_del}
        if not contact:
            return {"message": "Запись не найдена", "record_id": contact_id_del}
        contact_base = {contact_id:contact for contact_id, contact in contact_base.items() if int(contact_id) != contact_id_del}
        dump_contact_base(contact_base)
        return {"message": "Запись успешно удалена", "record_id": contact_id_del}
