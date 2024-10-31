---
title: Extraer Texto de PDF usando Python
linktitle: Extraer Texto de PDF
type: docs
weight: 10
url: /python-cpp/extract-text/
description: Esta sección describe cómo extraer texto de un documento PDF usando la biblioteca de Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer Texto de todas las Páginas del Documento PDF

Extraer texto de un PDF no es fácil. No muchos lectores de PDF pueden extraer texto de imágenes PDF o PDFs escaneados. Pero la herramienta **Aspose.PDF para Python vía C++** te permite extraer texto fácilmente de cualquier archivo PDF.

Consulta el fragmento de código y sigue los pasos para extraer texto de tu PDF:

1. Importa la biblioteca Aspose.PDF para Python
1. Crea un nuevo objeto extractor, que se utiliza para extraer texto e imágenes de documentos PDF.
1. Vincula el objeto extractor a un archivo PDF, que es la fuente de la extracción.
1. Extrae todo el texto del documento PDF y colócalo en alguna variable.

1. Haz lo que sea, imprime el texto extraído en la consola, busca algunos fragmentos, etc.

```python
from AsposePdfPython import *

extactor = Extract()
extractor_bind_pdf(extactor,"blank_pdf_document.pdf")
text = extractor_extract_text(extactor)

print(text)
```