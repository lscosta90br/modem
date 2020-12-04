from config import settings
import modem_uteis as mu
import json

mu.modem_tim(
            link_webdriver=settings.link_webdriver, 
            link=settings.link_modem_timlive, 
            password=settings.password_modem_timlive,
            operadora ="timlive",
            tempo_debug = 2
)

