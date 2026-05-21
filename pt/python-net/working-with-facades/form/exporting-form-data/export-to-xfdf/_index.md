---
title: Exportar para XFDF
type: docs
weight: 20
url: /pt/python-net/export-to-xfdf/
description: Este exemplo mostra como exportar os dados de campos de formulário PDF para um arquivo XFDF (XML Forms Data Format) usando Aspose.PDF for Python via .NET. Ele demonstra como carregar um formulário PDF, acessar seus campos através da fachada Form e salvar os valores extraídos em um fluxo XFDF.
lastmod: "2026-05-18"
---

XFDF é uma representação XML dos dados de formulário PDF que permite aos desenvolvedores transferir os valores dos campos de formulário independentemente do documento original. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) é usado para vincular o PDF de origem e exportar seus dados para um arquivo XFDF estruturado.

1. Inicialize pdf_facades.Form() para gerenciar os dados de formulário PDF.
1. Chame 'bind_pdf()' para anexar o documento PDF de origem.
1. Use 'open()' para criar um fluxo binário gravável.
1. Exportar Dados do Formulário. Chame 'export_xfdf()' para extrair e salvar os valores dos campos do formulário em formato XFDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```
