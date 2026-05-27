---
title: Exportar para JSON
type: docs
weight: 30
url: /pt/python-net/export-to-json/
description: Este exemplo demonstra como exportar valores de campos de formulário PDF para um arquivo JSON usando Aspose.PDF for Python via .NET. Ele explica como carregar um formulário PDF, acessar seus campos através da fachada Form e salvar os dados extraídos em um formato JSON estruturado.
lastmod: "2026-05-18"
---

JSON é um formato de dados amplamente utilizado que permite a troca fluida entre aplicativos e serviços. Neste exemplo, o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto do [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo é usado para vincular um arquivo PDF e exportar seus valores de campos de formulário para uma estrutura JSON legível.

1. Inicialize pdf_facades.Form() para trabalhar com campos de formulário.
1. Use 'bind_pdf()' para anexar o documento PDF de origem.
1. Crie um stream gravável usando 'FileIO()'.
1. Chame 'export_json()' para extrair os valores dos campos de formulário e salvá-los em JSON formatado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```
