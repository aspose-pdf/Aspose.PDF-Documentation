---
title: Criar Campo CheckBox
type: docs
weight: 10
url: /pt/python-net/create-checkbox-field/
description: Aprenda como adicionar programaticamente um campo de formulário checkbox a um documento PDF usando Aspose.PDF for Python. Este guia demonstra como usar a classe FormEditor para inserir uma caixa de seleção interativa em um arquivo PDF existente e salvar o documento atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um Campo Checkbox em um PDF usando Aspose.PDF for Python
Abstract: Campos de formulário interativos permitem que os usuários preencham e interajam com documentos PDF digitalmente. Neste tutorial, você aprenderá como adicionar um campo checkbox a um PDF usando a API Aspose.PDF Python. O exemplo mostra como vincular um documento PDF existente, criar um campo de formulário checkbox nas coordenadas especificadas e salvar o arquivo modificado.
---

Formulários PDF são amplamente usados para coletar entradas de usuários em documentos como solicitações, pesquisas e acordos. Um campo checkbox permite que os usuários selecionem ou desmarquem uma opção dentro de um formulário.

Usando Aspose.PDF for Python, os desenvolvedores podem manipular formulários PDF programaticamente. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe fornece métodos para adicionar, editar e gerenciar campos de formulário dentro de um documento PDF.

1. Carregue um arquivo PDF existente.
1. Chame o método 'add_field()' com o parâmetro 'FieldType.CHECK_BOX' para criar a caixa de seleção e especificar sua posição.
1. Defina o nome do campo, a legenda e a posição.
1. Salve o documento PDF atualizado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
