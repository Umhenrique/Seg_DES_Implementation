# Implementação do Algoritmo DES

Este projeto implementa o algoritmo de criptografia DES (Data Encryption Standard) em Python, com uma interface web para facilitar o uso.

## Requisitos

- Python 3.9 ou superior
- Bibliotecas Python:
  - numpy >= 1.26.0
  - bitarray >= 2.8.0
  - pytest >= 7.4.0
  - flask >= 3.0.0

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

### Interface Web

1. Inicie o servidor Flask:
```bash
python app.py
ou
py app.py
```

2. Abra seu navegador e acesse:
```
http://localhost:5000
```

3. Na interface web, você pode:
   - Criptografar texto usando uma chave hexadecimal de 16 caracteres
   - Descriptografar texto cifrado usando a mesma chave

## Testes

Execute os testes unitários:
```bash
pytest test_des.py -v
```

## Características

- Implementação completa do algoritmo DES
- Interface web amigável
- Suporte a mensagens de qualquer tamanho
- Validação de entrada
- Tratamento de erros
- Testes unitários abrangentes

## Estrutura do Projeto

```
.
├── app.py              # Aplicação Flask
├── des.py             # Implementação do DES
├── test_des.py        # Testes unitários
├── requirements.txt   # Dependências
├── templates/         # Templates HTML
│   └── index.html    # Interface web
└── README.md         # Este arquivo
```

No começo, Deus fez o homem
E o homem acha que fez Deus
E no fim, Deus foi morto pelo homem
E o homem agora quer ser Deus
