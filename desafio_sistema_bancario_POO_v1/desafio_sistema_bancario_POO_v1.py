""" Sistema bancario modelado em POO PARTE 1 - Trilha DIO Python """

from abc import ABC, abstractmethod

class Conta():

    def __init__(self,numero:int,cliente):
        self._saldo = 0 # Sempre inicia em 0
        self._numero = numero
        self._agencia = "0001" #Nunca se altera, pois existe 1 ag
        self._cliente = cliente
        self._historico = Historico()
        
    @property # forma correta de acesso de variaveis privadas
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls,cliente,numero:int):
        return cls(numero,cliente) #retorna uma instancia de conta

    def sacar(self,valor:float) -> bool:
        saldo = self.saldo
        # TODO Falta implementar a logica

    def depositar(self,valor:float) -> bool:
        self.saldo =+ valor
        # TODO Falta implementar a logica

class ContaCorrent(Conta):
    def __init__(self, numero: int, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self,valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes 
            if transacao["tipo"]== Saque.__name__]
        )
        exedeu_limite = valor > self.limite
        exedeu_saques = numero_saques >= self.limite_saques
        if exedeu_limite:
            print("Valor do saque exedeu limite")
        elif exedeu_saques:
            print("Numero maximo de saques atingido")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
                Ag.: {self.agencia}
                C.C.: {self.numero}
                Titular: {self.cliente.nome}
            """

class Historico():
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao,id_transacao=1):
        self._id =+ id_transacao
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "id": f"{self._id}" 
            }
        )

class Cliente():

    def __init__(self,endereco:str):
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self,nome:str, data_nascimento:str, cpf:str, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod 
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def depositar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)