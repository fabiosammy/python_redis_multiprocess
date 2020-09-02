from time import sleep
from redis import Redis
from rq import Queue
from redis_modules import print_as_function, soma

if __name__ == "__main__":
  print "Initializing redis master"
  redis_conn = Redis(host='127.0.0.1',port=6379)
  queue_jobs = Queue('fila_de_soma', connection=redis_conn)
  jobs = []
  for i in range(10):
    job = queue_jobs.enqueue(soma, i, 1)
    # sleep(2)
    jobs.append(job)

  for job in jobs:
    print "Trabalhos enfileirados {0}".format(len(queue_jobs))
    while job.result is None:
      print "O trabalho {0} ainda nao foi concluido".format(job.id)
      sleep(2)
    print "O Resultado de {0} com os parametros {1} eh: {2}".format(job.func_name, str(job.args), job.result)
