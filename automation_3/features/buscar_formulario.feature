# language: pt
Funcionalidade: Preencher formulário de contato

  Cenário: Preencher e enviar formulário de contato
    Dado que o navegador "edge" está aberto
    Quando eu preencher os dados no formulário de contato
    Então devo ver o formulário carregado
    E devo submeter o formulário
