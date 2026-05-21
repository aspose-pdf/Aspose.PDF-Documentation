---
title: Mover Campo
type: docs
weight: 50
url: /pt/python-net/move-field/
description: Mover um campo de formulário existente para uma posição diferente em um documento PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover um Campo de Formulário PDF para uma Nova Posição Usando Python
Abstract: Este exemplo demonstra como mover um campo de formulário existente para uma posição diferente em um documento PDF usando Aspose.PDF for Python. O código abre um PDF existente, realoca o campo de formulário especificado para novas coordenadas e salva o documento atualizado.
---

Os formulários PDF frequentemente requerem ajustes de layout após a criação. Usando Aspose.PDF for Python, os desenvolvedores podem mover campos de formulário existentes para uma nova posição sem recriá‑los.

Este exemplo mostra como reposicionar o campo \"Country\" especificando novas coordenadas para sua colocação dentro da página. O [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) classe fornece o método move_field para realocar campos dentro de uma página PDF.

1. Abra o formulário PDF existente.
1. Crie um objeto FormEditor.
1. Vincule o documento PDF ao FormEditor.
1. Mova o campo 'Country' para uma nova posição usando coordenadas.
1. Salve o documento modificado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```
