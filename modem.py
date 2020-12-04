from config import settings
import modem_uteis as mu

mu.modem_tim(settings.link_webdriver, settings.link, settings.password)

