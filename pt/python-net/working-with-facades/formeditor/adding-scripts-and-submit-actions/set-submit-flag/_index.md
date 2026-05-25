---
title: Definir Sinalizador de Envio
type: docs
weight: 50
url: /pt/python-net/set-submit-flag/
description: Aprenda como definir programaticamente um submit flag para um botão de formulário PDF usando Aspose.PDF for Python. Isso permite que o botão envie os dados do formulário em um formato específico, como XFDF, quando clicado por um usuário.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir Submit Flag para um Botão de Formulário PDF Usando Aspose.PDF for Python
Abstract: Formulários PDF podem ser configurados para enviar dados do formulário a um servidor ou endpoint em diferentes formatos. Ao definir um submit flag em um campo de botão, os desenvolvedores podem definir como os dados são enviados. Este tutorial demonstra como usar a classe FormEditor para definir um submit flag para um botão de envio existente em um documento PDF e salvar o arquivo atualizado.
---

Formulários PDF frequentemente incluem Botões de Envio para enviar a entrada do usuário a um servidor. O submit flag determina o formato de dados enviado (por exemplo, XFDF, FDF, HTML).

1. Vincular um documento PDF.
1. Acesse um botão de envio existente.
1. Defina a flag de envio para o formato desejado.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
