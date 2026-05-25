---
title: Dividir PDF até o final
type: docs
weight: 40
url: /pt/python-net/split-pdf-to-end/
description: Divida um documento PDF de uma página fornecida até a última página usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divida um PDF de uma página específica até o final em Python.
Abstract: Aprenda como dividir um documento PDF a partir de uma página dada até a última página usando Aspose.PDF for Python. Este exemplo demonstra a extração de todas as páginas a partir de uma página especificada para criar um novo arquivo PDF.
---

Dividir um PDF de uma página específica até o final é útil quando você precisa da parte posterior de um documento como um arquivo separado. Usando Aspose.PDF for Python, o método split_to_end da [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe permite que você extraia páginas a partir de qualquer número de página até a última página do documento. Isso é ideal para criar trechos, extrair capítulos ou processar partes de um PDF grande sem editá-lo manualmente.

1. Crie um objeto PdfFileEditor.
1. Dividir PDF a partir de uma página específica até o final.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```
