# Como utilizar:
Este este projeto possui dois scripts principais e um auxiliar.

* redis_modules.py - Possui a implementação de métodos que serão utilizados no master e workers;
* redis_master.py - Script que executa o processo principal, que adiciona trabalhos em uma fila, e aguarda os seus resultados. Também conecta-se em um servidor Redis, obrigatório e necessário para controle local ou externo das filas.
* redis_worker.py - Implementa a execução dos trabalhos que estão disponíveis em fila, sendo necessário conexão com o mesmo Redis do processo principal. Pode executar multíplas instâncias deste script localmente ou em diversas máquinas remotas.

## Executar nas maquinas(tanto em worker(s) quanto na master).
```
worker$ cd ~ && git clone https://github.com/fabiosammy/python_redis_multiprocess.git
worker$ sudo apt-get update
worker$ sudo apt-get install python-pip python-redis
worker$ sudo pip install rq
worker$ cd ~/python_redis_multiprocess/
```

#### Verifiquem se o redis esta rodando na maquina master(ou outra exclusiva para tal).
```
master$ docker run --rm --network="host" -p 6379:6379 redis:3.2-alpine
```

#### Agora alterem o arquivo `redis_worker` afim de apontar o serviço redis para o ip da maquina que está executando o serviço redis.
```
worker$ python redis_worker.py
```

#### E por fim, caso estejam rodando o redis na mesma máquida que o master, somente executem o script. Caso contrário, alterem devidamente o script afim de apontar para o ip correto. 
```
master$ python redis_master.py
```

