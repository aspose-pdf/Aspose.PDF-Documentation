---
title: Definir metadados PDF
type: docs
weight: 50
url: /pt/python-net/set-pdf-metadata/
description: Modifique e salve metadados em documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atualizando Metadados PDF Usando Aspose.PDF for Python
Abstract: Este guia explica como modificar e salvar metadados em documentos PDF usando Aspose.PDF for Python via .NET. Ele demonstra como atualizar propriedades padrão do PDF, como título, assunto, palavras‑chave e criador, bem como campos de metadados personalizados. Ao final, você será capaz de atualizar programaticamente os metadados do PDF e salvar as alterações.
---

Documentos PDF podem conter tanto metadados padrão (Title, Subject, Keywords, Creator, Author) quanto metadados personalizados armazenados como propriedades XMP. Aspose.PDF fornece uma API simples para modificar essas propriedades em Python. Este guia aborda como atualizar esses campos e salvar o arquivo PDF modificado usando o [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) classe.

1. Carregue o arquivo PDF.
1. Atualizar metadados padrão.
1. Adicionar ou atualizar metadados personalizados.
1. Salvar metadados atualizados.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
