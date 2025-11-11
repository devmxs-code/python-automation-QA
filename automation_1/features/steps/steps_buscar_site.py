import sys  # importa módulo sys para manipular path
import os  # importa módulo os para manipular caminhos
from behave import given, when, then  # importa decorators do behave
from selenium.webdriver.common.by import By  # importa seletores de elementos
from selenium.webdriver.common.keys import Keys  # importa teclas do teclado
from selenium.webdriver.support.ui import WebDriverWait  # importa wait para esperas
from selenium.webdriver.support import expected_conditions as EC  # importa condições esperadas

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))  # adiciona raiz ao path
from shared.browser_config import create_driver  # importa função genérica de criar driver

TIMEOUT = 10  # timeout padrão em segundos
GOOGLE_URL = "https://www.google.com"  # url do google
SEARCH_TERM = "Instituto Joga Junto"  # termo de busca


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
        context.driver.get(GOOGLE_URL)  # navega para google
        wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
        wait.until(EC.presence_of_element_located((By.NAME, "q")))  # aguarda campo de busca aparecer
    except Exception as e:  # captura exceção
        _cleanup_driver(context)  # limpa driver em caso de erro
        raise Exception(f"erro ao abrir navegador {browser}: {str(e)}")  # relança exceção com mensagem


@when('eu pesquisar por "Instituto Joga Junto" no Google')  # decorator para step "quando"
def step_search_google(context):  # função que realiza busca
    wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
    campo = wait.until(EC.element_to_be_clickable((By.NAME, "q")))  # aguarda campo ficar clicável
    campo.clear()  # limpa campo antes de digitar
    campo.send_keys(SEARCH_TERM, Keys.RETURN)  # digita termo e pressiona enter
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))  # aguarda resultados aparecerem


@then("devo ver o site do Instituto aberto com sucesso")  # decorator para step "então"
def step_verify_site(context):  # função que verifica site
    try:  # inicia bloco try
        wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))  # aguarda resultados
        
        resultados = context.driver.find_elements(By.CSS_SELECTOR, "h3")  # encontra todos os resultados
        if not resultados:  # verifica se há resultados
            raise AssertionError("nenhum resultado encontrado")  # lança erro se não houver
        
        resultado = _find_resultado_jogajunto(resultados) or resultados[0]  # busca resultado específico ou usa primeiro
        wait.until(EC.element_to_be_clickable(resultado))  # aguarda resultado ficar clicável
        resultado.click()  # clica no resultado
        
        wait.until(lambda d: "jogajunto" in d.current_url.lower() or  # aguarda url mudar ou conter jogajunto
                          d.current_url != "https://www.google.com/search")  # ou sair da página de busca
        
        url_atual = context.driver.current_url.lower()  # obtém url atual em minúsculas
        assert "jogajunto" in url_atual, f"url não contém 'jogajunto': {url_atual}"  # valida url contém jogajunto
    except AssertionError:  # captura assertion error
        raise  # relança sem modificar
    except Exception as e:  # captura outras exceções
        raise Exception(f"erro ao verificar site: {str(e)}")  # relança com mensagem
    finally:  # bloco finally sempre executa
        _cleanup_driver(context)  # limpa driver ao final


def _find_resultado_jogajunto(resultados):  # função auxiliar para encontrar resultado
    """encontra resultado que contenha jogajunto"""
    for resultado in resultados:  # itera sobre resultados
        if "jogajunto" in resultado.text.lower() or "instituto joga junto" in resultado.text.lower():  # verifica se contém termo
            return resultado  # retorna resultado encontrado
    return None  # retorna none se não encontrar
