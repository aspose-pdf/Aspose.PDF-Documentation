---
title: Definir Alinhamento Vertical do Campo
type: docs
weight: 40
url: /pt/python-net/set-field-alignment-vertical/
description: Este exemplo demonstra como definir o alinhamento vertical de um campo de formulário em um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir Alinhamento Vertical para Campos de Formulário PDF Usando Python
Abstract: Este artigo explica como abrir um PDF, definir o alinhamento vertical de um campo usando a classe FormEditor e salvar o PDF atualizado. O exemplo define o alinhamento vertical de um campo chamado "First Name" para a parte inferior da área do campo.
---

Os campos de formulário PDF podem conter texto que necessita de alinhamento vertical adequado para uma aparência consistente e profissional. Usando Aspose.PDF for Python, os desenvolvedores podem modificar programaticamente o alinhamento vertical dos campos de formulário.
O alinhamento vertical permite que os desenvolvedores controlem se o texto do campo aparece na parte superior, central ou inferior da caixa delimitadora do campo, melhorando o layout e a legibilidade dos dados do formulário.

Usando o [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe e o [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constantes, os desenvolvedores podem ajustar o alinhamento vertical programaticamente para obter um layout de formulário consistente:

1. Abra um documento PDF existente.
1. Crie um objeto FormEditor.
1. Defina o alinhamento vertical de um campo chamado "First Name" para a parte inferior.
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


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```
