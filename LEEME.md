# Datálogo Joven — instrucciones para publicación

Subdirección para la Juventud, Secretaría Distrital de Integración Social.

## Qué es

Un sitio web estático de cinco páginas. No necesita base de datos, ni PHP, ni Node, ni ningún proceso del lado del servidor. Se publica copiando esta carpeta tal como está.

## Cómo se publica

Copiar el contenido completo de la carpeta al servidor. La página de entrada es `index.html`.

Funciona en cualquier ruta del dominio, en la raíz o dentro de una subcarpeta, sin tener que ajustar nada: el sitio no tiene rutas absolutas.

## Lo único que no se debe cambiar

**Los nombres de archivos y carpetas.** Las rutas de los 49 documentos y sus portadas están escritas en `data/ecosistema-documentos.js`. Si el gestor de contenido renombra `ecosistema-general`, `enfoque-diferencial` o algún PDF, se caen esos enlaces.

Los nombres ya vienen sin espacios, sin tildes y en minúscula justamente para que ningún servidor tenga que reescribirlos.

## No depende de nada externo

Las tipografías, los iconos, la maquetación de Bootstrap y los logos institucionales del pie están dentro de la carpeta, en `externos/` y en `img/`. El sitio se ve igual aunque el servidor bloquee recursos de terceros o no tenga salida a internet.

Los únicos enlaces que salen a otros sitios son los que el usuario elige abrir: informes de la Secretaría Distrital de Planeación, tableros de la Subdirección y portales de GOV.CO.

## Un dato para revisar antes de cargar

La carpeta pesa 479 MB, casi todo son los PDF del repositorio de documentos. El archivo más grande pesa 83 MB. Si la plataforma tiene un límite por archivo o por cargue, conviene saberlo antes para acordar cómo se sube ese contenido.

## Qué hay en cada carpeta

```
index.html y las otras cuatro páginas
css/            estilos del sitio
js/             comportamiento de la página
data/           el repositorio de documentos en un archivo de datos
externos/       tipografías, iconos y Bootstrap, empaquetados
img/            imágenes y logos
ecosistema-general/    los PDF y sus portadas
enfoque-diferencial/   los PDF y sus portadas
programas/      scripts de Python con los que la Subdirección actualiza el contenido
```

`programas/` no interviene en la publicación: son las herramientas con las que la Subdirección genera los datos antes de entregar una versión nueva.

## Actualizaciones

El contenido lo mantiene la Subdirección para la Juventud. Cada actualización se entrega como la carpeta completa, para reemplazar la anterior.
