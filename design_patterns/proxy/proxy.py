"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List


class IUser(ABC):
    # Subject Inteface

    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):
    # Real Subject
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(1) # simulando requisição
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(1) # simulando requisição
        return [
            {'Rua': 'Av. Brasil', 'numero': 250}
        ]


    def get_all_user_data(self) -> Dict:
        sleep(1) # simulando requisição
        return {
            'cpf': '002.159.235.88',
            'rg': '6790125'
        }

class UserProxy(IUser):
    # Proxy
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser

        # Esses objetos ainda não existem nesse ponto do código
        self._real_user: RealUser
        self._cached_address: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)
        
    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_address'):
            self._cached_address = self._real_user.get_addresses()
        
        return self._cached_address

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        
        return self._all_user_data

if __name__ == '__main__':
    maria = UserProxy('Maria', 'Silva')

    print(maria.firstname)
    print(maria.lastname)

    # 3 segundos para responder
    print(maria.get_all_user_data())
    print(maria.get_addresses())

    # Responde instantaneamente
    for i in range(20):
        print(maria.get_addresses())
