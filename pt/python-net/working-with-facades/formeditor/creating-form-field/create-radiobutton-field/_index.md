---
title: Criar Campo RadioButton
type: docs
weight: 40
url: /pt/python-net/create-radiobutton-field/
description: Aprenda como adicionar programaticamente um campo de formulário de botão de rádio a um documento PDF usando Aspose.PDF for Python. Este exemplo demonstra como criar um grupo de botões de rádio, definir opções selecionáveis e salvar o arquivo PDF atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um Campo de Botão de Rádio em um PDF Usando Aspose.PDF for Python
Abstract: Botões de rádio são comumente usados em formulários PDF para permitir que os usuários selecionem uma opção de um grupo de escolhas predefinido. Neste tutorial, você aprenderá como criar um campo de botão de rádio em um PDF usando a classe FormEditor em Aspose.PDF for Python. O exemplo mostra como definir itens de botão de rádio, definir uma seleção padrão e salvar o documento atualizado.
---

Formulários PDF interativos permitem que os usuários forneçam entrada estruturada diretamente dentro de um documento. Um campo de botão de rádio é útil quando os usuários precisam escolher apenas uma opção entre várias, como selecionar um país, gênero ou preferência.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) A classe fornece métodos para criar diferentes tipos de campos, incluindo caixas de texto, caixas de seleção, caixas de combinação, caixas de lista e botões de rádio.

1. Carregue um documento PDF existente.
1. Defina uma lista de opções de botões de opção.
1. Adicione um campo de botão de opção a uma página específica.
1. Definir um valor selecionado padrão.
1. Salve o documento PDF modificado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
