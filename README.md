# Flask Authentication with Flet Frontend

Este é um projeto simples de autenticação de usuários utilizando **Flask** como back-end e **Flet** como front-end. Ele demonstra como integrar uma API de autenticação baseada em Flask com uma interface de usuário desenvolvida com Flet.

## 📋 Funcionalidades

- Autenticação de usuário com verificação de credenciais.
- Criação de novos usuários com hash de senhas usando **bcrypt**.
- Atualização e exclusão de usuários.
- Uso de **Flask-Login** para gerenciamento de sessões.
- Interface de usuário moderna e responsiva criada com **Flet**.
- Execução em **modo Web** via navegador.

## 🛠️ Tecnologias utilizadas

- **Flask**: Framework web para o back-end.
- **Flask-Login**: Gerenciamento de sessões e autenticação de usuário.
- **SQLAlchemy**: ORM para manipulação do banco de dados.
- **bcrypt**: Para hash de senhas.
- **Flet**: Framework para construção de interfaces de usuário no front-end.
- **MySQL**: Banco de dados relacional (pode ser substituído conforme necessidade).

## 🚀 Como rodar o projeto

### 1. Clonando o repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Instalação das dependências
Primeiro, crie um ambiente virtual para o projeto (opcional, mas recomendado):

python3 -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate  # Windows


Instale todas as dependências necessárias listadas no arquivo requirements.txt:

pip install -r requirements.txt

As principais dependências incluem:

Flask
Flet
SQLAlchemy
bcrypt
Flask-Login
3. Configuração do Banco de Dados
Certifique-se de que o MySQL esteja instalado e rodando. Crie um banco de dados para o projeto e atualize as credenciais no arquivo app.py:

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<usuario>:<senha>@localhost:3306/<nome-do-banco>'


4. Rodando o projeto
Modo Web (Recomendado)
Execute o projeto em modo Web com o comando abaixo. Isso abrirá a interface diretamente no navegador:

flet run app2.py --web


Modo Desktop (Opcional, sujeito a dependências)
Se você desejar rodar o Flet no modo desktop e tiver as dependências do sistema operacional instaladas (como libmpv.so.1), pode rodar o projeto sem a flag --web:

python3 app2.py

Nota: O modo desktop requer que a biblioteca libmpv.so.1 esteja instalada, o que pode causar problemas em alguns sistemas.

5. Acessando o projeto
Se estiver rodando o projeto no modo Web, abra o navegador e acesse o endereço:

http://127.0.0.1:XXXXX

O terminal fornecerá a porta correta (XXXXX) quando o projeto for iniciado.

📝 Estrutura do projeto

.
├── app2.py                # Arquivo principal que integra o back-end e o front-end
├── models/                # Modelos de banco de dados (ex: User)
├── database/              # Configuração do banco de dados e conexão
├── frontend/              # (Se houver) Arquivos relacionados ao front-end Flet
├── requirements.txt       # Arquivo com dependências do projeto
└── README.md              # Documentação do projeto


⚙️ Configuração do ambiente
Banco de Dados: Certifique-se de que o MySQL esteja rodando e o banco de dados esteja configurado corretamente.
Variáveis de Ambiente: Configure a variável de ambiente SECRET_KEY para a segurança da sessão.
🚧 Problemas conhecidos
Modo Desktop: Ao rodar em modo desktop, alguns sistemas podem apresentar o erro relacionado à biblioteca libmpv.so.1. Recomenda-se rodar o projeto no modo Web para evitar esse problema.
🖥️ Testes e desenvolvimento
Se você quiser fazer testes no back-end, utilize ferramentas como Postman para testar as rotas de autenticação diretamente no servidor Flask.

🛡️ Segurança
As senhas dos usuários são hashadas utilizando bcrypt.
Certifique-se de que a variável SECRET_KEY esteja devidamente configurada para manter as sessões seguras.
🖇️ Contribuições
Contribuições são bem-vindas! Se você deseja contribuir com melhorias ou correções, faça um fork do repositório, crie um branch para suas alterações e envie um pull request.

🧑‍💻

Feito com ❤️ por Leonardo Fragoso


### Pontos importantes no README:
- **Instruções de execução**: O modo Web é destacado como a forma recomendada para rodar o projeto, devido às dependências nativas do modo desktop.
- **Instalação**: O passo a passo cobre desde a clonagem do repositório até a execução.
- **Segurança**: Menciona o uso de hashing com `bcrypt` e a importância do `SECRET_KEY`.
- **Problemas conhecidos**: O erro relacionado à `libmpv.so.1` é mencionado para evitar confusões.
- **Contribuições**: Um convite para que outros desenvolvedores contribuam com o projeto.

### Como publicar no GitHub:
1. Crie um repositório no GitHub.
2. Adicione o arquivo `README.md` criado acima no diretório raiz do seu projeto.
3. Adicione e faça o commit dos arquivos no seu repositório Git:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main

