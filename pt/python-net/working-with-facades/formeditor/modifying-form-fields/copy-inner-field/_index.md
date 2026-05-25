---
title: Copiar Campo Interno
type: docs
weight: 20
url: /pt/python-net/copy-inner-field/
description: Copiar PDF Form Fields para uma Nova Posição Usando Python com Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Copiar PDF Form Fields para uma Nova Posição Usando Python
Abstract: Este exemplo demonstra como copiar um FormField existente para uma nova posição em um PDF Document usando Aspose.PDF for Python. O código abre um PDF, duplica um FormField para uma página e coordenadas especificadas e salva o Document atualizado.
---

Os formulários PDF geralmente exigem a duplicação de campos mantendo a formatação e o comportamento originais. Usando Aspose.PDF for Python, os desenvolvedores podem copiar um campo existente para uma nova posição na mesma página ou em outra página programaticamente.

Este artigo explica como copiar um campo chamado ‘First Name’ para um novo campo chamado ‘First Name Copy’ na página 2 em coordenadas específicas (x=200, y=600), produzindo um PDF com o campo recém‑posicionado.

1. Abra um formulário PDF existente.
1. Crie um objeto FormEditor.
1. Vincule o documento PDF ao FormEditor.
1. Copie o campo ‘First Name’ para um novo campo ‘First Name Copy’ na página 2 nas coordenadas (200, 600).
1. Salve o documento atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Por favor, note:**

A assinatura do método 'copy_inner_field' é a seguinte:

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – o campo que você deseja duplicar.
- 'new_field_name' – o nome do novo campo.
- 'page_number' – a página na qual o novo campo aparecerá.
- x, y – coordenadas nessa página.

O page_number deve ser um número inteiro positivo correspondente a uma página existente no PDF (indexação a partir de 1).

Se você passar um parâmetro negativo, por exemplo:

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

O programa então redefinirá para os parâmetros anteriores.
