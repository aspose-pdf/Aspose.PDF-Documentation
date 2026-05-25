---
title: Definir Aparência do Campo
type: docs
weight: 50
url: /pt/python-net/set-field-appearance/
description: Este exemplo demonstra como alterar a aparência visual de um campo de formulário PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir Aparência do Campo de Formulário PDF Usando Python
Abstract: Este artigo explica como abrir um PDF, definir a aparência de um campo de formulário usando a classe FormEditor e salvar o documento atualizado. O exemplo define a aparência de um campo chamado \u0022First Name\u0022 como invisível usando a flag AnnotationFlags.INVISIBLE.
---

Os campos de formulário PDF suportam flags de aparência que controlam visibilidade, capacidade de impressão e interatividade. Usando Aspose.PDF for Python, os desenvolvedores podem modificar programaticamente essas flags para campos de formulário específicos.

Usando o [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe, os desenvolvedores podem modificar essas flags para ocultar, exibir ou personalizar o comportamento dos campos de formulário em um PDF interativo.

1. Abra um documento PDF existente.
1. Crie um objeto FormEditor.
1. Defina a aparência do campo chamado "First Name" como invisível.
1. Salve o documento atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to invisible
    if not form_editor.set_field_appearance(
        "First Name", ap.annotations.AnnotationFlags.INVISIBLE
    ):
        raise Exception(
            "Failed to set field appearance. Field may not support appearance flags."
        )

    # Save updated document
    form_editor.save(outfile)
```
