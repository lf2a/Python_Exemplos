# Process

Objetos de um Process representam atividades executadas em um processo separado.

O construtor deve sempre ser chamado com argumentos de palavra-chave.

O `group` pode ser sempre ser `None`. 

`target` é o objeto que pode ser chamado pelo método `run()`, pode ser `None`.

`name` é o nome do processo.

`args` é a tupla de argumento para a função de destino.

`kwargs` é um dicionário de argumentos de palavras-chave para a chamada de destino.

`run()`: Método que representa a atividade do processo.

`start()`: Inicia a atividade do processo.

`join([timeout])`: Se o tempo limite opcional do argumento for Nenhum (o padrão), 
o método será bloqueado até que o processo cujo método join () seja chamado seja encerrado. 
Se o tempo limite for um número positivo, ele será bloqueado na maioria dos segundos. 
Observe que o método retornará None se o processo terminar ou se o tempo limite do método expirar. 
Verifique o código de saída do processo para determinar se ele terminou.

Um processo pode ser associado várias vezes.

`name`: O nome do processo.

`is_alive()`: retorna se o processo está ativo.


# Pipes and Queues
Ao usar vários processos, geralmente se usa a passagem de mensagens para comunicação entre processos e evita o uso de primitivas de sincronização, como bloqueios.

`put(obj[, block[, timeout]])`
Coloca o objeto na queue.

`get([block[, timeout]])`
Remove e retorna um item da queue.
