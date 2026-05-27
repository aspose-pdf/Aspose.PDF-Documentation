---
title: Adicionar link local
type: docs
weight: 40
url: /pt/python-net/add-local-link/
description: Este exemplo vincula um PDF de entrada, adiciona um link local de cor vermelha na página 1 que aponta para a página 1 e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar um link local a um PDF usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar um link local a um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como criar uma área clicável que navega para outra página dentro do mesmo PDF e salvar o documento atualizado.
---

Links locais em PDFs permitem navegação rápida entre páginas dentro do mesmo documento. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode definir um retângulo clicável que vincula uma página a outra, melhorando a usabilidade e a navegação do documento.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Defina um retângulo para o link local clicável.
1. Especifique a página de origem e a página de destino.
1. Defina a cor do link.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
