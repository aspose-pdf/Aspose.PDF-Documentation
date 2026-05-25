---
title: Excluir Todas as Imagens do PDF
type: docs
weight: 10
url: /pt/python-net/delete-all-images/
description: Excluir todas as imagens de um documento PDF usando Aspose.PDF for Python via a Facades API.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover Todas as Imagens de um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como excluir todas as imagens de um documento PDF usando Aspose.PDF for Python via a Facades API. Ele mostra como vincular um PDF, remover todas as imagens incorporadas e salvar o documento atualizado.
---

Documentos PDF frequentemente contêm imagens para ilustrações, branding ou decoração. Pode haver casos em que você precise remover todas as imagens de um PDF, como reduzir o tamanho do arquivo, proteger conteúdos visuais sensíveis ou preparar uma versão somente de texto.

Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)", você pode remover programaticamente todas as imagens de um PDF, garantindo que o documento contenha apenas conteúdo textual. Este exemplo associa um PDF de entrada, exclui todas as imagens e salva o arquivo modificado."

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Excluir todas as imagens.
1. Salvar o Document atualizado.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```
