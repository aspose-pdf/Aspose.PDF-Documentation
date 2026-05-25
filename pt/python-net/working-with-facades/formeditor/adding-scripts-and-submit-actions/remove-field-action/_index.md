---
title: Remover Ação de Campo
type: docs
weight: 20
url: /pt/python-net/remove-field-action/
description: Remover JavaScript dos campos de formulário pode ser útil ao modificar formulários PDF interativos, desativar ações previamente atribuídas ou limpar documentos que contêm scripts desnecessários.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover Ações JavaScript de Campos de Formulário PDF Usando Python
Abstract: Usando Aspose.PDF for Python, os desenvolvedores podem remover programaticamente ações JavaScript anexadas a campos de formulário. Este artigo explica como abrir um formulário PDF existente, remover o script associado a um campo específico usando a classe FormEditor, verificar a operação e salvar o documento modificado.
---

Os formulários PDF frequentemente contêm ações JavaScript que são executadas quando os usuários interagem com elementos do formulário, como botões ou campos de entrada. Em alguns casos, esses scripts precisam ser removidos para simplificar o comportamento do formulário, melhorar a segurança ou atualizar a lógica do formulário. Remova uma ação JavaScript de um campo de formulário em um documento PDF usando Aspose.PDF for Python. O código abre um formulário PDF existente, localiza um campo específico, remove sua ação JavaScript associada e salva o documento atualizado como um novo arquivo PDF.

Usando o [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/), você pode remover ações JavaScript de campos específicos em um formulário PDF existente:

1. Abra um formulário PDF existente.
1. Localize um campo de formulário chamado 'Script_Demo_Button'.
1. Remova a ação JavaScript associada a esse campo.
1. Verifique se a remoção foi bem-sucedida.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```
