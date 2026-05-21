---
title: Gerenciar Carimbo por ID
type: docs
weight: 95
url: /pt/python-net/manage-stamp-by-id/
description: Como manipular anotações de carimbo de borracha em um PDF pelos seus IDs exclusivos usando Aspose.PDF for Python
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerenciar Carimbos de Borracha por ID em um PDF usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como manipular anotações de carimbo de borracha em um PDF pelos seus IDs únicos usando Aspose.PDF for Python via a API Facades. Você pode ocultar ou exibir carimbos específicos em determinadas páginas sem afetar outros carimbos.
---

Em PDFs com múltiplos carimbos de borracha, pode ser útil controlar carimbos individuais com base em seu ID. Os métodos 'hide_stamp_by_id()' e 'show_stamp_by_id()' permitem o controle seletivo de visibilidade. Este exemplo mostra como:

- Adicionar múltiplos carimbos com IDs exclusivos
- Ocultar um carimbo em uma página específica
- Mostrar um carimbo em outra página

Ao usar operações baseadas em ID, você evita rastrear carimbos por posição de página ou outros atributos.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Adicionar carimbos de borracha com IDs específicos.
1. Ocultar e mostrar carimbos com base em seus IDs e números de página.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```
