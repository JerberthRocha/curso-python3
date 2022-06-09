import re 

class CalculaIpv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_de_ips(self):
        return self._get_numero_ips()

    @property
    def ip(self):
        return self._ip
        
    @property
    def mascara(self):
        return self._mascara
        
    @property
    def prefixo(self):
        return self._prefixo
        
    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('IP inválido.')
                
        self._ip = valor
        self._ip_em_binario = self._converte_ip_para_binario(valor)

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return
            
        if not self._valida_ip(valor):
            raise ValueError('Máscara inválida')

        self._mascara = valor
        self._mascara_em_binario = self._converte_ip_para_binario(valor)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_em_binario.count('1')

    @prefixo.setter
    def prefixo(self, valor):
        
        if not valor:
            return
        
        if not isinstance(valor, int):
            raise TypeError('Prefixo precisa ser inteiro.')
        
        if valor > 32:
            raise TypeError('Valor precisa ter 32Bits.')
        
        self._prefixo = valor
        self._mascara_em_binario = (valor * '1').ljust(32, '0')

        if not hasattr(self, 'mascara'):
            self.mascara = self._converte_binario_para_ip(self._mascara_em_binario)

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True 

    @staticmethod
    def _converte_ip_para_binario(ip):
        blocos = ip.split('.')
        blocos_em_binarios = [bin(int(x)) [2:].zfill(8) for x in blocos]
        return ''.join(blocos_em_binarios)

    @staticmethod
    def _converte_binario_para_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n+i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)
    
    def _set_broadcast(self):
        qtde_bits_usados_para_hosts = 32 - self.prefixo
        self._broadcast_em_binario = self._ip_em_binario[:self.prefixo] + (qtde_bits_usados_para_hosts * '1')
        self._broadcast = self._converte_binario_para_ip(self._broadcast_em_binario)
        return self._broadcast

    def _set_rede(self):
        qtde_bits_usados_para_hosts = 32 - self.prefixo
        self._rede_em_binario = self._ip_em_binario[:self.prefixo] + (qtde_bits_usados_para_hosts * '0')
        self._rede = self._converte_binario_para_ip(self._rede_em_binario)
        return self._rede
    
    def _get_numero_ips(self):
        return 2 ** (32 - self.prefixo)