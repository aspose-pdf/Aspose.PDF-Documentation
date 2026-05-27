---
title: Excluir Selos Globalmente
type: docs
weight: 60
url: /pt/python-net/delete-stamps-globally/
description: Este exemplo demonstra como excluir anotações de selo de borracha globalmente em todas as páginas de um PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como remover selos por ID sem especificar páginas individuais.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Excluir Selos de Borracha Globalmente em um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como excluir anotações de selo de borracha globalmente em todas as páginas de um PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como remover selos por ID sem especificar páginas individuais.
---

Ao trabalhar com múltiplas páginas, pode ser necessário remover certos selos em todo o documento. Os métodos 'delete_stamp_by_id()' e 'delete_stamp_by_ids()' permitem excluir selos globalmente pelos seus identificadores, eliminando a necessidade de iterar manualmente por cada página.

1. Criar um [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instância.
1. Vincule o documento PDF de entrada.
1. Adicionar selos de borracha a várias páginas.
1. Excluir selos globalmente usando seus IDs.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```
