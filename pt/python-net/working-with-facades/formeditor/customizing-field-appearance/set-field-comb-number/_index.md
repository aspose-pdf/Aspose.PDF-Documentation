---
title: Definir número de comb do campo
type: docs
weight: 70
url: /pt/python-net/set-field-comb-number/
description: Este exemplo demonstra como definir um número de comb para um campo de formulário PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir número de comb para campos de formulário PDF usando Python
Abstract: Usando Aspose.PDF for Python, os desenvolvedores podem definir programaticamente o número de caixas (número de comb) para um campo de formulário, a fim de impor uma entrada de comprimento fixo. Este artigo demonstra a definição do número de comb para um campo chamado "PIN".
---

O número de comb define como o conteúdo do campo é dividido em caixas igualmente espaçadas, frequentemente usado para códigos PIN, números de série ou outros campos de entrada de comprimento fixo. O código abre um PDF existente, define o número de comb para um campo e salva o documento modificado.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) A classe fornece o método ‘set_field_comb_number’ para definir o número de caixas (caracteres) em um campo de formulário.

1. Abra um formulário PDF existente.
1. Cria um objeto FormEditor.
1. Define o número de comb de um campo chamado "PIN" para 5.
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


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```
