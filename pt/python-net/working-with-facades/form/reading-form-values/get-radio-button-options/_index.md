---
title: Obter opções de botão de rádio
type: docs
weight: 20
url: /pt/python-net/get-radio-button-options/
description: Este artigo demonstra como recuperar o valor atualmente selecionado de um campo de botão de rádio em um documento PDF usando a API Aspose.PDF Facades.
lastmod: "2026-05-18"
---

Os campos de botão de rádio em formulários PDF são controles agrupados onde apenas uma opção pode ser selecionada de cada vez. Cada grupo possui um nome de campo, e cada opção tem um valor correspondente.

1. Criar um objeto Form
1. Vincular o PDF Document
1. Recuperar a opção de botão de rádio selecionada

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```
