from clients.whatsapp_client import WhatsAppClient
from settings import settings

wa_client = WhatsAppClient(settings)
result = wa_client.restApi.serviceMethods.getContacts().data
for r in result:
    if r.get('type') == 'user':
        wa_id = r.get('id')
        name = r.get('name')

