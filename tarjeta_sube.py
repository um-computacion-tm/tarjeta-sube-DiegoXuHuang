ACTIVADO = 'activado'
PRIMARIO = 'primario'
PRECIO_TICKET = 35

class Sube:
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO
    

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == PRIMARIO:
            return PRECIO_TICKET
        return PRECIO_TICKET
    
    def obetener_precio_ticket_con_grupo_beneficiario(self):
        pass
    
    def pagar_pasaje_con_saldo(self,saldo):
        self.pagar_pasaje -= saldo

    def imposible_pagar_pasaje_sin_saldo(self):
        pass