---
title: Adicionar Anotação de Anexo de Arquivo a partir de Stream
type: docs
weight: 40
url: /pt/python-net/add-file-attachment-annotation-from-stream/
description: O exemplo carrega um PDF, lê um arquivo externo para um stream de memória, adiciona uma anotação de anexo de arquivo na primeira página e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotações de Anexo de Arquivo a um PDF a partir de um Stream em Python
Abstract: Este exemplo demonstra como criar uma anotação de anexo de arquivo em um PDF usando um stream de arquivo com Aspose.PDF for Python via the Facades API. Ele mostra como especificar a posição da anotação, definir uma descrição, incluir um valor de opacidade e salvar o documento modificado.
---

As anotações de anexo de arquivo permitem incorporar arquivos como ícones interativos dentro de uma página de PDF. Usando uma abordagem baseada em stream, você pode anexar arquivos dinamicamente sem depender de um caminho de arquivo físico. Este método também oferece suporte à personalização da aparência da anotação, incluindo opacidade.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Leia o Arquivo de Anexo como um Stream.
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


def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```
