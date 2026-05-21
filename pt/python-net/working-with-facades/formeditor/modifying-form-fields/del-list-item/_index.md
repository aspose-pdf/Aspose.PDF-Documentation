---
title: Excluir item da lista
type: docs
weight: 40
url: /pt/python-net/del-list-item/
description:
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover itens de campos de caixa de lista PDF usando Python
Abstract: Este exemplo demonstra como remover um item de um campo de caixa de lista em um documento PDF usando Aspose.PDF for Python. O código abre um PDF existente, exclui um item específico de um campo de caixa de lista e salva o documento atualizado.
---

Campos de caixa de lista em PDFs permitem que os usuários selecionem uma ou várias opções predefinidas. Usando Aspose.PDF for Python, os desenvolvedores podem remover itens desses campos programaticamente.

Este artigo explica como excluir o item 'UK' de um campo de caixa de lista chamado 'Country', garantindo que o campo contenha apenas as opções desejadas.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) A classe fornece o método 'del_list_item' para remover um item específico de um campo de caixa de lista.

1. Abra um formulário PDF existente.
1. Crie um objeto FormEditor.
1. Vincule o documento PDF ao FormEditor.
1. Excluir o item “UK” da caixa de listagem “Country”.
1. Salve o documento atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```

