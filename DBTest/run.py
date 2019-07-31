try:
    
    import sys
    
    import mysql.connector                # mysql
    from mysql.connector import Error     # mysql
    
    from pymongo import MongoClient       # mongodb
    from pymongo import errors
    
except ImportError as e:
    print('Error: %s' % e)
def MySQL(host_, user_, password_, db_):
    try:
        connection = mysql.connector.connect(host = host_, database = db_, user = user_, password = password_)
    
        if connection.is_connected():
            db_info = connection.get_server_info()
            print('\n## Conectado ao MySQL %s ##\n' % db_info)
            cursor = connection.cursor()
            
            print('\tExecutando Teste \'SELECT VERSION()\'')
            cursor.execute('SELECT VERSION()')
            print('\tTeste executado com sucesso!')
            record = cursor.fetchone()
            print ('\tResultado: %s' % record)
        
    except Error as e:
            if e.errno == 2003:
                print('Erro: Não é possivel estabelecer conexão com o MySQL')

    finally:    
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("\n## Conexão Encerrada ##")

def MongoDB(host_, port_):
    try:
        cliente = MongoClient(host_, port_)
        v = cliente.server_info()['version']
        print('MongoDB %s' % v)
        cliente.close()
    except errors.ConnectionFailure as e:
        print('Não foi possivel estabelecer conexão com o MongoDB')
    
if __name__ == '__main__':
    
    if len(sys.argv) == 0:
        while True:
            db = input('mysql ou mongodb: ')
            if db == 'mysql':
                h = input('host: ')
                d = input('database: ')
                u = input('user: ')
                p = input('password: ')
                
                MySQL(h, u, p, d)
            elif db == 'mongodb':
                h = input('host: ')
                p = int(input('port: '))
            
                MongoDB(h, p)
            elif db == 'q':
                break
            else:
                print('Comando inválido! :(')
    elif len(sys.argv) > 0:
        if sys.argv[1] == 'mysql':
            try:
                MySQL(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            except IndexError:
                MySQL(sys.argv[2], sys.argv[3], '', '')
        elif sys.argv[1] == 'mongo':
            MongoDB(sys.argv[2], int(sys.argv[3]))