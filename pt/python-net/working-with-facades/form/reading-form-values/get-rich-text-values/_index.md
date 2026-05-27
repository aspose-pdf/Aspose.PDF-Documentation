---
title: Obter Valores de Texto Rico
type: docs
weight: 40
url: /pt/python-net/get-rich-text-values/
description: Esta seção explica como recuperar o conteúdo de texto rico de um campo de formulário em um documento PDF usando a API Aspose.PDF Facades. Ao contrário dos campos de texto simples, os campos de texto rico podem conter conteúdo formatado, como texto em negrito, diferentes fontes, cores e estilo de parágrafo.
lastmod: "2026-05-18"
---

Formulários PDF podem incluir campos de texto que suportam formatação de texto rico. Esses campos podem armazenar conteúdo com atributos de estilo além dos valores de texto simples.

1. Criar um objeto Form
1. Vincular o PDF Document
1. Recuperar Valores de Texto Rico.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```
