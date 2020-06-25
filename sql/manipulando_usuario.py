from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

# O valor de retorno de create_engine() é uma instância do Engine e representa a interface
# principal do banco de dados, adaptada por meio de um dialeto que lida com os detalhes
# do banco de dados e da DBAPI em uso. Nesse caso, o dialeto SQLite interpretará instruções
# para o módulo sqlite3 interno do Python.
engine = create_engine('sqlite:///sqlite3.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship('Usuario')

    def __repr__(self):
        return f'Produto <id={self.id}, nome={self.nome}>'


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String, unique=True)
    primeiro_nome = Column(String)
    ultimo_nome = Column(String)
    altura = Column(Float)
    ativo = Column(Boolean, default=True, nullable=True)  # se for false, significa que esta conta foi 'excluida'
    cadastro = Column(DateTime, default=datetime.now(), nullable=True)
    produto = relationship('Produto', back_populates='usuario')

    def nome_completo(self):
        return f'{self.primeiro_nome} {self.ultimo_nome}'

    def __repr__(self):
        return f'Usuario <id={self.id}>'


# Usuario.produto = relationship('Produto', order_by=Produto.id, back_populates='usuario')
Base.metadata.create_all(engine)

# adicionando um novo usuario no banco
novo_usuario = Usuario(usuario='luizfilipy', primeiro_nome='Luiz', ultimo_nome='Filipy', altura=1.89)
session.add(novo_usuario)
print(f'Novo usuario: {novo_usuario}')

# buscando o usuario 'luizfilipy'
luizfilipy = session.query(Usuario).filter_by(usuario='luizfilipy').first()
print(f'Usuario retornado: {luizfilipy}')

print(f'São as mesmas pessoas? {novo_usuario is luizfilipy}')

# atualizando uma informação
luizfilipy.usuario = 'luizf'

# criando usuarios em massa
usuarios = [
    Usuario(usuario='estefanepaula', primeiro_nome='Estephane', ultimo_nome='Paula', altura=1.90),
    Usuario(usuario='msilva', primeiro_nome='Maria', ultimo_nome='Silva', altura=1.59),
    Usuario(usuario='pjose', primeiro_nome='Pedro', ultimo_nome='Jose', altura=1.56),
    Usuario(usuario='annamaria', primeiro_nome='Anna', ultimo_nome='Maria', altura=1.67),
    Usuario(usuario='leticia', primeiro_nome='Fernanda', ultimo_nome='Leticia', altura=1.45),
]
session.add_all(usuarios)
todos_usuarios = session.query(Usuario).all()
print(f'Todos os usuarios do banco: {todos_usuarios}')
print('todos os usernames: %s' % list(map(lambda us: us.usuario, todos_usuarios)))

# ordenando resultado por primeiro nome
ordenando_nome = session.query(Usuario).order_by(Usuario.primeiro_nome)
print('ordenados pelo primeiro nome: %s' % list(map(lambda us: us.primeiro_nome, ordenando_nome)))

# usuarios que não tem a letra 'a' no primeiro nome
# like (nao é case sensitive) | ilike (écase sensitive)
usuario_sem_a = session.query(Usuario).filter(Usuario.ultimo_nome.like('%a%')).count()
print('sem a letra \'a\' no primeiro nome: %s' % usuario_sem_a)

# adicionando produtos
produtos = [
    Produto(nome='Pão', usuario_id=1),
    Produto(nome='Uva', usuario_id=1),
    Produto(nome='Maça', usuario_id=3),
    Produto(nome='Pera', usuario_id=3),
    Produto(nome='Mamão', usuario_id=4),
]
session.add_all(produtos)

# relacionamentos
u = session.query(Usuario).filter_by(id=1).first()
print(u.produto)

msilva = session.query(Usuario).filter_by(id=3).first()
msilva.produto = [produtos[0], produtos[1]] + msilva.produto
print(list(map(lambda p: f'{p.nome} pertence tambem a {p.usuario_id}', msilva.produto)))

# armazenando as informações no banco
# session.commit()
