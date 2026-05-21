---
title: Obter Nomes de Campos Obrigatórios
type: docs
weight: 30
url: /pt/python-net/get-required-field-names/
description: Este exemplo demonstra como identificar e recuperar os nomes dos campos de formulário obrigatórios em um documento PDF usando a API Aspose.PDF Facades.
lastmod: "2026-05-18"
---

Formulários PDF podem conter campos obrigatórios que os usuários devem preencher antes do envio. Esses campos geralmente são marcados como obrigatórios nas propriedades do formulário.

1. Criar um objeto Form
1. Vincular o PDF Document
1. Acesse todos os nomes de campos usando ‘pdf_form.field_names’.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")
```
