---
title: Criar Campo ListBox
type: docs
weight: 30
url: /pt/python-net/create-listbox-field/
description: Aprenda como adicionar programaticamente um campo de formulário ListBox a um documento PDF usando Aspose.PDF for Python. Este guia mostra como inserir um campo ListBox, definir itens selecionáveis e salvar o arquivo PDF atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um Campo ListBox em um PDF Usando Aspose.PDF for Python
Abstract: Formulários PDF permitem que os usuários interajam com documentos selecionando opções, inserindo dados e enviando informações digitalmente. Um campo ListBox permite que os usuários escolham um ou vários valores de uma lista visível de opções. Neste tutorial, você aprenderá como criar um campo ListBox em um PDF usando a classe FormEditor em Aspose.PDF for Python e preenchê-lo com itens predefinidos.
---

Formulários PDF são comumente usados para aplicações, pesquisas e documentos de registro. Um campo ListBox exibe várias opções simultaneamente, facilitando para os usuários a revisão e a seleção de itens em uma lista.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) A classe fornece funcionalidade para adicionar diferentes tipos de campos interativos, incluindo elementos ListBox.

1. Carregue um documento PDF existente.
1. Definir uma lista de opções selecionáveis.
1. Adicionar um campo ListBox a uma página específica.
1. Definir um valor selecionado padrão.
1. Salve o documento PDF atualizado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
