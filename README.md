# desafio-medicar
Projeto de gerenciamento de consultas, agendas e medicos desenvolvido com o intuito de angariar uma vaga no time da empresa Intmed.

O software foi desenvolvido ultilizando tecnologias REST portanto tem seu backend e frontand independentes. 
O backend pode ser encontrado na pasta backend e se trata de uma API desenvolvida em Python, usando entre outras as bibliotecas do Django e DjangoRestFramework para facilitar seu desenvolvimento.
Já o frontend que pode ser encontrado na pasta frontend foi desenvolviedo em Typescript com o uso mais relevante dos frameworks Angular e da biblioteca Material Angular.

## Getting Started

### Configurando o Backend
Após clonar o repositorio para sua maquina devemos configurar o frontend e backend, para fins desse tutorial estarei pressupondo que você já tem o python e o node instalados caso este não seja o caso instale-os pois estes seram necessarios, começando pelo backend execute os seguintes comando no terminal:

``` 
  #cria o ambiente virtualApos 
  python -m venv env
  
  #ativa o ambiente (Linux)
  source env/bin/activate
  
  # No windows pode ser necessario executar este comando para liberar a execução de arquivos de comandos.
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass    
  #ativa o ambinente (Windows - Powershell) 
  .\env\Scripts\activate
  
  #instale as dependências (Windows - Powershell)
  python -m pip install -r requirements.txt
  
  #instale as dependências (Linux)
  pip install -r requirements.txt
```
### Configurando o Frontend
Após terminar a configuração do ambiente backend e instalação de suas dependências navegue pelo terminal até a pasta frontend que está na raiz do projeto junto com este arquivo de Readme e dentro dela execute o comando npm install para instalação das dependências.

### Iniciando a aplicação
Por ser uma aplicação REST para testar está se faz necessario a execução de dois servidores sendo um frontend e um backend.
Pelo terminal navegue até a pasta backend e nela execute o comando que rodará nosso servidor de teste:


```
Rodando o projeto (Windows - Powershell)
  python .\manage.py runserver
  
Rodando o projeto (Linux)
  python manage.py runserver
  
```

Lembre-se que caso esteja ultilizando o Windows e esteja abrindo está instancia do terminal pela primeira vez pode se fazer necessario a execução do comando Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass.

Agora vamos inciar o servidor frontend, sem fechar o terminal que está rodando nosso servidor backend abra um novo terminal e navegue até o interior da pasta frontend e nela execute o comando npm start.

Tudo pronto com os servidores iniciados e funcionando em seu modo default você poderá acessar nosso frontend digitando no browser o caminho http://localhost:4200/ já para acessar o admin do backend use o endereço http://127.0.0.1:8000/admin/

Caso seja sua primeira vez acessando o admin do backend se faz necessario a criação do superuser que por sua vez tera permiss~eos de acesso para cadastra medicos, agendas e especialidades. para fazer-lo basta executar os seguintes comando no backend con o env do python ativado:

```
Rodando o projeto (Windows - Powershell)
  python manage.py createsuperuser
  
Rodando o projeto (Linux)
  python manage.py createsuperuser
  
```
Em seguida lhe será solicitado que você digite um username, email e senha digite-os e você já estará pronto para usar nosso sistema.