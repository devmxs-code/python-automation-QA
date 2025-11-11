# 🚀 Projeto de Automação QA com Behave e Selenium

Projeto de automação de testes web utilizando **Behave** (BDD) e **Selenium WebDriver** para testes end-to-end.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Executando os Testes](#executando-os-testes)
- [Projetos de Automação](#projetos-de-automação)
- [Configuração](#configuração)
- [Melhorias Implementadas](#melhorias-implementadas)

## 🎯 Sobre o Projeto

Este projeto contém dois módulos de automação de testes web:

1. **automation_1**: Teste de busca no Google e acesso ao site do Instituto Joga Junto
2. **automation_2**: Teste de preenchimento e submissão de formulário de contato

Ambos os projetos utilizam a metodologia **BDD (Behavior-Driven Development)** com o framework **Behave**, permitindo que os testes sejam escritos em linguagem natural (Gherkin) e facilmente compreendidos por stakeholders não técnicos.

## 🛠 Tecnologias

- **Python 3.12+**
- **Behave 1.3.3** - Framework BDD para Python
- **Selenium 4.38.0** - Automação de navegadores web
- **Microsoft Edge** - Navegador utilizado para os testes

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.12 ou superior**
- **Microsoft Edge** instalado no sistema
- **EdgeDriver** (geralmente incluído com o Selenium 4.x)

### Verificando a instalação do Python

```bash
python --version
# ou
python3 --version
```

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd pyhon-automation-QA
```

### 2. Crie um ambiente virtual (recomendado)

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Isso instalará:
- `behave==1.3.3`
- `selenium==4.38.0`

## 📁 Estrutura do Projeto

```
pyhon-automation-QA/
│
├── automation_1/                    # Projeto 1: Busca no Google
│   ├── behave.ini                   # Configuração do Behave (específica)
│   └── features/
│       ├── buscar_site.feature      # Cenário BDD em Gherkin
│       └── steps/
│           └── steps_buscar_site.py # Implementação dos steps
│
├── automation_2/                    # Projeto 2: WhatsApp Web
│   ├── behave.ini                   # Configuração do Behave (específica)
│   └── features/
│       ├── enviar_whatsapp.feature  # Cenário BDD em Gherkin
│       └── steps/
│           └── steps_whatsapp.py    # Implementação dos steps
│
├── shared/                          # Módulo compartilhado
│   ├── __init__.py
│   └── browser_config.py           # Configuração do navegador
│
├── requirements.txt                # Dependências do projeto
├── behave.ini                       # Configuração de referência (não usado)
├── .gitignore                      # Arquivos ignorados pelo Git
└── README.md                       # Este arquivo
```

## ▶️ Executando os Testes

⚠️ **IMPORTANTE**: Cada projeto deve ser executado **separadamente**. Cada projeto possui sua própria configuração `behave.ini` para execução independente.

### Executar automation_1 (Busca no Google)

```bash
cd automation_1
behave
```

Ou a partir do diretório raiz (especificando o path):

```bash
behave automation_1/features
```

### Executar automation_2 (WhatsApp Web)

```bash
cd automation_2
behave
```

Ou a partir do diretório raiz (especificando o path):

```bash
behave automation_2/features
```

**⚠️ Nota**: 
- Na primeira execução, será necessário escanear o QR Code do WhatsApp Web manualmente.
- Certifique-se de que o Safari tem "Allow Remote Automation" habilitado nas preferências.

### 🌐 Alternância de Navegadores

Ambos os projetos suportam **Safari**, **Edge** e **Firefox**. Veja o guia completo:
- **[NAVEGADORES.md](NAVEGADORES.md)** - Guia completo de alternância de navegadores

**Exemplo rápido:**
```bash
# Testar no Safari
BROWSER=safari python3 -m behave

# Testar no Edge
BROWSER=edge python3 -m behave

# Testar no Firefox
BROWSER=firefox python3 -m behave
```

### Executar um cenário específico

#### automation_1:
```bash
cd automation_1
behave features/buscar_site.feature
```

#### automation_2:
```bash
cd automation_2
behave features/enviar_whatsapp.feature
```

### Opções úteis do Behave

Execute estas opções dentro do diretório de cada projeto:

```bash
# Executar com formato JSON
cd automation_1
behave --format json

# Executar com tags específicas
behave --tags @smoke

# Executar com mais detalhes
behave --verbose

# Executar e gerar relatório HTML
behave --format html -o reports/report.html
```

## 📝 Projetos de Automação

### 🔍 automation_1: Busca no Google

**Objetivo**: Testar a busca no Google e acesso ao site do Instituto Joga Junto.

**Cenário**:
1. Abre o navegador Microsoft Edge
2. Acessa o Google
3. Realiza uma busca por "Instituto Joga Junto"
4. Clica no primeiro resultado relevante
5. Valida que o site do Instituto foi aberto

**Arquivo**: `automation_1/features/buscar_site.feature`

### 💬 automation_2: Enviar Mensagem no WhatsApp Web

**Objetivo**: Testar o envio de mensagem através do WhatsApp Web usando Safari.

**Cenário**:
1. Abre o navegador Safari
2. Acessa o WhatsApp Web
3. Busca pelo contato desejado
4. Envia uma mensagem
5. Valida que a mensagem foi enviada com sucesso

**Arquivo**: `automation_2/features/enviar_whatsapp.feature`

**⚠️ Configuração Necessária do Safari**:
1. Abra o Safari
2. Vá em **Safari > Preferências** (ou `Cmd + ,`)
3. Clique na aba **Avançado**
4. Marque a opção **"Mostrar menu Desenvolver na barra de menus"**
5. Vá em **Desenvolver > Permitir Automação Remota**
6. Reinicie o Safari

**⚠️ Importante**: É necessário escanear o QR Code manualmente quando o WhatsApp Web abrir pela primeira vez.

## ⚙️ Configuração

### behave.ini

Cada projeto possui seu próprio arquivo `behave.ini` para execução independente:

- `automation_1/behave.ini` - Configuração específica do projeto 1
- `automation_2/behave.ini` - Configuração específica do projeto 2

Ambos compartilham as mesmas configurações padrão:

```ini
[behave]
paths = features
format = pretty
default_timeout = 30
logging_level = INFO
```

O arquivo `behave.ini` na raiz é apenas uma referência e não é usado para execução.

### Módulo Compartilhado

O módulo `shared/browser_config.py` centraliza a configuração do navegador, evitando duplicação de código:

- `create_edge_driver()`: Cria e configura o navegador Edge
- `create_wait()`: Cria instância de WebDriverWait para esperas explícitas

## ✨ Melhorias Implementadas

### ✅ Código

- ✅ **Waits explícitos**: Substituição de `time.sleep()` por `WebDriverWait`
- ✅ **Código compartilhado**: Módulo centralizado para configuração do navegador
- ✅ **Tratamento de exceções**: Try/except em todas as operações críticas
- ✅ **Validações melhoradas**: Verificações mais robustas e específicas
- ✅ **Limpeza de recursos**: Garantia de fechamento do navegador mesmo em caso de erro

### ✅ Infraestrutura

- ✅ **requirements.txt**: Gerenciamento de dependências
- ✅ **.gitignore**: Exclusão de arquivos desnecessários do controle de versão
- ✅ **behave.ini**: Configuração centralizada do Behave
- ✅ **Documentação**: README completo e detalhado

### ✅ Boas Práticas

- ✅ Uso de esperas explícitas em vez de esperas fixas
- ✅ Validações mais específicas e informativas
- ✅ Mensagens de erro descritivas
- ✅ Código limpo e bem documentado

## 🐛 Troubleshooting

### Problema: EdgeDriver não encontrado

**Solução**: O Selenium 4.x gerencia o driver automaticamente. Se houver problemas, verifique se o Microsoft Edge está instalado.

### Problema: Elemento não encontrado

**Solução**: 
- Verifique se o site está acessível
- Aumente o timeout nas configurações
- Verifique se os seletores estão corretos

### Problema: ImportError ao importar módulo shared

**Solução**: Certifique-se de estar executando os testes a partir do diretório correto ou ajuste o `sys.path` nos arquivos de steps.

## 📚 Recursos Adicionais

- [Documentação do Behave](https://behave.readthedocs.io/)
- [Documentação do Selenium](https://www.selenium.dev/documentation/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/)

## 👤 Autor

**Marcelo Xavier**

## 📄 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.

---

**Última atualização**: 2025
