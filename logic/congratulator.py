from datetime import date
from persistance.people_repository import PeopleRepository
from clients.whatsapp_client import WhatsAppClient


class Congratulator:
    def __init__(self, repository: PeopleRepository, wa_client: WhatsAppClient):
        self.repository = repository
        self.wa_client = wa_client

    async def congratulate(self):
        birthday_people = await self.repository.get_people_by_birth_date(date.today())
        message = 'С днем рождения!'
        for person in birthday_people:
            self.wa_client.send_message(person.wa_id, message)