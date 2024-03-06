from persistance.people_repository import PeopleRepository
from clients.whatsapp_client import WhatsAppClient
from models.person_model import PersonModel


class DataLoader:
    def __init__(self, repository: PeopleRepository, wa_client: WhatsAppClient):
        self.repository = repository
        self.wa_client = wa_client

    async def load_contact_data_to_db(self):
        wa_contacts_data = self.wa_client.get_contacts_data()
        for contact in wa_contacts_data:
            if contact.get('type') == 'user':
                wa_id = contact.get('id')
                name = contact.get('name')
                phone_number = wa_id[:11]
                await self.repository.create_new_person(PersonModel(wa_id=wa_id, name=name, phone_number=phone_number))
