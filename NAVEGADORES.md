# 🌐 Guia de Alternância de Navegadores

Todos os projetos de automação suportam **Safari**, **Edge** e **Firefox**. Você pode alternar facilmente entre eles de duas formas:

## 📝 Método 1: Alterar no arquivo .feature (Recomendado)

Edite o arquivo `.feature` do projeto desejado e altere a linha do step:

### automation_1 (Busca no Google)
Edite `automation_1/features/buscar_site.feature`:
```gherkin
Dado que o navegador "edge" está aberto
```

### automation_2 (WhatsApp Web)
Edite `automation_2/features/enviar_whatsapp.feature`:
```gherkin
Dado que o navegador "safari" está aberto
```

**Navegadores disponíveis:**
- `"safari"` - Safari
- `"edge"` - Microsoft Edge  
- `"firefox"` - Firefox

**Exemplos:**
```gherkin
Dado que o navegador "safari" está aberto
Dado que o navegador "edge" está aberto
Dado que o navegador "firefox" está aberto
```

## 🔧 Método 2: Variável de Ambiente

Defina a variável de ambiente `BROWSER` antes de executar:

### automation_1 (padrão: edge)
```bash
cd automation_1
python3 -m behave                    # Edge (padrão)
BROWSER=safari python3 -m behave     # Safari
BROWSER=firefox python3 -m behave    # Firefox
```

### automation_2 (padrão: safari)
```bash
cd automation_2
python3 -m behave                    # Safari (padrão)
BROWSER=edge python3 -m behave       # Edge
BROWSER=firefox python3 -m behave     # Firefox
```

## ⚙️ Requisitos por Navegador

### Safari
- ✅ Já vem instalado no macOS
- ⚠️ **Requer**: Habilitar "Allow Remote Automation" em Safari > Desenvolver
  - Abra Safari > Preferências (Cmd + ,)
  - Aba **Avançado** > Marque "Mostrar menu Desenvolver"
  - Menu **Desenvolver** > Marque "Permitir Automação Remota"
  - Reinicie o Safari

### Edge
- ✅ Já vem instalado no macOS/Windows
- ✅ Funciona automaticamente (Selenium gerencia o driver)

### Firefox
- ⚠️ **Requer**: Instalar Firefox
- ⚠️ **Requer**: Instalar geckodriver (geralmente gerenciado pelo Selenium 4.x)

## 🚀 Exemplos de Uso Completos

### automation_1 - Testar no Edge:
```bash
cd automation_1
python3 -m behave
```

### automation_1 - Testar no Safari:
```bash
cd automation_1
BROWSER=safari python3 -m behave
```

### automation_2 - Testar no Safari:
```bash
cd automation_2
python3 -m behave
```

### automation_2 - Testar no Edge:
```bash
cd automation_2
BROWSER=edge python3 -m behave
```

## 💡 Dicas

### Testar em múltiplos navegadores

Crie um script para testar em todos os navegadores:

**automation_1:**
```bash
#!/bin/bash
cd automation_1
for browser in safari edge firefox; do
    echo "Testando automation_1 em $browser..."
    BROWSER=$browser python3 -m behave
done
```

**automation_2:**
```bash
#!/bin/bash
cd automation_2
for browser in safari edge firefox; do
    echo "Testando automation_2 em $browser..."
    BROWSER=$browser python3 -m behave
done
```

### Verificar qual navegador está sendo usado

O navegador escolhido será exibido no step do teste:
```
Dado que o navegador "safari" está aberto
```

## 📋 Resumo

| Navegador | Requisitos | Status |
|-----------|------------|--------|
| **Safari** | Habilitar "Allow Remote Automation" | ⚠️ Requer configuração |
| **Edge** | Nenhum | ✅ Pronto para usar |
| **Firefox** | Instalar Firefox | ⚠️ Requer instalação |

## 🔍 Troubleshooting

### Safari não abre
- Verifique se "Allow Remote Automation" está habilitado
- Feche completamente o Safari antes de executar
- Reinicie o Safari após habilitar a opção

### Firefox não abre
- Verifique se o Firefox está instalado
- O Selenium 4.x geralmente gerencia o geckodriver automaticamente
- Se necessário, instale geckodriver manualmente

### Edge não abre
- Verifique se o Edge está atualizado
- O Selenium gerencia o driver automaticamente

