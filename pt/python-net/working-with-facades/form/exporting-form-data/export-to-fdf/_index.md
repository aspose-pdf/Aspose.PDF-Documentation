---
title: Exportar para FDF
type: docs
weight: 10
url: /pt/python-net/export-to-fdf/
description: Este exemplo explica como exportar os dados de campos de formulário PDF para um arquivo FDF (Forms Data Format) usando Aspose.PDF for Python via .NET. Ele demonstra como acessar os dados de formulário interativo através da fachada Form, vincular um documento PDF de origem e salvar os valores extraídos em um fluxo FDF.
lastmod: "2026-05-18"
---

FDF é um formato leve projetado especificamente para armazenar e transferir dados de formulário PDF sem incorporar o documento inteiro. Neste exemplo, um [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto é inicializado a partir do [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo, permitindo que os desenvolvedores interajam com campos AcroForm e exportem seus valores.

1. Crie uma instância de pdf_facades.Form() para trabalhar com campos de formulário PDF.
1. Chame 'bind_pdf()' para anexar o documento PDF que contém o formulário.
1. Use 'open(')' para criar um fluxo binário gravável para o arquivo FDF.
1. Exportar dados do formulário. Chame 'export_fdf()' para extrair e salvar todos os valores dos campos do formulário.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```
