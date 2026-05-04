---
title: Combinar archivos PDF en Python
linktitle: Combinar archivos PDF
type: docs
weight: 50
url: /python-net/merge-pdf-documents/
description: Aprenda cómo combinar varios archivos PDF en un único documento en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Combinar páginas PDF usando Python
Abstract: Este artículo aborda la necesidad común de combinar varios archivos PDF en un único documento, un proceso valioso para organizar y optimizar el almacenamiento y la compartición de contenido PDF. Explora el uso de Aspose.PDF for Python via .NET para combinar eficientemente archivos PDF, reconociendo que combinar PDFs en Python puede ser un desafío sin bibliotecas de terceros. El artículo brinda una guía paso a paso para concatenar archivos PDF: crear un nuevo documento, combinar los archivos y guardar el documento combinado. Un fragmento de código muestra la implementación usando Aspose.PDF, resaltando la capacidad de la biblioteca para simplificar el proceso de combinación. Además, presenta Aspose.PDF Merger, una herramienta en línea para combinar PDFs, que permite a los usuarios explorar la funcionalidad en un entorno web.
---

## Combinar archivos PDF usando Python y DOM

Para concatenar dos archivos PDF:

1. Crear un Nuevo Documento.
1. Combinar los Archivos PDF
1. Guardar el Documento Combinado

Combinar varios documentos PDF en un solo archivo:

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Ejemplo en vivo

[Aspose.PDF Fusionador](https://products.aspose.app/pdf/merger) es una aplicación web gratuita en línea que le permite investigar cómo funciona la funcionalidad de fusión de presentaciones.

[![Aspose.PDF Fusionador](merger.png)](https://products.aspose.app/pdf/merger)

