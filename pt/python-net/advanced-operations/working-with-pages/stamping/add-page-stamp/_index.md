---
title: Adicionar Selos de Página ao PDF em Python
linktitle: Adicionando Selos de Página
type: docs
weight: 30
url: /pt/python-net/page-stamps-in-the-pdf-file/
description: Aprenda como adicionar selos de página PDF como sobreposições ou fundos em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar Selos de Página ao PDF usando Python
Abstract: Este artigo explica como adicionar um selo de página a um documento PDF usando Aspose.PDF for Python. Um selo de página permite sobrepor ou subpor conteúdo — como logotipos, marcas d'água ou anotações — a uma página específica em um PDF. O exemplo mostra como abrir um PDF existente, criar um objeto PdfPageStamp a partir de outra página PDF, configurá‑lo como um selo de fundo e aplicá‑lo a uma página em particular. O PDF com selo é então salvo como um novo documento. Esta técnica é útil para branding, marca d'água ou para enfatizar conteúdo ao nível de página em fluxos de trabalho automatizados de PDF.
---

Aspose.PDF for Python via .NET mostra como aplicar um selo de página (marca d'água ou sobreposição) a uma página específica em um PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). O carimbo de página pode ser uma página PDF existente usada como camada de fundo ou de primeiro plano (veja [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Isso é útil para adicionar logotipos, marcas d'água ou outro conteúdo de página repetitivo.

1. Abra o documento PDF usando `ap.Document()` (veja [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Criar um `PdfPageStamp` objeto usando a página PDF ou arquivo a ser usado como selo (ver [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Defina as propriedades do selo, por exemplo, `background = True` para colocá-lo atrás do conteúdo.
1. Adicionar o carimbo a uma página específica usando `document.pages[page_number].add_stamp(page_stamp)` (veja [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) e [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Salve o PDF modificado no arquivo de saída especificado usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

## Tópicos Relacionados de Carimbagem

- [Carimbar páginas PDF em Python](/pdf/pt/python-net/stamping/)
- [Adicionar números de página ao PDF em Python](/pdf/pt/python-net/add-page-number/)
- [Adicionar carimbos de imagem ao PDF em Python](/pdf/pt/python-net/image-stamps-in-pdf-page/)
- [Adicionar carimbos de texto ao PDF em Python](/pdf/pt/python-net/text-stamps-in-the-pdf-file/)