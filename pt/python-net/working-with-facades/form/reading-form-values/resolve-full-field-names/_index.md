---
title: Resolver nomes completos de campos
type: docs
weight: 60
url: /pt/python-net/resolve-full-field-names/
description: Este exemplo demonstra como recuperar os nomes totalmente qualificados dos campos de formulário em um documento PDF usando a API Aspose.PDF Facades.
lastmod: "2026-05-18"
---

Em formulários PDF, os campos podem ser organizados hierarquicamente, especialmente quando subformulários são usados. Cada campo possui um nome curto e um nome totalmente qualificado. O nome totalmente qualificado representa o caminho completo do campo dentro da hierarquia do formulário e é exigido por muitos métodos da API que manipulam ou leem os dados do formulário.

1. Criar um objeto Form
1. Vincular o PDF Document
1. Acesse todos os nomes de campos de formulário.
1. O nome totalmente qualificado de cada campo é resolvido usando get_full_field_name().

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```
