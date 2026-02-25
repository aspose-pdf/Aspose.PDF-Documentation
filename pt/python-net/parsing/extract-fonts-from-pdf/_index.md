---
title: Extrair fontes de PDF via Python
linktitle: Extrair fontes de PDF
type: docs
weight: 30
url: /pt/python-net/extract-fonts-from-pdf/
description: Use a biblioteca Aspose.PDF para Python para extrair todas as fontes incorporadas do seu documento PDF.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair fontes de PDF usando Python
Abstract: Este artigo fornece orientações sobre como extrair todas as fontes de um documento PDF usando um método específico da biblioteca Aspose.PDF. Ele apresenta o método `font_utilities.get_all_fonts()` disponível na classe `Document`, que facilita a obtenção de informações sobre as fontes. O artigo inclui um trecho de código Python demonstrando o processo, que envolve a importação dos módulos necessários, a abertura do documento PDF e a iteração sobre as fontes para imprimir o nome de cada fonte. Essa abordagem é útil para desenvolvedores que precisam analisar ou manipular dados de fontes dentro de arquivos PDF.
---

Caso você queira obter todas as fontes de um documento PDF, pode usar o método 'font_utilities.get_all_fonts()' fornecido na classe Document. Por favor, verifique o trecho de código a seguir para obter todas as fontes de um documento PDF existente:

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

