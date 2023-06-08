# Manipulação de arquivos, exceções e testes


## Criar e ativar ambiente

```bash
python3 -m venv .venv && source .venv/bin/activate
```

## Instalar dependências

```bash
pip install --no-cache-dir -r dev-requirements.txt
```

### Objetivo

- Extrair dados do arquivo JSON
- Fazer uma análise nos dados extraídos
- Retornar Relatório por string
- Instalar, conhecer e testar o Pytest