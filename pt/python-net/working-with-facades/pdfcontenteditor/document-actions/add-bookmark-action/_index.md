---
title: Adicionar ação de marcador
type: docs
weight: 10
url: /pt/python-net/add-bookmark-action/
description: Este exemplo vincula um PDF de entrada, cria um marcador rotulado "PdfContentEditor Bookmark" que navega para a página 1 e salva o documento atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um marcador com ação de navegação em um PDF usando Python
Abstract: Este exemplo demonstra como adicionar um marcador com uma ação de navegação a um documento PDF usando Aspose.PDF para Python via a API Facades. Ele mostra como configurar o texto do marcador, a aparência e uma ação que direciona os usuários para uma página específica.
---

Marcadores fornecem navegação rápida dentro de documentos PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode criar marcadores programaticamente e atribuir ações como navegar para uma página. Você também pode personalizar a aparência do marcador, incluindo opções de cor e estilo, como negrito ou itálico.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Definir propriedades do marcador.
1. Atribuir ação ao marcador.
1. Salvar o Document atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```