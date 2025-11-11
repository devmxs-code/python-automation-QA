import sys  # importa módulo sys para manipular path
import os  # importa módulo os para manipular caminhos
import time  # importa módulo time para pausas
from behave import given, when, then  # importa decorators do behave
from selenium.webdriver.common.by import By  # importa seletores de elementos
from selenium.webdriver.common.keys import Keys  # importa teclas do teclado
from selenium.webdriver.support.ui import WebDriverWait  # importa wait para esperas
from selenium.webdriver.support import expected_conditions as EC  # importa condições esperadas

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))  # adiciona raiz ao path
from shared.browser_config import create_driver  # importa função genérica de criar driver

TIMEOUT = 30  # timeout padrão em segundos (maior para whatsapp)
WHATSAPP_URL = "https://web.whatsapp.com"  # url do whatsapp web


def _cleanup_driver(context):  # função auxiliar para limpar driver
    """encerra o navegador se existir"""
    if hasattr(context, 'driver'):  # verifica se driver existe
        context.driver.quit()  # encerra o navegador


@given("que o navegador {browser} está aberto")  # decorator para step "dado que" com parâmetro de navegador
def step_open_browser(context, browser):  # função que abre navegador (safari, edge ou firefox)
    try:  # inicia bloco try para tratamento de erro
        context.browser = browser.lower()  # armazena nome do navegador no context
        context.driver = create_driver(browser.lower())  # cria driver baseado no navegador escolhido
        try:  # tenta maximizar janela
            context.driver.maximize_window()  # maximiza janela (pode não funcionar no safari)
        except:  # ignora erro se não suportar
            pass  # continua execução
        context.driver.get(WHATSAPP_URL)  # navega para whatsapp web
        time.sleep(5)  # aguarda página carregar (whatsapp precisa de tempo para qr code)
    except Exception as e:  # captura exceção
        _cleanup_driver(context)  # limpa driver em caso de erro
        raise Exception(f"erro ao abrir navegador {browser}: {str(e)}")  # relança exceção com mensagem


@when("eu acessar o WhatsApp Web")  # decorator para step "quando"
def step_access_whatsapp(context):  # função que acessa whatsapp
    wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
    try:  # tenta encontrar elemento que indica que está logado
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='chat-list']")))  # aguarda lista de chats aparecer
    except:  # se não encontrar, pode estar na tela de login
        pass  # continua execução (usuário precisa escanear qr code manualmente)


@when('eu buscar pelo contato "{contato}"')  # decorator para step "quando" com parâmetro
def step_search_contact(context, contato):  # função que busca contato "Marcelo Xavier"
    wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
    try:  # tenta encontrar campo de busca "Pesquisar ou começar uma nova conversa"
        # tenta diferentes seletores para o campo de busca
        search_selectors = [  # lista de seletores possíveis
            "[data-testid='chat-list-search']",  # seletor por data-testid
            "div[contenteditable='true'][data-tab='3']",  # seletor por contenteditable
            "div[contenteditable='true'][role='textbox']",  # seletor alternativo
            "input[placeholder*='Pesquisar']",  # seletor por placeholder
            "div[title='Pesquisar ou começar uma nova conversa']",  # seletor por title
            "div[contenteditable='true'][title*='Pesquisar']"  # seletor alternativo com title
        ]
        search_box = None  # inicializa variável
        for selector in search_selectors:  # itera sobre seletores
            try:  # tenta encontrar elemento
                search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))  # aguarda campo aparecer
                break  # sai do loop se encontrar
            except:  # continua se não encontrar
                continue  # tenta próximo seletor
        if not search_box:  # verifica se encontrou campo
            raise Exception("campo de busca não encontrado")  # lança erro se não encontrar
        search_box.click()  # clica no campo de busca
        time.sleep(1)  # aguarda campo ficar ativo
        search_box.clear()  # limpa campo antes de digitar
        search_box.send_keys(contato)  # digita nome do contato "Marcelo Xavier"
        time.sleep(3)  # aguarda resultados aparecerem
        context.contato_buscado = contato  # armazena contato buscado no context
    except Exception as e:  # captura exceção
        raise Exception(f"erro ao buscar contato: {str(e)}")  # relança com mensagem


@when("eu clicar no contato encontrado")  # decorator para step "quando"
def step_click_contact(context):  # função que clica no contato encontrado
    wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
    try:  # tenta encontrar e clicar no contato
        # tenta diferentes seletores para encontrar o contato
        contact_selectors = [  # lista de seletores possíveis
            "[data-testid='cell-frame-container']",  # seletor por data-testid
            "div[role='listitem']",  # seletor por role
            "span[title*='Marcelo Xavier']",  # seletor por title contendo nome
            "div[title*='Marcelo Xavier']"  # seletor alternativo
        ]
        contact = None  # inicializa variável
        for selector in contact_selectors:  # itera sobre seletores
            try:  # tenta encontrar elemento
                contact = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))  # aguarda contato ficar clicável
                break  # sai do loop se encontrar
            except:  # continua se não encontrar
                continue  # tenta próximo seletor
        if not contact:  # verifica se encontrou contato
            # tenta encontrar pelo texto do contato
            contacts = context.driver.find_elements(By.XPATH, "//span[contains(text(), 'Marcelo Xavier')]")  # busca por texto
            if contacts:  # verifica se encontrou
                contact = contacts[0].find_element(By.XPATH, "./ancestor::div[@role='listitem']")  # encontra elemento pai clicável
        if contact:  # verifica se encontrou contato
            contact.click()  # clica no contato
            time.sleep(2)  # aguarda conversa abrir
        else:  # se não encontrou
            raise Exception("contato 'Marcelo Xavier' não encontrado")  # lança erro
    except Exception as e:  # captura exceção
        raise Exception(f"erro ao clicar no contato: {str(e)}")  # relança com mensagem


@when('eu enviar a mensagem "{mensagem}"')  # decorator para step "quando" com parâmetro
def step_send_message(context, mensagem):  # função que envia mensagem "Mensagem enviada!!!"
    wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
    try:  # tenta encontrar campo "Digite uma mensagem"
        # tenta diferentes seletores para o campo de mensagem
        message_selectors = [  # lista de seletores possíveis
            "[data-testid='conversation-compose-box-input']",  # seletor por data-testid
            "div[contenteditable='true'][data-tab='10']",  # seletor por contenteditable
            "div[contenteditable='true'][role='textbox']",  # seletor alternativo
            "div[contenteditable='true'][title*='Digite uma mensagem']",  # seletor por title
            "div[contenteditable='true'][placeholder*='Digite uma mensagem']",  # seletor por placeholder
            "div[title='Digite uma mensagem']"  # seletor direto por title
        ]
        message_box = None  # inicializa variável
        for selector in message_selectors:  # itera sobre seletores
            try:  # tenta encontrar elemento
                message_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))  # aguarda campo aparecer
                break  # sai do loop se encontrar
            except:  # continua se não encontrar
                continue  # tenta próximo seletor
        if not message_box:  # verifica se encontrou campo
            # tenta encontrar por xpath usando texto do placeholder
            try:  # tenta xpath
                message_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and contains(@title, 'Digite uma mensagem')]")))  # busca por xpath
            except:  # se não encontrar
                raise Exception("campo 'Digite uma mensagem' não encontrado")  # lança erro
        message_box.click()  # clica no campo de mensagem
        time.sleep(1)  # aguarda campo ficar ativo
        message_box.clear()  # limpa campo antes de digitar
        message_box.send_keys(mensagem)  # digita mensagem "Mensagem enviada!!!"
        time.sleep(1)  # aguarda mensagem ser digitada
        send_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='send']")))  # aguarda botão enviar ficar clicável
        send_button.click()  # clica no botão enviar
        time.sleep(2)  # aguarda mensagem ser enviada
    except Exception as e:  # captura exceção
        raise Exception(f"erro ao enviar mensagem: {str(e)}")  # relança com mensagem


@then("devo ver a mensagem enviada com sucesso")  # decorator para step "então"
def step_verify_message_sent(context):  # função que verifica envio
    try:  # inicia bloco try
        wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
        time.sleep(2)  # aguarda mensagem aparecer na conversa
        sent_messages = context.driver.find_elements(By.CSS_SELECTOR, "[data-testid='msg-container']")  # encontra todas as mensagens
        assert len(sent_messages) > 0, "nenhuma mensagem encontrada na conversa"  # valida que há mensagens
    except AssertionError:  # captura assertion error
        raise  # relança sem modificar
    except Exception as e:  # captura outras exceções
        raise Exception(f"erro ao verificar mensagem: {str(e)}")  # relança com mensagem
    finally:  # bloco finally sempre executa
        time.sleep(3)  # aguarda antes de fechar (para visualizar resultado)
        _cleanup_driver(context)  # limpa driver ao final

