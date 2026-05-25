---
title: Criar Campo ComboBox
type: docs
weight: 20
url: /pt/python-net/create-combobox-field/
description: Confira como adicionar programaticamente um campo ComboBox (lista suspensa) a um documento PDF usando Aspose.PDF for Python. Este exemplo demonstra como inserir um campo de formulário ComboBox, adicionar itens selecionáveis e salvar o arquivo PDF atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um Campo ComboBox em um PDF Usando Aspose.PDF for Python
Abstract: Campos de formulário interativos tornam os PDFs mais dinâmicos e fáceis de usar. Um campo ComboBox permite que os usuários selecionem uma opção a partir de uma lista suspensa pré-definida. Neste tutorial, você aprenderá como criar um ComboBox em um PDF usando a classe FormEditor no Aspose.PDF for Python, preenchê-lo com opções e salvar o documento modificado.
---

Formulários PDF são amplamente utilizados para coletar informações estruturadas em documentos digitais, como aplicativos, pesquisas e formulários de registro. Um campo ComboBox oferece uma maneira conveniente para os usuários escolherem entre uma lista de valores pré-definidos, mantendo o formulário compacto e organizado.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) A classe permite criar e gerenciar diferentes tipos de campos, incluindo caixas de texto, caixas de seleção, botões de opção e listas suspensas.

1. Carregue um documento PDF existente.
1. Adicione um campo ComboBox usando o método 'add_field()' e o parâmetro 'FieldType.COMBO_BOX'.
1. Use o método 'add_list_item()' para inserir opções selecionáveis na lista suspensa.
1. Salve o documento PDF atualizado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514
    )
    pdf_form_editor.add_list_item("combobox1", ["Australia", "Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand", "New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
