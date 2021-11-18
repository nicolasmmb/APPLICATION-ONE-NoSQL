

# :scroll: Documentação da API:scroll:

### **Para que a API execute sem erros, é *ESTRITAMENTE NECESSÁRIO* seguir os passos decritos a seguir**.
---
----

## :round_pushpin: Introdução

É necessario que todo o **TIME de DESENVOLVIMENTO** tenha noção do Funcionamento da API e todos os Processos e Requistos estejam Documentados tanto para possíveis Auditorias quanto para o própio entendimento do **TIME**. Essa é uma documentação inicial para suporte ao desenvolvimento da API.

----
----
## :mag_right: Tecnologias

:round_pushpin: Ferramentas e Frameworks Utilizados:

- [VS Code](https://code.visualstudio.com/download) - IDE Utilizada.
- [Python](https://www.python.org/) - Linguagem de Programação
- [FAST-API](https://fastapi.tiangolo.com/) - Framework de Desenvolvimento de APIs com Python.
- [MongoDB](https://www.postgresql.org/) - Banco de dados Não Relacional. 
- [Heroku](https://dashboard.heroku.com/) - Plataforma de Serviços da Amazon - RDS. 
- [Docker](https://www.docker.com/) - plataforma de virtualização de nível de sistema operacional.
- [Git](https://github.com/) - GitHub para controle de versões.





<p align="center">
<img height=64" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" alt="VSCode"/>&nbsp;&nbsp;
<img height=64" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python"/>&nbsp;&nbsp;
<img height=64" src="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg" alt="FastAPI"/>&nbsp;&nbsp; 
<img height=64" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="MongoDB"/>&nbsp;&nbsp;
<img height=64" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/heroku/heroku-original-wordmark.svg" alt="AWS-RDS"/>&nbsp;&nbsp;
<img height=64" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="Git"/>&nbsp;&nbsp;
<img height=64" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" alt="Docker"/>&nbsp;&nbsp;
</p>




----
----
# :rotating_light: Passos :rotating_light:
## Passo 1:
### Instalações
>
>:pushpin: Para utilizar a API será necessário a instalação de alguns **Softwares** :computer::
>>:round_pushpin: Os links estarão em "[Azul]()", como nessa demonstração. Eles irão lhe redirecionar para as páginas dos Softwares que deverão ser instalados.
>>:round_pushpin: Siga os passos a Seguir para a instalação dos recursos necessários para Executar a API:
>>> 1. Instale o [Docker](https://www.docker.com/products/docker-desktop) : **Será utilizado para Iniciar um Container contendo as aplicações necessárias para execussão da API.**
>>> 2. Instale o [Git](https://git-scm.com/downloads) : **Necessário para o controle de versão e integrações e versionamento, além de utilizar o processo de Deploy.**
> - **Obs:** Os procedimentos foram executados em um ambiente **Windows**, caso haja necessidade de execução em outro Sistema Operacional, poderá ocorrer incompatibilidades nos processos descritos.


## Passo 2:
### Clonado o Projeto
> :pushpin: Agora será necessário Clonar o Projeto do Git.
> - Acesse um Diretório, esse diretório será usado futuramente.
> - Abra o console nesse diretório acessado.
> - Copie o código abaixo, cole no console e execute:
>```shell 
> git clone https://github.com/nicolasmmb/APPLICATION-ONE-NoSQL.git
>```
> - **Confirme se o repositório foi clonado com sucesso**.
> 

## Passo 3:
### Acessando o Projeto
> :pushpin: Certifique os passos anteriores fom executados corretamente.
> - Localize o diretório clonado anteriormente.
> - No console aberto com o caminho de execução referente ao diretório clonado, execute o seguinte comando:
>```shell 
>docker-compose up --build -d
>```
> - Logo em seguida o Container com a aplicação deve estar em execução como na imagem a seguir.
>>  ![](https://raw.githubusercontent.com/nicolasmmb/saved-images/main/telponto/CAP1.png) 
> --- 
>


## Passo 4:
### Acessando a Documentação da API
> :pushpin: Para realizar os testes nas rotas, acesse os endereço fornecidos:
>>  [HEROKU -  https://app-one-nosql.herokuapp.com/](https://app-one-nosql.herokuapp.com/)
>
>>  [LOCALHOST - http://localhost:3001/](http://localhost:3001/)
> 1. Os testes poderem ser realizados direto na documentação da API já que foi utilizado o Swagger, porém também é possivel realizar os teste utilizando o Postman ou outros.
>>  ![](https://raw.githubusercontent.com/nicolasmmb/saved-images/main/telponto/CAP2.png) 
> ---
> 
## Passo 5:
### Finalizando
> :pushpin: Se todos os passos anteriores foram seguidos corretamente, a API deve estar em execução nesse momento.
----