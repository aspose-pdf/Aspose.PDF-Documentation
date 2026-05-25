---
title: Mover Carimbo Por ID
type: docs
weight: 80
url: /pt/python-net/move-stamp-by-id-example/
description: Neste exemplo, um carimbo de borracha é adicionado à página 1 e, em seguida, movido para uma nova posição usando seu ID antes de salvar o documento atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover um Carimbo de Borracha por ID em um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como reposicionar uma anotação de carimbo de borracha existente em um PDF usando Aspose.PDF for Python via a Facades API. Ele mostra como criar um carimbo e, em seguida, movê-lo programaticamente usando seu ID.
---

Depois de adicionar uma anotação de carimbo de borracha a um PDF, pode ser necessário ajustar sua posição. O método 'move_stamp_by_id()' permite realocar um carimbo com base em seu identificador, sem recriá‑lo. Isso é útil em fluxos de trabalho automatizados onde a colocação do carimbo deve ser ajustada dinamicamente.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Adicionar uma anotação de carimbo de borracha.
1. Mova o carimbo usando seu ID.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    
