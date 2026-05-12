---
title: Rotar páginas PDF en Python
linktitle: Rotación de páginas PDF
type: docs
weight: 110
url: /es/python-net/rotate-pages/
description: Aprenda cómo rotar páginas PDF y cambiar la orientación de la página en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo rotar páginas en PDF con Python
Abstract: Este artículo ofrece una guía sobre cómo actualizar o cambiar programáticamente la orientación de página de las páginas en un archivo PDF existente utilizando Python. Utilizando Aspose.PDF for Python via .NET, los usuarios pueden cambiar fácilmente entre orientaciones horizontal y vertical ajustando las propiedades MediaBox de la página. El artículo incluye un fragmento de código Python que muestra cómo iterar a través de las páginas de un documento PDF, modificar sus dimensiones y posiciones MediaBox, y ajustar el CropBox si es necesario. Además, explica cómo establecer el ángulo de rotación de las páginas usando el método 'rotate' para lograr la orientación deseada. El proceso concluye guardando el archivo PDF actualizado.
---

Este tema describe cómo actualizar o cambiar la orientación de página de las páginas en un archivo PDF existente programáticamente con Python.

Utilice esta página cuando necesite cambiar las páginas entre orientación vertical y horizontal o aplicar ángulos de rotación al contenido PDF existente.

## Cambiar orientación de página

Esta función rota cada página de un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 grados en sentido horario usando Aspose.PDF for Python.
Es útil para corregir problemas de orientación de página, como documentos escaneados que están de lado. El PDF original permanece sin cambios, y la versión rotada se guarda como un nuevo archivo.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## Temas de página relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Cambiar el tamaño de página del PDF en Python](/pdf/es/python-net/change-page-size/)
- [Recortar páginas PDF en Python](/pdf/es/python-net/crop-pages/)
- [Obtener y establecer propiedades de página PDF en Python](/pdf/es/python-net/get-and-set-page-properties/)