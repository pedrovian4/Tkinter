## Principais comandos para o GIT 



- Iniciará o git dentro do repositório


```
$ git init
```

- Clonar um repositório ``` $git clone <url>```


- Adicionar um repositório local ```$git remote add <nome do repositorio> <path do arquivo> ```
- Adicionar repositorio remoto ``` $git remote add <URL>```

- Ver os arquivos que foram modificados ``` $ git status ``` 
    - Ver em uma linha ``` $ git init --oneline  ```


- Adicionar para uma sessão que pode fazer commmits 
    ``` $git add <nome do arquivo>```
    -  ``` git add .``` para adicionar todos
- Para fazer um commit ``` $ git commit -m "Alterações feitas"```


- Para armazenar em memória sem a sessão commit ```$git stash```
    
- Para atualizar do repositorio princial ```$git pull origin master```


- Para empurar alterações para o repositório principal 

```$ git push <branch>```



- Para alterar um commit 
    - Commit ainda não foi dado push 
        ```$git commit --amend``` E edite o commit no editor de texto 
    - Se o commit ja foi feito o exemplo acima vale no entanto o push deve ser feito como
    ```$git push --force-with-lease```



- Criar um branch 
```$git branch -a <nome do branch>```
    -Ir para o branch
        ```$git checkout <nome do branch> ```
    - Atualizar o branch por outro 
    ```$git rebase <nome do branch> ```