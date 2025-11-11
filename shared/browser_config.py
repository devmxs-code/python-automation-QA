"""configuração compartilhada do navegador edge, safari e firefox"""

import os  # importa módulo os para variáveis de ambiente
from selenium.webdriver import Edge, Safari, Firefox  # importa drivers
from selenium.webdriver.edge.options import Options as EdgeOptions  # importa opções do edge
from selenium.webdriver.firefox.options import Options as FirefoxOptions  # importa opções do firefox
from selenium.webdriver.support.ui import WebDriverWait  # importa wait para esperas explícitas


def create_edge_driver():  # função para criar driver configurado do edge
    """cria instância configurada do edge"""
    options = EdgeOptions()  # cria objeto de opções
    options.add_argument("--start-maximized")  # maximiza janela ao iniciar
    options.add_argument("--disable-blink-features=AutomationControlled")  # desativa detecção de automação
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # remove logs desnecessários
    return Edge(options=options)  # retorna driver configurado


def create_safari_driver():  # função para criar driver configurado do safari
    """cria instância configurada do safari"""
    # nota: safari precisa ter "allow remote automation" habilitado nas preferências do desenvolvedor
    return Safari()  # retorna driver do safari (não precisa de opções no safari)


def create_firefox_driver():  # função para criar driver configurado do firefox
    """cria instância configurada do firefox"""
    options = FirefoxOptions()  # cria objeto de opções
    options.add_argument("--width=1920")  # define largura da janela
    options.add_argument("--height=1080")  # define altura da janela
    return Firefox(options=options)  # retorna driver configurado


def create_driver(browser=None):  # função genérica para criar driver baseado no navegador escolhido
    """cria driver baseado no navegador especificado ou variável de ambiente"""
    browser = browser or os.getenv("BROWSER", "safari").lower()  # obtém navegador do parâmetro ou variável de ambiente (padrão: safari)
    if browser == "safari":  # verifica se é safari
        return create_safari_driver()  # retorna driver do safari
    elif browser == "edge":  # verifica se é edge
        return create_edge_driver()  # retorna driver do edge
    elif browser == "firefox":  # verifica se é firefox
        return create_firefox_driver()  # retorna driver do firefox
    else:  # se não for nenhum dos anteriores
        raise ValueError(f"navegador '{browser}' não suportado. use: safari, edge ou firefox")  # lança erro


def create_wait(driver, timeout=10):  # função para criar wait
    """cria instância de webdriverwait"""
    return WebDriverWait(driver, timeout)  # retorna instância de wait
