---
title: Remover Campo
type: docs
weight: 60
url: /pt/python-net/remove-field/
description: Este exemplo mostra como excluir o campo 'Country' de um formulário PDF usando o método 'remove_field' da classe 'FormEditor'.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover um Campo de Formulário de um Documento PDF Usando Python
Abstract: Este exemplo demonstra como remover um campo de formulário existente de um documento PDF usando Aspose.PDF for Python. O código carrega um arquivo PDF, exclui o campo especificado usando a classe FormEditor e salva o documento atualizado.
---

Formulários PDF podem conter campos que não são mais necessários devido a mudanças de design ou atualizações de fluxo de trabalho. Com Aspose.PDF for Python, os desenvolvedores podem remover facilmente campos de formulário específicos programaticamente.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) A classe em Aspose.PDF fornece o método 'remove_field', que permite aos desenvolvedores excluir um campo de formulário pelo seu nome.

1. Carregue o documento PDF.
1. Crie um objeto FormEditor.
1. Vincule o PDF ao FormEditor.
1. Remova o campo de formulário especificado.
1. Salve o documento atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```
