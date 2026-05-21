---
title: Obter Metadados PDF
type: docs
weight: 20
url: /pt/python-net/get-pdf-metadata/
description: Extrair e exibir metadados de documentos PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperando Metadados PDF Usando Aspose.PDF for Python.
Abstract: Este guia demonstra como extrair e exibir metadados de documentos PDF usando Aspose.PDF for Python. Você aprenderá a acessar propriedades padrão de PDF, como título, autor, palavras‑chave, datas de criação/modificação, bem como campos de metadados personalizados. Além disso, o guia aborda verificações de validade do PDF, criptografia e status de portfólio.
---

Os documentos PDF frequentemente contêm metadados valiosos que descrevem o conteúdo do documento, autoria e permissões. Aspose.PDF fornece uma API conveniente para recuperar tanto propriedades de metadados padrão quanto personalizadas. Este trecho de código mostra como usar o [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) classe para inspecionar arquivos PDF programaticamente, incluindo exemplos passo a passo em Python.

1. Carregue o arquivo PDF.
1. Recuperar metadados padrão.
1. Verificar o status e a segurança do PDF.
1. Recuperar metadados personalizados.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```
