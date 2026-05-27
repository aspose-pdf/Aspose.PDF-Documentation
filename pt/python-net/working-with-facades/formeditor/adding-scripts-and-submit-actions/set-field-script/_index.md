---
title: Definir Script de Campo
type: docs
weight: 30
url: /pt/python-net/set-field-script/
description: Este trecho de código mostra como atribuir uma ação JavaScript a um campo de formulário em um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir Ações JavaScript para Campos de Formulário PDF Usando Python
Abstract: Este artigo explica como abrir um documento PDF, atribuir código JavaScript a um campo de formulário, atualizar o script usando a classe FormEditor e salvar o arquivo modificado. O exemplo demonstra como scripts existentes podem ser substituídos para modificar o comportamento dos campos de formulário.
---

Formulários PDF interativos frequentemente dependem de JavaScript para realizar tarefas como exibir alertas, validar entradas ou acionar comportamento dinâmico do formulário. Com Aspose.PDF for Python, os desenvolvedores podem gerenciar esses scripts programaticamente.

O exemplo primeiro adiciona uma ação JavaScript ao campo e depois a substitui por outro script usando o \u0027set_field_script\u0027 método. Essa abordagem permite que os desenvolvedores controlem ou atualizem o comportamento interativo dos elementos de formulário PDF, como botões ou campos de entrada.

O campo de formulário usado neste exemplo se chama 'Script_Demo_Button', que normalmente representa um botão que executa o script atribuído quando acionado.

Usando o [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo, os desenvolvedores podem gerenciar programaticamente as ações JavaScript associadas aos campos de formulário:

1. Abra um documento de formulário PDF existente.
1. Adicione uma ação JavaScript a um campo de formulário.
1. Defina (substitua) a ação JavaScript com um novo script.
1. Salve o documento PDF modificado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
