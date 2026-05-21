---
title: Adicionar Anotação de Anexo de Arquivo
type: docs
weight: 30
url: /pt/python-net/add-file-attachment-annotation/
description: O exemplo vincula um PDF de entrada, adiciona uma anotação de anexo de arquivo à primeira página usando o caminho do arquivo e salva o documento atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotações de Anexo de Arquivo a um PDF Usando Python
Abstract: Este exemplo demonstra como criar uma anotação de anexo de arquivo em um PDF usando um caminho de arquivo com Aspose.PDF for Python via a Facades API. Ele mostra como definir a posição da anotação, definir o texto de descrição, escolher um tipo de ícone e salvar o documento modificado.
---

Anotações de anexo de arquivo permitem incorporar arquivos externos como ícones interativos em uma página de PDF. Usando a sobrecarga de caminho de arquivo, você pode anexar arquivos diretamente do disco sem abrir fluxos manualmente. Esse método também permite personalizar o ícone da anotação e fornecer uma descrição para os usuários.

1. Criar o [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular o PDF de entrada.
1. Defina o Retângulo da Anotação.
1. Adicionar a Anotação de Anexo de Arquivo.
1. Salvar o Document atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```
