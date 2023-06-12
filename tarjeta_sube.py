class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass

ACTIVADO = 'activado'
PRIMARIO = 'primario'
SECUNDARIO = 'secundario'
UNIVERSITARIO = 'universitario'
JUBILADO = 'jubilado'
DESACTIVADO = 'desactivado'
PRECIO_TICKET = 70


DESCUENTOS = {
    PRIMARIO: 35,
    SECUNDARIO: 42,
    UNIVERSITARIO: 30,
    JUBILADO: 25
}

class Sube():
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO
    
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario is not None:
            return DESCUENTOS.get(self.grupo_beneficiario)
        return PRECIO_TICKET

   
    def pagar_pasaje(self):
        if self.saldo < PRECIO_TICKET and self.grupo_beneficiario == None:
            raise NoHaySaldoException
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException

        if self.grupo_beneficiario is not None:
            self.saldo -=  self.obtener_precio_ticket()
            return self.saldo
        self.saldo -= self.obtener_precio_ticket()
        return self.saldo

    

    def cambiar_estado(self,estado):
        self.estado = estado
        if estado == 'pendiente':
            raise EstadoNoExistenteException

        

