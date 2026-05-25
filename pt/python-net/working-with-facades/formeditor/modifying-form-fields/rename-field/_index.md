---
title: Renomear Campo
type: docs
weight: 70
url: /pt/python-net/rename-field/
description: Renomeie um campo de formulário existente em um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Renomear um Campo de Formulário PDF Usando Python
Abstract: Este exemplo demonstra como renomear um campo de formulário existente em um documento PDF usando Aspose.PDF for Python. O código abre um PDF de entrada, altera o nome de um campo de formulário especificado usando a classe FormEditor e salva o documento atualizado.
---

Os formulários PDF geralmente dependem dos nomes dos campos para scripts, automação e processamento de dados. Usando Aspose.PDF for Python, os desenvolvedores podem renomear campos existentes sem recriá‑los ou alterar o layout do formulário.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) a classe fornece o método 'rename_field', que permite aos desenvolvedores alterar o nome de um campo existente enquanto preserva sua posição, valor e aparência.

1. Carregue o formulário PDF existente.
1. Crie uma instância de FormEditor.
1. Vincule o documento PDF ao editor.
1. Renomeie o campo alvo.
1. Salve o PDF atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```

