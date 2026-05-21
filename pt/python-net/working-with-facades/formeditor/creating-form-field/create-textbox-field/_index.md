---
title: Criar Campo TextBox
type: docs
weight: 60
url: /pt/python-net/create-textbox-field/
description: Aprenda como adicionar programaticamente campos TextBox a um documento PDF usando Aspose.PDF for Python. Este tutorial mostra como inserir múltiplos campos de texto, definir valores padrão e salvar o documento PDF atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar Campos TextBox em um PDF Usando Aspose.PDF for Python
Abstract: Campos TextBox em formulários PDF permitem que os usuários insiram e editem texto, tornando os documentos interativos e fáceis de usar. Neste tutorial, você aprenderá como criar campos de formulário TextBox em um PDF usando a classe FormEditor no Aspose.PDF for Python. O exemplo demonstra a adição de múltiplos campos, a especificação de valores padrão e a gravação do PDF modificado.
---

Formulários PDF frequentemente exigem entrada de texto dos usuários, como nomes, endereços ou comentários. Campos TextBox habilitam essa funcionalidade ao fornecer campos editáveis diretamente dentro do documento PDF.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) A classe permite adicionar campos de texto, caixas de seleção, botões de opção, caixas de lista, caixas combinadas e botões, facilitando a criação de PDFs interativos.

1. Carregue um documento PDF existente.
1. Adicione vários campos TextBox para entrada do usuário.
1. Defina valores padrão para cada campo.
1. Salve o documento PDF atualizado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
