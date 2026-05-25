---
title: Criar Botão de Envio
type: docs
weight: 50
url: /pt/python-net/create-submit-button/
description: Aprenda como adicionar um Botão de Envio a um documento PDF programaticamente usando Aspose.PDF for Python. Este tutorial demonstra como criar um botão que envia os dados do formulário para uma URL especificada e salva o PDF atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um Botão de Envio em um PDF usando Aspose.PDF for Python
Abstract: Botões de envio em formulários PDF permitem que os usuários enviem os dados do formulário diretamente para um servidor ou endpoint. Neste guia, você aprenderá como adicionar um campo Botão de Envio a um PDF usando a classe FormEditor no Aspose.PDF for Python. O exemplo mostra como configurar o nome, rótulo, URL de destino e posição do botão, e então salvar o documento PDF atualizado.
---

Formulários PDF interativos frequentemente exigem que os usuários enviem suas entradas para processamento, como o envio de resultados de pesquisas, formulários de inscrição ou dados de feedback. Um campo Botão de Envio fornece essa funcionalidade ao vincular o botão a um endpoint da web.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) A classe permite adicionar botões, caixas de seleção, botões de opção, campos de texto e outros controles de formulário.

1. Carregue um documento PDF existente.
1. Adicionar um campo de botão Submit a uma página específica.
1. Definir o rótulo do botão e o URL de envio de destino.
1. Salvar o PDF atualizado com o novo botão.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
