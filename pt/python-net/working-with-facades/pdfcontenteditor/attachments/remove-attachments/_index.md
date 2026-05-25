---
title: Remover Anexos
type: docs
weight: 50
url: /pt/python-net/remove-attachments/
description: Este exemplo vincula um PDF de entrada, exclui todos os anexos e salva o PDF modificado sem nenhum arquivo incorporado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover Todos os Anexos de um PDF Usando Python
Abstract: Este exemplo demonstra como remover todos os anexos de arquivo de um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como vincular um PDF, excluir anexos incorporados e salvar o documento atualizado.
---

Os PDFs podem conter anexos, como documentos, imagens ou outros arquivos. Existem cenários em que você precisa limpar um PDF de todos os anexos por motivos de segurança, privacidade ou distribuição. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode remover programaticamente todos os anexos incorporados em um documento.

1. Crie o objeto PdfContentEditor. 
1. Vincular o PDF de entrada.
1. Excluir todos os anexos.
1. Salvar o Document atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```
