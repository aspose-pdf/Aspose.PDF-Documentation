---
title: Extraer fuentes de PDF mediante Python
linktitle: Extraer fuentes de PDF
type: docs
weight: 30
url: /es/python-net/extract-fonts-from-pdf/
description: Utilice la biblioteca Aspose.PDF para Python para extraer todas las fuentes incrustadas de su documento PDF.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer fuentes de PDF usando Python
Abstract: Este artículo proporciona orientación sobre cómo extraer todas las fuentes de un documento PDF usando un método específico de la biblioteca Aspose.PDF. Introduce el método `font_utilities.get_all_fonts()` disponible en la clase `Document`, que facilita la obtención de información de fuentes. El artículo incluye un fragmento de código Python que demuestra el proceso, el cual implica importar los módulos necesarios, abrir el documento PDF y recorrer las fuentes para imprimir el nombre de cada fuente. Este enfoque es útil para desarrolladores que necesitan analizar o manipular datos de fuentes dentro de archivos PDF.
---

En caso de que desee obtener todas las fuentes de un documento PDF, puede usar el método 'font_utilities.get_all_fonts()' proporcionado en la clase Document. Por favor, revise el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

