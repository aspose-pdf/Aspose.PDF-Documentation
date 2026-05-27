---
title: Excluir Carimbo por Índice
type: docs
weight: 50
url: /pt/python-net/delete-stamp-by-index/
description: Este exemplo cria dois carimbos de borracha na página 2. Em seguida, um carimbo pode ser excluído especificando seu índice.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Excluir um Carimbo de Borracha por Índice em um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como excluir uma anotação de carimbo de borracha em um PDF usando seu índice com Aspose.PDF for Python via the Facades API. Ele mostra como adicionar vários carimbos e depois excluir um deles com base na ordem na página.
---

Quando múltiplos carimbos de borracha existem em uma página, você pode excluir um específico usando seu índice. O método delete_stamp() permite remover anotações de acordo com sua sequência, o que é útil quando você não rastreia IDs de carimbos, mas conhece sua ordem.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Vincule o arquivo PDF de entrada à instância PdfContentEditor usando bind_pdf(infile).
1. Chame 'delete_stamp(1, [2, 3])' para remover o carimbo com índice 1 das páginas 2 e 3.
1. Salve o documento PDF modificado no arquivo de saída usando save(outfile).

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```
