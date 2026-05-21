---
title: Definir URL de envio
type: docs
weight: 40
url: /pt/python-net/set-submit-url/
description: Este exemplo demonstra como configurar uma ação de envio para um campo de botão em um formulário PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir uma URL de envio para um botão de formulário PDF usando Python
Abstract: Este artigo explica como abrir um formulário PDF existente, definir uma URL de submissão para um campo de botão usando a classe FormEditor, verificar se a operação tem sucesso e salvar o documento PDF atualizado.
---

Formulários PDF podem ser projetados para enviar seus dados a um servidor web quando um usuário clica em um botão de envio. Usando Aspose.PDF for Python, desenvolvedores podem configurar programaticamente uma ação de envio para campos de formulário.
Ao definir uma URL de envio, o formulário pode enviar os dados inseridos pelo usuário a um servidor quando o botão é clicado. Essa funcionalidade é útil em fluxos de trabalho onde formulários PDF precisam enviar informações para aplicações web, bancos de dados ou serviços de processamento.

Usando o [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Módulo, os desenvolvedores podem atribuir programaticamente um URL de envio a um campo de botão em um formulário PDF existente.

1. Abra um formulário PDF existente.
1. Localize um campo de botão chamado Script_Demo_Button.
1. Atribua um URL onde os dados do formulário serão enviados.
1. Verifique se a ação foi aplicada com sucesso.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```
