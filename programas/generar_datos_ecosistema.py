# -*- coding: utf-8 -*-
"""
Genera todo lo que se deriva de data/ecosistema-documentos.json: el archivo .js
que lee la pagina, los contadores de respaldo de la cabecera del Ecosistema y los
dos Indice.xlsx de las carpetas de documentos.

Por que existe este paso: los navegadores bloquean la lectura de un archivo .json
cuando la pagina se abre directamente desde una carpeta (file://). Al dejar los
mismos datos dentro de un .js, el repositorio de documentos tambien se ve cuando
alguien recibe la carpeta y abre el index sin publicarlo.

La fuente que se edita siempre es el .json. Despues de agregar o cambiar una
ficha, correr este script para regenerar el .js:

    python programas/generar_datos_ecosistema.py
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar_indices_excel

raiz = Path(__file__).resolve().parent.parent
ruta_json = raiz / "data" / "ecosistema-documentos.json"
ruta_js = raiz / "data" / "ecosistema-documentos.js"
ruta_html = raiz / "ecosistema-juventud.html"

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

# Los contadores de la cabecera los calcula js/main.js al cargar la pagina. Los
# numeros escritos en el HTML solo se ven mientras el navegador carga los datos,
# pero si se quedan viejos alcanzan a mostrar una cifra equivocada. Se refrescan
# aca para que nadie tenga que acordarse de subirlos a mano.
html = ruta_html.read_text(encoding="utf-8")
for atributo, valor in (("data-ecosistema-total", len(documentos)),
                        ("data-ecosistema-diferencial", diferenciales)):
    html = re.sub(rf"(<strong {atributo}>)\d+(</strong>)", rf"\g<1>{valor}\g<2>", html)
ruta_html.write_text(html, encoding="utf-8")

print(f"{ruta_js.name} generado con {len(documentos)} fichas "
      f"({diferenciales} con enfoque diferencial)")
print(f"{ruta_html.name}: contadores de respaldo en {len(documentos)} y {diferenciales}")

# Los indices en Excel salen del mismo JSON, para que no puedan desfasarse
for linea in generar_indices_excel.generar():
    print(linea)
