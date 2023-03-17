from dataclasses import dataclass
import numbers
@dataclass

class Activo:
    idActivo: str
    nombre: str
    cantidad: numbers
    precio: numbers
    tipo_activo: str
    responsable: str