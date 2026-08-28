# -*- coding: utf-8 -*-
"""
Genera data/ecosistema-documentos.js a partir de data/ecosistema-documentos.json.

Por que existe este paso: los navegadores bloquean la lectura de un archivo .json
cuando la pagina se abre directamente desde una carpeta (file://). Al dejar los
mismos datos dentro de un .js, el repositorio de documentos tambien se ve cuando
alguien recibe la carpeta y abre el index sin publicarlo.

La fuente que se edita siempre es el .json. Despues de agregar o cambiar una
ficha, correr este script para regenerar el .js:

    python programas/generar_datos_ecosistema.py
"""
import json
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
ruta_json = raiz / "data" / "ecosistema-documentos.json"
ruta_js = raiz / "data" / "ecosistema-documentos.js"

documentos = json.loads(ruta_json.read_text(encoding="utf-8"))

contenido = (
    "// Archivo generado por programas/generar_datos_ecosistema.py\n"
    "// No editar a mano: la fuente es data/ecosistema-documentos.json\n"
    "window.ECOSISTEMA_DOCUMENTOS = "
    + json.dumps(documentos, ensure_ascii=False, indent=2)
    + ";\n"
)
ruta_js.write_text(contenido, encoding="utf-8")

diferenciales = sum(1 for d in documentos if d["source"] == "Enfoque diferencial")
print(f"{ruta_js.name} generado con {len(documentos)} fichas "
      f"({diferenciales} con enfoque diferencial)")
