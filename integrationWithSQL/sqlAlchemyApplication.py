import pprint

from sqlalchemy import Column
from sqlalchemy import select
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(20))
    cpf = Column(String(9), unique=True)
    endereco = Column(String(55), unique=True)
    conta = relationship("Conta", back_populates="cliente")

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome},cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):
    __tablename__ = 'conta'
    id_conta = Column(Integer, primary_key=True, autoincrement=True)
    tipo_conta = Column(String(30), default='Conta corrente')
    agencia = Column(String(30))
    num = Column(Integer, unique=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship("Cliente", back_populates="conta")


engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

with Session(engine) as session:
    Pedro = Cliente(nome="Pedro",
                    cpf="123.456.789-09",
                    endereco="Samambaia Sul",
                    conta=[Conta(tipo_conta="Conta corrente",
                                 agencia="0007",
                                 num="26342-1")])

    Amanda = Cliente(nome="Amanda",
                     cpf="987.654.321-09",
                     endereco="Asa Sul",
                     conta=[Conta(tipo_conta="Conta poupança",
                                  agencia="0003",
                                  num="12345-1/500")]
                     )

    Lucas = Cliente(nome="Lucas",
                    cpf="341.634.312-08",
                    endereco="Taguatinga",
                    conta=[Conta(tipo_conta="Conta corrente",
                                 agencia="0004",
                                 num="72365-1/")])

session.add_all([Pedro, Amanda, Lucas])
session.commit()

stmt_cliente = select(Cliente).where(Cliente.nome.in_(['Pedro', 'Amanda', 'Lucas']))
print('Recuperando clientes a partir de uma condição de filtragem')
for cliente in session.scalars(stmt_cliente):
    print(cliente)

stmt_join = select(Cliente.nome, Cliente.cpf, Conta.num).join_from(Conta, Cliente)
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)
