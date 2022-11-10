from dataclasses import dataclass
import numbers
@dataclass

class Activo:
    idActivo: str
    nombre: str
    cantidad: numbers
    precio: str
    tipo_activo: str
    responsable: str