---
title: Optimizar, Comprimir o Reducir el Tamaño de PDF en Python
linktitle: Optimizar PDF
type: docs
weight: 30
url: /python-cpp/optimize-pdf/
keywords: "optimizar pdf Python"
description: Optimizar archivo PDF, reducir todas las imágenes, reducir tamaño PDF, Desincrustar fuentes, Eliminar objetos no utilizados con Python.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Un documento PDF a veces puede contener datos adicionales. Reducir el tamaño de un archivo PDF te ayudará a optimizar la transferencia de red y el almacenamiento. Esto es especialmente útil para publicar en páginas web, compartir en redes sociales, enviar por correo electrónico o archivar en almacenamiento. Podemos usar varias técnicas para optimizar el PDF:

- Optimizar el contenido de la página para navegación en línea
- Reducir o comprimir todas las imágenes
- Permitir la reutilización del contenido de la página
- Unir flujos duplicados
- Desincrustar fuentes
- Eliminar objetos no utilizados
- Eliminar campos de formularios aplanados
- Eliminar o aplanar anotaciones

{{% alert color="primary" %}}

 Se puede encontrar una explicación detallada de los métodos de optimización en la página de Visión General de Métodos de Optimización.

{{% /alert %}}

## Optimizar un Documento PDF para la Web

La optimización, o linearización para la Web, se refiere al proceso de hacer un archivo PDF adecuado para la navegación en línea usando un navegador web. Para optimizar un archivo para visualización web:

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```python

    import AsposePDFPythonWrappers as ap

    # La ruta al directorio de documentos.
    dataDir = "..."

    # Abrir documento
    document = ap.Document(dataDir + "OptimizeDocument.pdf")

    # Optimizar para web
    document.optimize()

    dataDir = dataDir + "OptimizeDocument_out.pdf"

    # Guardar documento de salida
    document.Save(dataDir)
```