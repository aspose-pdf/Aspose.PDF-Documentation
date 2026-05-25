---
title: Obter Versão do PDF
type: docs
weight: 20
url: /pt/python-net/get-pdf-version/
description: Aprenda como determinar programaticamente a versão de um documento PDF usando Aspose.PDF for Python. Este tutorial demonstra como usar a classe PdfFileInfo para verificar a versão PDF de um arquivo.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar Versão do PDF Usando Aspose.PDF for Python
Abstract: Documentos PDF têm números de versão que indicam os recursos e especificações que suportam (por exemplo, 1.4, 1.7, 2.0). Conhecer a versão do PDF é importante para compatibilidade, suporte a recursos e fluxos de trabalho de processamento de documentos. Neste guia, você aprenderá como recuperar a versão do PDF programaticamente usando a classe PdfFileInfo no Aspose.PDF for Python.
---

As versões de PDF definem os recursos e capacidades suportados em um documento, incluindo campos de formulário, criptografia, anotações e compressão. Para desenvolvedores que trabalham com múltiplos PDFs, verificar a versão garante compatibilidade com ferramentas, bibliotecas ou fluxos de trabalho que processam esses arquivos.

Usando Aspose.PDF for Python, você pode inspecionar facilmente a versão do PDF com o [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) classe.

1. Carregue um documento PDF.
1. Recupere sua versão PDF.
1. Exiba a versão no console.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```
