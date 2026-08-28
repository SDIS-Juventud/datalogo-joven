# -*- coding: utf-8 -*-
"""Crea img/patron-blanco.png: el mismo grano de las cabeceras, pero en blanco.

Se parte de patron-header.png, se toma su luminancia y se lleva a un rango
casi blanco, para que la textura se note como papel y no como un color de fondo.
"""
import sys
from pathlib import Path

from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")

repo = Path(__file__).resolve().parent.parent
origen = Image.open(repo / "img" / "patron-header.png").convert("L")

pixeles = list(origen.getdata())
minimo, maximo = min(pixeles), max(pixeles)
rango = max(maximo - minimo, 1)

# El grano se mueve entre 246 y 255: visible al mirar de cerca, invisible como color
claro, oscuro = 255, 246
salida = [
    round(oscuro + (p - minimo) / rango * (claro - oscuro))
    for p in pixeles
]

textura = Image.new("L", origen.size)
textura.putdata(salida)
textura.convert("RGB").save(repo / "img" / "patron-blanco.png", optimize=True)
print("patron-blanco.png", origen.size, "rango original", (minimo, maximo), "->", (oscuro, claro))
