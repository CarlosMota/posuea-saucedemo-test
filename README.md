# posuea-saucedemo-test
Scripts para testar a página saucedemo

## Configuração do ambiente

* Crie um ambiente virtual para isolar as dependências do projeto. Execute o seguinte comando no terminal

```bash
python -m venv venv
```

1. Ative o ambiente virtual
  
    * Ative no Windows

        ```bash
        venv\Scripts\activate
        ```

    * Ative no Linux/Mac
        ```bash
        source venv/bin/activate
        ```

2. Instalação de Dependências:

    * Instale as dependências do projeto usando o seguinte comando:

    ```bash
    python -m pip install -r requirements.txt
    ```

3. Configurações Sensíveis

    As configurações sensíveis, como credenciais de login, não devem ser incluídas diretamente no repositório. Para isso crie um arquivo `config.json` não versionado conforme mostrado abaixo: 


    ```json
    {
        "login_credentials": {
            "username": "",
            "password": ""
        }
    }
    ```

## Estrutura do projeto

O projeto utiliza o padrão POM (Page Object Model) para facilitar a organização e a manutenabilidade dos testes

```plaintext
posuea-saucedemo-test/
|-- pages/
| |-- login_page.py
|-- tests/
| |-- test_login_page.py
|-- requirements.txt
|-- .gitignore
|-- README.md
```

`pages/:` Contém arquivos para cada página ou componente da aplicação.

`tests/:` Armazena os casos de teste.

`requirements.txt:` Lista as dependências do projeto.

`.gitignore:` Define os arquivos/diretórios a serem ignorados pelo Git.