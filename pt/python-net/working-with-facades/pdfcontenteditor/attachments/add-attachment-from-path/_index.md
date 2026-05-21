---
title: Adicionar Anexo a partir do Caminho
type: docs
weight: 20
url: /pt/python-net/add-attachment-from-path/
description: Este exemplo vincula um PDF de entrada, anexa um arquivo externo usando seu caminho de arquivo e salva o PDF modificado com o anexo incorporado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Anexar Arquivos a um PDF usando Sobrecarga de Caminho de Arquivo em Python
Abstract: Este exemplo demonstra como anexar arquivos externos a um documento PDF usando a sobrecarga de caminho de arquivo de 'add_document_attachment()' no Aspose.PDF for Python via the Facades API. Ele simplifica a adição de anexos sem abrir manualmente um fluxo de arquivo.
---

Um PDF pode incluir arquivos incorporados, como documentos, planilhas ou imagens, para referência ou distribuição. A sobrecarga de caminho de arquivo de 'add_document_attachment()' permite adicionar anexos diretamente a partir de um caminho de arquivo, eliminando a necessidade de abrir o arquivo manualmente.

1. Criar o [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular o PDF de entrada.
1. Adicionar o Anexo usando o Caminho de Arquivo.
1. Salvar o Document atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```
