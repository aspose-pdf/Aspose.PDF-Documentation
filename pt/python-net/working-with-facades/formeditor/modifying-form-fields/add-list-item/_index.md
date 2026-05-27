---
title: Adicionar item à lista
type: docs
weight: 10
url: /pt/python-net/add-list-item/
description: Este exemplo demonstra como adicionar itens a um campo de formulário de caixa de lista em um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar itens aos campos de caixa de lista PDF usando Python
Abstract: Este artigo mostra como abrir um documento PDF, acrescentar itens a um campo de caixa de lista chamado "Country", e salvar o documento atualizado.
---

Os campos de caixa de lista em PDFs permitem que os usuários selecionem uma ou várias opções de um conjunto predefinido. Usando Aspose.PDF for Python, os desenvolvedores podem adicionar programaticamente novos itens a esses campos. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) A classe fornece o método 'add_list_item' para acrescentar itens a um campo de caixa de lista existente.

1. Abra um formulário PDF existente.
1. Crie um objeto FormEditor.
1. Vincule o PDF ao FormEditor.
1. Adicione itens ao campo de caixa de lista "Country".
1. Salve o documento atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```
