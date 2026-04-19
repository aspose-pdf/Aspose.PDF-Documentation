---
title: Fusionar archivos PDF en Python
linktitle: Fusionar archivos PDF
type: docs
weight: 50
url: /es/python-net/merge-pdf-documents/
description: Aprenda cómo fusionar varios archivos PDF en un único documento en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Combinar páginas PDF usando Python
Abstract: Este artículo aborda la necesidad común de fusionar varios archivos PDF en un único documento, un proceso valioso para organizar y optimizar el almacenamiento y la compartición de contenido PDF. Explora el uso de Aspose.PDF for Python via .NET para combinar eficientemente archivos PDF, reconociendo que fusionar PDFs en Python puede ser un desafío sin bibliotecas de terceros. El artículo ofrece una guía paso a paso para concatenar archivos PDF: crear un nuevo documento, fusionar los archivos y guardar el documento fusionado. Un fragmento de código muestra la implementación usando Aspose.PDF, destacando la capacidad de la biblioteca para simplificar el proceso de fusión. Además, presenta el Aspose.PDF Merger, una herramienta en línea para fusionar PDFs, que permite a los usuarios explorar la funcionalidad en un entorno web.
---

## Fusionar o combinar varios PDF en un único PDF en Python.

Combinar archivos PDF es una consulta muy popular entre los usuarios Esto puede ser útil cuando tienes varios archivos PDF que deseas compartir o almacenar juntos como un solo documento.

Fusionar archivos PDF puede ayudarte a organizar tus documentos, liberar espacio de almacenamiento en tu PC y compartir varios archivos PDF con otros combinándolos en un solo documento.

Fusionar PDF en Python mediante .NET no es una tarea sencilla sin usar una biblioteca de terceros.
Este artículo muestra cómo combinar varios archivos PDF en un documento PDF único usando Aspose.PDF for Python via .NET. 

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

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) es una aplicación web gratuita en línea que le permite investigar cómo funciona la funcionalidad de fusión de presentaciones.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Temas de documentos relacionados

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Dividir archivos PDF en Python](/pdf/es/python-net/split-document/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)

