---
title: Extraer fuentes de PDF mediante Python
linktitle: Extraer fuentes de PDF
type: docs
weight: 30
url: /es/python-net/extract-fonts-from-pdf/
description: Utilice Aspose.PDF for Python via .NET para extraer todas las fuentes incrustadas de su documento PDF.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer fuentes de PDF usando Python
Abstract: Este artículo explica cómo inspeccionar las fuentes utilizadas en un documento PDF con Aspose.PDF for Python via .NET. Muestra cómo abrir un PDF con la clase Document, llamar a `font_utilities.get_all_fonts()` para obtener los objetos de fuente disponibles y recorrer los resultados para leer los nombres de las fuentes con fines de análisis, auditoría o flujos de trabajo de procesamiento de documentos.
---

Utilice [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para abrir el PDF y llamar a `font_utilities.get_all_fonts()` para recuperar todos los objetos [Font](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) referenciados por el documento. Esto resulta útil para auditar fuentes incrustadas, verificar su disponibilidad antes de la conversión o analizar los recursos del documento.

1. Abra el PDF de origen como un `Document`.
1. Llame a `document.font_utilities.get_all_fonts()` para obtener la colección de fuentes.
1. Recorra los objetos `Font` devueltos.
1. Lea e imprima cada valor de `font.font_name`.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
