---
title: Adicionar Script de Campo
type: docs
weight: 10
url: /pt/python-net/add-field-script/
description: Formulários PDF interativos podem incluir JavaScript para automatizar ações quando os usuários interagem com os campos de formulário. Usando Aspose.PDF for Python, desenvolvedores podem facilmente anexar scripts a elementos de formulário, como botões ou campos de texto.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Ações JavaScript a Campos de Formulário PDF Usando Python
Abstract: Este artigo explica como abrir um formulário PDF, atribuir código JavaScript a um campo de formulário específico, acrescentar ações de script adicionais e salvar o documento atualizado. O exemplo usa a classe FormEditor da API Aspose.PDF Facades para manipular o comportamento do formulário programaticamente.
---

## Adicionar Ações JavaScript a Campos de Formulário PDF Usando Python

Este trecho de código permite que você adicione ações JavaScript a um campo de formulário PDF existente usando a biblioteca Aspose.PDF for Python. Ele abre um documento PDF, atribui uma ação JavaScript a um campo de formulário e adiciona um script que é executado quando o campo é acionado. Finalmente, o PDF atualizado é salvo como um novo arquivo.
Usando o [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo, você pode anexar programaticamente JavaScript a campos de formulário existentes:

1. Abra um formulário PDF existente.
1. Defina uma ação JavaScript para um campo específico.
1. Anexe outra ação JavaScript ao mesmo campo.
1. Salve o documento PDF modificado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
