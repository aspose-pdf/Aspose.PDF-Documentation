---
title: Mover Carimbo Por Índice
type: docs
weight: 90
url: /pt/python-net/move-stamp-by-index/
description: Como reposicionar anotações de carimbo de borracha em um PDF usando seu índice em uma página com Aspose.PDF for Python
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover Carimbos de Borracha em um PDF Usando Posicionamento Baseado em Índice
Abstract: Este exemplo demonstra como reposicionar anotações de carimbo de borracha em um PDF usando seu índice em uma página com Aspose.PDF for Python via a Facades API. Ele destaca a criação de vários carimbos e a preparação deles para operações de movimentação.
---

Na edição de PDF, pode ser necessário ajustar a posição de carimbos de borracha existentes. Este trecho de código mostra como:

- Adicionar Vários Carimbos na Mesma Página
- Prepare-os para reposicionamento usando seu índice
- Opcionalmente, mova um selo especificando sua página, índice e novas coordenadas

O método 'move_stamp(page_number, stamp_index, new_x, new_y)' pode reposicionar selos com precisão.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincule o PDF ao editor.
1. Adicione vários selos de borracha a uma página.
1. Salve o documento antes de executar operações de movimentação.
1. Mover um carimbo específico pelo seu índice.
1. Salve o PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
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
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    
