---
title: Definir Alinhamento de Campo
type: docs
weight: 30
url: /pt/python-net/set-field-alignment/
description: Este exemplo demonstra como definir o alinhamento de texto de um campo de formulário em um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir Alinhamento de Texto para Campos de Formulário PDF Usando Python
Abstract: Este artigo explica como abrir um documento PDF, definir o alinhamento de um campo específico usando a classe FormEditor e salvar o PDF atualizado. O exemplo define o alinhamento de texto de um campo chamado \u0022First Name\u0022 para centralizado.
---

Os campos de formulário PDF frequentemente requerem alinhamento de texto personalizado para manter um layout consistente e profissional. Usando Aspose.PDF for Python, os desenvolvedores podem definir programaticamente o alinhamento do conteúdo de texto de um campo de formulário\u2019s.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe, em combinação com o [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constants, permite que os desenvolvedores modifiquem o alinhamento dos campos de formulário existentes programaticamente.

1. Abra um documento PDF existente.
1. Crie um objeto FormEditor.
1. Defina o alinhamento de um campo chamado "First Name" para o centro.
1. Salve o documento modificado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```
