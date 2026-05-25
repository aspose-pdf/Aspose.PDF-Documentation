---
title: Preencher Campos de Código de Barras
type: docs
weight: 50
url: /pt/python-net/fill-barcode-fields/
description: Este exemplo demonstra como preencher programaticamente campos de código de barras em um formulário PDF usando Aspose.PDF for Python via .NET. Ele mostra como vincular um documento PDF, atribuir um valor a um campo de código de barras e salvar o arquivo atualizado.
lastmod: "2026-05-18"
---

Campos de código de barras em formulários PDF permitem que informações codificadas sejam armazenadas e exibidas visualmente como códigos de barras. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada do [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo é usado para acessar os campos do formulário e atribuir um valor de código de barras. Depois que os dados são preenchidos, o PDF é salvo com o conteúdo do código de barras atualizado.

1. Inicialize 'pdf_facades.Form()' para gerenciar interações com formulários PDF.
1. Chame ‘bind_pdf()’ para anexar o PDF que contém campos de código de barras.
1. Use ‘fill_field()’ para atribuir um valor de código de barras.
1. Salve o Document atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```
