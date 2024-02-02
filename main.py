from clients.whatsapp_client import WhatsAppClient
from settings import settings

wa_client = WhatsAppClient(settings)
result = wa_client.restApi.serviceMethods.getContacts().data


