from selenium import webdriver
import time

def modem_tim(link_webdriver, link, password):

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "87.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    browser = webdriver.Remote(
        command_executor= link_webdriver,
        desired_capabilities=capabilities)

    browser.get(link)

    #digita a senha    
    passwordbox = browser.find_element_by_xpath('//*[@id="srp_password"]')
    passwordbox.send_keys(password)
    time.sleep(1)
    #clica no botão entra
    entrarButton = browser.find_element_by_xpath('//*[@id="sign-me-in"]')
    entrarButton.click()
    time.sleep(1)
    # click na engranem para pegar options
    bandalargacfg = browser.find_element_by_xpath('//*[@id="Banda Larga"]/i')
    # bandalargacfg = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/div[3]/i')
    bandalargacfg.click()
    time.sleep(1)

    status_id = browser.find_element_by_id('Status DSL')

    status_sinal = status_id.text

    print("")
    print(f"Link da TimLive:")
    # print("")

    # print(type(status_sinal))
    if status_sinal == "NoSignal":
        print(f"O link está:.............. {status_id.text}")
    else:
        tempo_conectado_dsl = browser.find_element_by_id('Tempo conectado DSL')
        line_rate = browser.find_element_by_id('Line Rate')
        print(f"O link está:.............. {status_id.text}")
        print(f"O tempo é:................ {tempo_conectado_dsl.text}")
        print(f"Conexão DSL velocidade:... {line_rate.text}")

    time.sleep(1)

    browser.quit()


