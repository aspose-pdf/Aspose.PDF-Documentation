---
title: Copiar Campo Externo
type: docs
weight: 30
url: /pt/python-net/copy-outer-field/
description: Este exemplo demonstra como copiar um campo de formulário de um documento PDF para outro usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Copiar Campos de Formulário PDF de Outro Documento Usando Python
Abstract: Este artigo explica como criar um novo documento PDF, copiar o campo "First Name" de um PDF fonte para a página 1 nas coordenadas (200, 600) e salvar o documento de destino atualizado.
---

Às vezes, os formulários PDF exigem reutilizar campos de um documento em outro. Usando Aspose.PDF for Python, os desenvolvedores podem copiar programaticamente campos de formulário de um PDF de origem para um PDF de destino.

O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) a classe fornece o método 'copy_outer_field', que copia um campo de um documento de origem para um documento de destino em uma página e coordenadas especificadas.

O código cria um novo PDF (destino), adiciona uma página e, em seguida, copia um campo de um PDF existente (origem) para o documento de destino nas coordenadas especificadas.

1. Crie um novo documento PDF de destino.
1. Adicione pelo menos uma página ao PDF de destino.
1. Salve o documento de destino vazio.
1. Crie um objeto FormEditor e vincule‑o ao PDF de destino.
1. Copie o campo 'First Name' do PDF de origem para a página 1 em (200, 600).
1. Salve o PDF de destino atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Por favor, note:**

A assinatura do método 'copy_outer_field' é a seguinte:

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – o campo que você deseja duplicar.
- 'new_field_name' – o nome do novo campo.
- 'page_number' – a página na qual o novo campo aparecerá.
- x, y – coordenadas nessa página.

O page_number deve ser um número inteiro positivo correspondente a uma página existente no PDF (indexação a partir de 1).

Se você passar um parâmetro negativo, por exemplo:

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

O programa então redefinirá para os parâmetros anteriores.
