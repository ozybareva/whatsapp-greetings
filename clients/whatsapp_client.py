from whatsapp_api_client_python.API import GreenApi
from settings import Settings


class WhatsAppClient:
    def __init__(self, settings: Settings):
        self.restApi = GreenApi(
            host=settings.wa_host,
            media=settings.wa_media_host,
            idInstance=settings.wa_id_instance,
            apiTokenInstance=settings.wa_api_token_instance
        )
