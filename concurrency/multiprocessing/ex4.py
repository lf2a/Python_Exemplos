from multiprocessing import Process, Pipe


def get_dados(con):
    con.send([12, False, '', None])
    con.close()


if __name__ == '__main__':
    """ A função Pipe() retorna um par de conexão de objetos conectados por um pipe que por padrão é duplex
    cada objeto de conexão tem os metodos send() e recv().
    Observe que os dados em um canal podem ficar corrompidos se dois processos (ou threads) tentarem ler ou 
    gravar na mesma extremidade do canal ao mesmo tempo. Obviamente, não há risco de corrupção de processos 
    que usam extremidades diferentes do pipe ao mesmo tempo. 
    """
    parent_conn, child_conn = Pipe()
    p = Process(target=get_dados, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
