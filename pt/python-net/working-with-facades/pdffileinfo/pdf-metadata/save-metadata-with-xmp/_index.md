---
title: Salvar Metadados com XMP
type: docs
weight: 30
url: /pt/python-net/save-metadata-with-xmp/
description: Salvar metadados PDF usando XMP com Aspose.PDF for Python via .NET
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salvando Metadados PDF com XMP Usando Aspose.PDF for Python
Abstract: Este guia demonstra como salvar metadados PDF usando XMP (Extensible Metadata Platform) com Aspose.PDF for Python via .NET. O XMP garante que tanto os metadados padrão quanto os personalizados sejam incorporados em um formato XML padronizado dentro do PDF, melhorando a compatibilidade entre aplicativos e fluxos de trabalho.
---

Os metadados PDF podem ser armazenados de várias maneiras, e o XMP é o método moderno e padronizado para incorporar metadados dentro de um arquivo PDF. Usando Aspose.PDF, você pode atualizar campos padrão como Título, Assunto, Palavras‑chave e Criador, e então salvá‑los no formato XMP para garantir maior compatibilidade e preparação para o futuro. Este método é recomendado em relação aos métodos legados de armazenamento de metadados.

1. Carregue o arquivo PDF.
1. Defina campos de metadados padrão.
1. Salvar metadados no formato XMP.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```
