class Pagamento:
    def __init__(self, valor:float, desc:str):
        self.valor = valor
        self.descricao = desc

    def validar_valor(self):
        if self.valor <= 0:
            raise Exception("fail: valor invalido")

    def resumo(self):
        print(f"Pagamento de R$ {self.valor}: {self.descricao}")

    def processar(self):
        pass


class CartaoCredito(Pagamento):
    def __init__(self, valor, desc, num, nome, limite):
        super().__init__(valor, desc)
        self.num = num
        self.nome = nome
        self.limite = limite

    def processar(self):
        if self.valor > self.limite:
            raise ValueError(f"fail: limite insuficiente no cartão {self.num}")

        self.limite -= self.valor

        print(
            f"Pagamento aprovado no cartão {self.nome}. "
            f"Limite restante: {self.limite}"
        )


class Pix(Pagamento):
    def __init__(self, valor, desc, chave, banco):
        super().__init__(valor, desc)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"Pix aprovado via {self.banco} com chave: {self.chave}")


class Boleto(Pagamento):
    def __init__(self, valor, desc, codigo, vencimento):
        super().__init__(valor, desc)
        self.codigo_barras = codigo
        self.vencimento = vencimento

    def processar(self):
        print("Boleto gerado. Aguardando pagamento...")


def processar_pagamento(pagamento: Pagamento):
    try:
        pagamento.validar_valor()
        pagamento.resumo()
        pagamento.processar()
    except Exception as e:
        print(e)

    print("\n")

pagamentos = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
    CartaoCredito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500),
    Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    CartaoCredito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700),  # deve falhar
]


for pagamento in pagamentos:
    processar_pagamento(pagamento)
