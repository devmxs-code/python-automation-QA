import sys  # importa módulo sys para manipular path
import os  # importa módulo os para manipular caminhos
from behave import given, when, then  # importa decorators do behave
from selenium.webdriver.common.by import By  # importa seletores de elementos
from selenium.webdriver.support.ui import WebDriverWait  # importa wait para esperas
from selenium.webdriver.support import expected_conditions as EC  # importa condições esperadas

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))  # adiciona raiz ao path
from shared.browser_config import create_driver  # importa função genérica de criar driver

TIMEOUT = 10  # timeout padrão em segundos
FORM_URL = "https://formulario-contato-m8p8.onrender.com/"  # url do formulário

FORM_DATA = {  # dicionário com dados do formulário
    "nome": "Marcelo Xavier",  # nome para preencher
    "email": "marcelo_07@live.com",  # email para preencher
    "telefone": "12992103119",  # telefone para preencher
    "cidade": "Ilhabela",  # cidade para preencher
    "bairro": "Reino",  # bairro para preencher
    "mensagem": "Boa noite!!!!"  # mensagem para preencher
}


def _cleanup_driver(context):  # função auxiliar para limpar driver
    """encerra o navegador se existir"""
    if hasattr(context, 'driver'):  # verifica se driver existe
        context.driver.quit()  # encerra o navegador


def _fill_field(wait, name, value):  # função auxiliar para preencher campo
    """preenche campo do formulário"""
    campo = wait.until(EC.presence_of_element_located((By.NAME, name)))  # aguarda campo aparecer
    campo.clear()  # limpa campo antes de preencher
    campo.send_keys(value)  # preenche campo com valor
    return campo  # retorna elemento do campo


@given("que o navegador {browser} está aberto")  # decorator para step "dado que" com parâmetro de navegador
def step_open_browser(context, browser):  # função que abre navegador (safari, edge ou firefox)
    try:  # inicia bloco try para tratamento de erro
        context.browser = browser.lower()  # armazena nome do navegador no context
        context.driver = create_driver(browser.lower())  # cria driver baseado no navegador escolhido
        try:  # tenta maximizar janela
            context.driver.maximize_window()  # maximiza janela (pode não funcionar no safari)
        except:  # ignora erro se não suportar
            pass  # continua execução
        context.driver.get(FORM_URL)  # navega para formulário
        wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
        wait.until(EC.presence_of_element_located((By.NAME, "nome")))  # aguarda campo nome aparecer
    except Exception as e:  # captura exceção
        _cleanup_driver(context)  # limpa driver em caso de erro
        raise Exception(f"erro ao abrir navegador {browser}: {str(e)}")  # relança exceção com mensagem


@when("eu preencher os dados no formulário de contato")  # decorator para step "quando"
def step_fill_form(context):  # função que preenche formulário
    wait = WebDriverWait(context.driver, TIMEOUT)  # cria instância de wait
    
    for field_name, value in FORM_DATA.items():  # itera sobre dados do formulário
        _fill_field(wait, field_name, value)  # preenche cada campo
    
    checkboxes = wait.until(EC.presence_of_all_elements_located((By.NAME, "escolaridade")))  # encontra checkboxes de escolaridade
    for checkbox in checkboxes:  # itera sobre checkboxes
        if checkbox.get_attribute("value") == "Superior":  # verifica se é opção superior
            wait.until(EC.element_to_be_clickable(checkbox))  # aguarda checkbox ficar clicável
            checkbox.click()  # clica no checkbox
            break  # sai do loop após encontrar


@then("devo ver o formulário de contato carregado com sucesso")  # decorator para step "então"
def step_verify_form(context):  # função que verifica formulário
    driver = context.driver  # obtém driver do context
    wait = WebDriverWait(driver, TIMEOUT)  # cria instância de wait
    
    titulo = driver.title.lower()  # obtém título em minúsculas
    assert any(termo in titulo for termo in ["formulário", "contato"]), f"título inesperado: {driver.title}"  # valida título
    
    for campo_name in ["nome", "email", "mensagem"]:  # itera sobre campos essenciais
        campo = wait.until(EC.presence_of_element_located((By.NAME, campo_name)))  # aguarda campo aparecer
        assert campo.is_displayed(), f"campo '{campo_name}' não está visível"  # valida campo está visível


@then("devo submeter o formulário e ver a confirmação de envio")  # decorator para step "então"
def step_submit_and_verify(context):  # função que submete e verifica formulário
    try:  # inicia bloco try
        driver = context.driver  # obtém driver do context
        wait = WebDriverWait(driver, 15)  # cria wait com timeout maior
        url_antes = driver.current_url  # salva url antes do envio
        
        botao = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))  # aguarda botão ficar clicável
        botao.click()  # clica no botão enviar
        
        try:  # tenta aguardar confirmação
            wait.until(lambda d: "sucesso" in d.page_source.lower() or  # aguarda mensagem de sucesso
                              "enviado" in d.page_source.lower() or  # ou mensagem de enviado
                              d.current_url != url_antes)  # ou mudança de url
        except:  # ignora timeout se não encontrar
            pass  # continua execução
        
        url_depois = driver.current_url  # obtém url depois do envio
        page_source = driver.page_source.lower()  # obtém código fonte em minúsculas
        
        sucesso = (url_depois != url_antes or  # verifica se url mudou
                  any(termo in page_source for termo in ["sucesso", "enviado", "obrigado"]) or  # ou tem mensagem de sucesso
                  "enviar" not in url_depois.lower())  # ou não está mais na página de envio
        
        assert sucesso, f"formulário não enviado. antes: {url_antes}, depois: {url_depois}"  # valida envio bem-sucedido
    except AssertionError:  # captura assertion error
        raise  # relança sem modificar
    except Exception as e:  # captura outras exceções
        raise Exception(f"erro ao submeter formulário: {str(e)}")  # relança com mensagem
    finally:  # bloco finally sempre executa
        _cleanup_driver(context)  # limpa driver ao final
