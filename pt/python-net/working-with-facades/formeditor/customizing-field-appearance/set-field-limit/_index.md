---
title: Definir Limite de Campo
type: docs
weight: 80
url: /pt/python-net/set-field-limit/
description: Este exemplo mostra como definir um limite máximo de caracteres para um campo de formulário em um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir Limite Máximo de Caracteres para Campos de Formulário PDF Usando Python
Abstract: Este exemplo demonstra a definição do limite de caracteres para um campo chamado "Last Name" com 10 caracteres, garantindo que os usuários não possam inserir mais do que o limite especificado.
---

Campos de formulário em documentos PDF podem exigir restrições de entrada para manter a formatação adequada. Usando Aspose.PDF for Python, os desenvolvedores podem programaticamente definir um número máximo de caracteres para um campo.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) a classe fornece o método 'set_field_limit' para definir o comprimento máximo de entrada para um campo.

1. Abra um formulário PDF existente.
1. Crie um objeto FormEditor.
1. Defina o limite máximo de caracteres para o campo "Last Name".
1. Salve o PDF atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```
