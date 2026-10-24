from .operaciones import suma, resta, multiplicacion, division
from .figuras import area_rectangulo, area_triangulo, area_circulo
from .conversiones import a_binario, a_hexadecimal, a_entero

__all__ = [
    "a_binario",
    "a_entero",
    "a_hexadecimal",
    "area_circulo",
    "area_rectangulo",
    "area_triangulo",
    "division",
    "multiplicacion",
    "resta",
    "suma",
]

__version__ = "1.0"