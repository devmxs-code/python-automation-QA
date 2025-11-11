# language: pt
Funcionalidade: Acessar o site do Instituto Joga Junto pelo Google

  Cenário: Usuário realiza a busca e acessa o site com sucesso
    Dado que o navegador "edge" está aberto
    Quando eu pesquisar por "Instituto Joga Junto" no Google
    Então devo ver o site do Instituto aberto com sucesso