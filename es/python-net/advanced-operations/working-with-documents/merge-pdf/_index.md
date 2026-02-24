---
title: Cómo combinar PDF usando Python
linktitle: Combinar archivos PDF
type: docs
weight: 50
url: /es/python-net/merge-pdf-documents/
description: Esta página explica cómo combinar documentos PDF en un solo archivo PDF con Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinar páginas PDF usando Python
Abstract: Este artículo aborda la necesidad común de combinar varios archivos PDF en un solo documento, un proceso valioso para organizar y optimizar el almacenamiento y la compartición de contenido PDF. Explora el uso de Aspose.PDF para Python a través de .NET para combinar eficazmente archivos PDF, reconociendo que combinar PDFs en Python puede ser un desafío sin bibliotecas de terceros. El artículo proporciona una guía paso a paso para concatenar archivos PDF crear un nuevo documento, combinar los archivos y guardar el documento combinado. Un fragmento de código muestra la implementación usando Aspose.PDF, destacando la capacidad de la biblioteca para simplificar el proceso de combinación. Además, presenta Aspose.PDF Merger, una herramienta en línea para combinar PDFs, que permite a los usuarios explorar la funcionalidad en un entorno web.
---

## Combinar o fusionar varios PDF en un solo PDF con Python

Combinar archivos PDF es una consulta muy popular entre los usuarios. Esto puede ser útil cuando tienes varios archivos PDF que deseas compartir o almacenar juntos como un solo documento.

Combinar archivos PDF puede ayudarte a organizar tus documentos, liberar espacio de almacenamiento en tu PC y compartir varios archivos PDF con otros al combinarlos en un solo documento.

Combinar PDF en Python a través de .NET no es una tarea sencilla sin usar una biblioteca de terceros.
Este artículo muestra cómo combinar varios archivos PDF en un solo documento PDF usando Aspose.PDF para Python a través de .NET.

## Combinar archivos PDF usando Python y DOM

Para concatenar dos archivos PDF:

1. Crear un nuevo documento.
1. Combinar los archivos PDF
1. Guardar el documento combinado

Combinar varios documentos PDF en un solo archivo:

```python

    import aspose.pdf as apdf
    import aspose.pydrawing as asdrw
    from io import FileIO
    from os import path

    path_infile1 = path.join(self.dataDir, infile1)
    path_infile2 = path.join(self.dataDir, infile2)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document()
    document.merge(files=[path_infile1, path_infile2])
    document.save(path_outfile)
```

## Ejemplo en vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) es una aplicación web gratuita en línea que te permite investigar cómo funciona la funcionalidad de fusión de presentaciones.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)


