# Importa as bibliotecas necessárias
from behave import given, when, then  # Para os steps do BDD
from selenium.webdriver.common.by import By  # Para localizar elementos na página
from shared.browser_config import create_driver  # Para criar o navegador

# Step 1: Abrir o navegador
@given("que o navegador {browser} está aberto")
def step_open_browser(context, browser):
    # Cria o driver do navegador (Chrome, Firefox, etc)
    context.driver = create_driver(browser)
    # Abre a URL do formulário de contato
    context.driver.get("https://formulario-contato-m8p8.onrender.com/")

# Step 2: Preencher o formulário
@when("eu preencher os dados no formulário de contato")
def step_fill_form(context):
    driver = context.driver
    
    # Preenche o campo nome
    driver.find_element(By.NAME, "nome").send_keys("Marcelo Xavier")
    # Preenche o campo email
    driver.find_element(By.NAME, "email").send_keys("marcelo_07@live.com")
    # Preenche o campo telefone
    driver.find_element(By.NAME, "telefone").send_keys("12992103119")
    # Preenche o campo mensagem
    driver.find_element(By.NAME, "mensagem").send_keys("Boa noite!!!!")
    
    # Procura e marca a checkbox "Superior" em escolaridade
    for checkbox in driver.find_elements(By.NAME, "escolaridade"):
        if checkbox.get_attribute("value") == "Superior":
            checkbox.click()  # Clica na checkbox
            break  # Para o loop após encontrar

# Step 3: Verificar se o formulário carregou
@then("devo ver o formulário carregado")
def step_verify_form(context):
    driver = context.driver
    # Verifica se o campo nome está visível na tela
    assert driver.find_element(By.NAME, "nome").is_displayed()
    # Verifica se o campo email está visível na tela
    assert driver.find_element(By.NAME, "email").is_displayed()

# Step 4: Enviar o formulário e fechar
@then("devo submeter o formulário")
def step_submit_form(context):
    driver = context.driver
    # Clica no botão de enviar formulário
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Fecha o navegador após o envio
    driver.quit()
