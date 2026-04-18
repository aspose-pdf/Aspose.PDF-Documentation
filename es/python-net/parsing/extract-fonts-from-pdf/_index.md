---
title: Extraer fuentes de PDF mediante Python
linktitle: Extraer fuentes de PDF
type: docs
weight: 30
url: /es/python-net/extract-fonts-from-pdf/
description: Utilice la biblioteca Aspose.PDF for Python para extraer todas las fuentes incrustadas de su documento PDF.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer fuentes de PDF usando Python
Abstract: Este artículo explica cómo inspeccionar las fuentes utilizadas en un documento PDF con Aspose.PDF for Python. Muestra cómo abrir un PDF con la clase Document, llamar a font_utilities.get_all_fonts() para obtener los objetos de fuente disponibles y recorrer los resultados para leer los nombres de las fuentes para análisis, auditoría o flujos de trabajo de procesamiento de documentos.
---

Usar [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para abrir el PDF y llamar `font_utilities.get_all_fonts()` para obtener todo lo disponible [Font](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) objetos referenciados por el documento. Esto es útil al auditar fuentes incrustadas, comprobar la disponibilidad de fuentes antes de la conversión o analizar los recursos del documento.

1. Abre el PDF de origen como un `Document`.
1. Llamar `document.font_utilities.get_all_fonts()` para obtener la colección de fuentes.
1. Iterar a través de lo devuelto `Font` objetos.
1. Lee e imprime cada `font.font_name` valor.

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
