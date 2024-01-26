from whatsapp_api_client_python.API import GreenApi
import settings


class WhatsAppClient:
    def __init__(self):
        self.settings = settings.Settings()
        self.restApi = GreenApi(
            host=self.settings.wa_host,
            media=self.settings.wa_media_host,
            idInstance=self.settings.wa_id_instance,
            apiTokenInstance=self.settings.wa_api_token_instance
        )


wa_client = WhatsAppClient()
result = wa_client.restApi.serviceMethods.getContacts().data

