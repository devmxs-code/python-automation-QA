# language: pt
Funcionalidade: Enviar mensagem no WhatsApp Web

  Cenário: Usuário acessa WhatsApp Web e envia mensagem
    Dado que o navegador "safari" está aberto
    Quando eu acessar o WhatsApp Web
    E eu buscar pelo contato "Marcelo Xavier"
    E eu clicar no contato encontrado
    E eu enviar a mensagem "Mensagem enviada!!!"
    Então devo ver a mensagem enviada com sucesso

