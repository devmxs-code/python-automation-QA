# language: pt
Funcionalidade: Acessar o site do Formulário de Contato

  Cenário: Usuário acessa o site do formulário com sucesso e preenche o formulário
    Dado que o navegador "edge" está aberto
    Quando eu preencher os dados no formulário de contato
    Então devo ver o formulário de contato carregado com sucesso
    E devo submeter o formulário e ver a confirmação de envio
