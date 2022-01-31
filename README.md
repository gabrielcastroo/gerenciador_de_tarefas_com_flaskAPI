![GitHub repo size](https://img.shields.io/github/repo-size/gabrielcastroo/gerenciador_de_tarefas_com_flaskAPI?color=green&style=plastic)

<h2>Gerenciador de Tarefas com Flask API</h2>

Funcionalidades da aplicação

* Criar tasks com conteúdo da task, data de criação e nível de prioridade da tarefa (baixa, média e alta).
* Atualizar tasks já existentes.
* Envio automático de e-mail ao criar ou atualizar uma task alertando o usuário sobre o que foi alterado na tarefa.

Durante o projeto, são utilizadas as seguintes ferramentas:

* Python 3 
* Flask API
* SQL Lite
* Rest API
* Virtualenv
* HTML 5
* CSS 3
* Princípios de Programação Orientada a Objetos.


Para executar o projeto:

1. Instale o `virtualenv`:
```
$ pip install virtualenv
```

2. Abra o terminal na raíz da aplicação e execute:
```
$ virtualenv env
```

3. Depois, execute o seguinte comando:
```
$ .\env\Scripts\activate
```

4. Instale as Dependências necessárias para o projeto com o seguinte comando:
```
$ (env) pip install -r requirements.txt
```

5. Execute o servidor:
```
$ (env) python app.py
```

O Servidor usa a porta 5000 por padrão. você pode mudar isso alterando o seguinte código no arquivo 'app.py':

```python
if __name__ == "__main__":
    app.run(debug=True, port=<porta desejada>)
```
Abaixo, segue o link do projeto implantado no Heroku:
 
```
https://gerenciador-tarefas-flask.herokuapp.com/
```
