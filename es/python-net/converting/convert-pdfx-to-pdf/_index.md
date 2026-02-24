---
title: Convertir PDF/x a formatos PDF en Python
linktitle: Convertir PDF/x a formatos PDF
type: docs
weight: 120
url: /es/python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: Este tema le muestra cómo convertir PDF/x a formatos PDF usando Aspose.PDF para Python a través de .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF/x a formatos PDF
Abstract: El artículo ofrece una guía completa sobre cómo convertir PDF/UA y PDF/A a archivo PDF usando Aspose.PDF para Python.
---

**PDF/x a formato PDF significa la capacidad de convertir PDF/UA y PDF/A a un archivo PDF.**

## Convertir PDF/A a PDF

1. Cargue el documento PDF usando 'ap.Document'.
1. Llame a 'remove_pdfa_compliance()' para eliminar todos los ajustes de cumplimiento y metadatos relacionados con PDF/A.
1. Guarde el PDF resultante en la ruta de salida.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Eliminando el cumplimiento de PDF/UA

Esta función demuestra un proceso de conversión en dos pasos: primero eliminar el cumplimiento de PDF/UA (Accesibilidad Universal), y luego convertir el PDF resultante al formato PDF/A-1B con etiquetado automático para accesibilidad y estructura semántica.

1. Cargue el documento PDF usando 'ap.Document()'.
1. Llame a 'document.remove_pdfa_compliance()' para eliminar cualquier restricción o ajuste de cumplimiento de PDF/A.
1. Guarde el PDF modificado en 'path_outfile'.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
