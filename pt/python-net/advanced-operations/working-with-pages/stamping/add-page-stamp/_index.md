---
title: Adicionando Selos de Página ao PDF com Python
linktitle: Adicionando Selos de Página
type: docs
weight: 30
url: /pt/python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for Python via .NET permite adicionar Selos de Página ao seu arquivo PDF.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar Selos de Página ao PDF usando Python
Abstract: Este artigo explica como adicionar um selo de página a um documento PDF usando Aspose.PDF para Python. Um selo de página permite sobrepor ou colocar sob o conteúdo — como logotipos, marcas d'água ou anotações — em uma página específica de um PDF. O exemplo mostra como abrir um PDF existente, criar um objeto PdfPageStamp a partir de outra página PDF, configurá-lo como selo de fundo e aplicá-lo a uma página particular. O PDF selado é então salvo como um novo documento. Esta técnica é útil para branding, marca d'água ou para enfatizar conteúdo em nível de página em fluxos de trabalho automatizados de PDF.
---

Aspose.PDF for Python via .NET mostra como aplicar um selo de página (marca d'água ou sobreposição) a uma página específica em um PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). O selo de página pode ser uma página PDF existente usada como camada de fundo ou de primeiro plano (veja [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Isso é útil para adicionar logotipos, marcas d'água ou outro conteúdo de página repetitivo.

1. Abra o documento PDF usando `ap.Document()` (veja [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Crie um objeto `PdfPageStamp` usando a página PDF ou arquivo a ser usado como selo (veja [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Defina as propriedades do selo, por exemplo, `background = True` para posicioná-lo atrás do conteúdo.
1. Adicione o selo a uma página específica usando `document.pages[page_number].add_stamp(page_stamp)` (veja [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) e [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Salve o PDF modificado no arquivo de saída especificado usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

