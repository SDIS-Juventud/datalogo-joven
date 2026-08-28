# -*- coding: utf-8 -*-
"""Crea en la raiz las paginas de redireccion con los nombres anteriores.

Al mover las paginas a html/ cambiaron sus direcciones. Estos archivos conservan
las direcciones viejas vivas: quien abra un enlace guardado o compartido llega
igual a la pagina, ahora en su ubicacion nueva.
"""
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

repo = Path(__file__).resolve().parent.parent

paginas = {
    "politica-publica-distrital-juventud.html": "Política Pública Distrital de Juventud",
    "sistema-distrital-juventud.html": "Sistema Distrital de Juventud",
    "proyectos-inversion.html": "Proyectos de inversión",
    "ecosistema-juventud.html": "Ecosistema de Juventud",
}

plantilla = """<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="0; url=html/{archivo}">
    <link rel="canonical" href="html/{archivo}">
    <title>{titulo} | Datálogo Joven</title>
  </head>
  <body>
    <p>Esta página se trasladó. Si tu navegador no te lleva solo,
      <a href="html/{archivo}">abre {titulo}</a>.</p>
    <script>location.replace("html/{archivo}" + location.hash);</script>
  </body>
</html>
"""

for archivo, titulo in paginas.items():
    destino = repo / archivo
    destino.write_text(plantilla.format(archivo=archivo, titulo=titulo), encoding="utf-8")
    print("redireccion creada:", archivo, "->", f"html/{archivo}")
