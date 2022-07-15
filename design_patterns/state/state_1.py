"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    # Context
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()
        print(f'Estado Atual: {self.state}')
        print()

    def approve(self) -> None:
        self.state.approve()
        print(f'Estado Atual: {self.state}')
        print()

    def reject(self) -> None:
        self.state.reject()
        print(f'Estado Atual: {self.state}')
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já Pendente')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento Aprovado')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento Recusado')


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento Pendente')

    def approve(self) -> None:
        print('Pagamento Já foi aprovado')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento Recusado')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Pagamento recusado. Não é possível mover para Pendente')

    def approve(self) -> None:
        print('Pagamento recusado. Não é possível mover para Aprovado')

    def reject(self) -> None:
        print('Pagamento já recusado.')


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
