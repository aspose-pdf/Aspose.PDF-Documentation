---
title: Limpar Metadados do PDF
type: docs
weight: 10
url: /pt/python-net/clear-pdf-metadata/
description: Remova todos os metadados de um documento PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Limpeza de Metadados de PDF Usando Aspose.PDF for Python
Abstract: Este guia explica como remover todos os metadados de um documento PDF usando Aspose.PDF for Python via .NET. Você aprenderá a limpar tanto os campos de metadados padrão quanto os personalizados e a salvar o PDF sanitizado. Isso é útil para privacidade, segurança ou para preparar PDFs para publicação pública.
---

Os PDFs frequentemente contêm metadados como título, autor, palavras‑chave, datas de criação e campos personalizados. Em alguns cenários, você pode querer remover todos os metadados de um PDF, por exemplo antes da distribuição ou arquivamento. Aspose.PDF fornece o método clear_info() para remover facilmente todos os metadados. Após a limpeza, você pode salvar o PDF usando o método save().

1. Carregue o arquivo PDF.
1. Limpar todos os metadados.
1. Salvar o PDF limpo.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
