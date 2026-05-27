---
title: Excluir Carimbo por ID
type: docs
weight: 85
url: /pt/python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Excluir Carimbos de Borracha por IDs Únicos ou Múltiplos em um PDF Usando PdfContentEditor
Abstract: Este exemplo demonstra como remover anotações de carimbos de borracha de um PDF com base em seus IDs exclusivos usando Aspose.PDF for Python via the Facades API. Ele abrange tanto a exclusão por ID único quanto a exclusão por múltiplos IDs.
---

Ao trabalhar com PDFs contendo múltiplos carimbos, muitas vezes é necessário remover carimbos específicos sem afetar os demais. Usando exclusão baseada em ID, você pode controlar precisamente quais carimbos remover:

- `'delete_stamp_by_id(stamp_id, page_number)' – exclui um único carimbo pelo seu ID em uma página específica`
- `'delete_stamp_by_ids(page_number, stamp_ids)' – exclui múltiplos carimbos pelos seus IDs em uma página especificada`

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Adicione dois carimbos de borracha com IDs distintos.
1. Exclua carimbos usando métodos de exclusão de ID único e ID múltiplo.
1. Salve o PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```

