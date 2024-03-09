*** Criando ambiente virtual no Python *** 
Utilize o Powersheel para ter resultados equivalente ao passos a seguir:

Criando ambiente virtual de nome aws-price
````
python -m venv aws-price
````

Abrindo pelo powersheel o ambiente virtual criado:
liberar o acesso com o comando:

````
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
````

Após habilitar executar o comando abaixo, ative o ambiente virtual:
````
.\aws-price\Scripts\activate
````

Caso queira desativar execute:
deactivate

para listar os ambientes virtuais dentro do seu computador digite:
````
Get-ChildItem
````

Caso queira trocar de ambiente virtual, navegar entre um ou outro, desative o atual com o comando
````
deactivate
````
E após isso entre no ambiente virtual que deseja usando:
````
.\aws-price\Scripts\activate
````
aonde aws-price é o nome do ambiente virtual que foi criado.


*** Iniciando configuração projeto AWS ***

instale a dependencia:
````
pip install boto3
````

*** listar as dependencias do projeto ***
verifique se existe apenas a dependencia instalada, já que está em um ambiente virtual ela deverá aparecer na listagem
de maneira solitária na sua listagem, para listar as dependencias do seu ambiente virtuão digite o comando:

````
pip freeze

````


Na linha listagem foi apresentada a seguinte sequencia de dependencias:

````
boto3==1.34.59
botocore==1.34.59
jmespath==1.0.1
python-dateutil==2.9.0.post0
s3transfer==0.10.0
six==1.16.0
urllib3==2.0.7

````

*** Criando o arquivo requirements na raiz do projeto automáticamente. ***
Apos instalar as dependencias necessárias, digite o comando a seguir para gerar um arquivo de requeriments.txt
que seria a lista de dependencias do projeto, esse arquivo ficará na raiz do seu projeto python.

````
pip freeze > requirements.txt
````

Atente-se a estar dentro de um ambiente virtual antes de criar o arquivo requiriments.txt
para pegar apenas as dependencias vinculadas ao projeto.


*** Ignorando erros do console no boto3 ***
crie na raiz do projeto um arquivo chamado mypy.ini
adicione dentro o arquivo as seguintes informações:

````
[mypy-boto3.*]
ignore_missing_imports = True

````
Salve o arquivo

*** Configurando o AWS no windows ***

Siga o manual da AWS no link:
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

Ou você pode ir direto ao ponto seguindo os passo abaixo:

Na pasta: C:\Users\PC\.aws
coloque os arquivos, eles não contém extensão:
---> credentials
---> config

Aonde credentials tem dentro dele:

````
[default]
aws_access_key_id = chave que não iremos dispor aqui!
aws_secret_access_key = chave de acesso que não iremos dispor aqui!
````

E config tem dentro dele:

````
[default]
region=us-east-1
````

*** Executando o progama ***
Para iniciar o programa no visual studio code pressione: 
````
F5
````
E ative o modo debug, é necessário estar dentro o arquivo main.py


*** Nota IMPORTANTE!!! ***
No momento atual o projeto está buscando a lista corretamente na AWS porém 
ele da erro ao listar na tela os dados, será necessário criar novas features 
para arrumar esse bug do projeto, caso queira visualizar os dados coloque um breakpoint
antes da conversão do response para colher os dados em tempo de execução.


*** Features previstas ***
Tratar os dados atuais em um DTO normalizado (Contrato de recebimento de dados) de acordo 
com o que é esperado pelo time e verificar se todos estão de acordo com o contrato.


Criar lógica de calculadora de price para que todos possam calcular o price da AWS de maneira simples
verificar a possibilidade de guardar as requisições em um REDIS para que a latencia de consulta não seja 
constante, criar uma lógica que não busque toda vez os dados na fonte da AWS.
