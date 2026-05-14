---
title: Добавить аннотацию вложения файла из потока
type: docs
weight: 40
url: /python-net/add-file-attachment-annotation-from-stream/
description: В примере загружается PDF, читается внешний файл в поток памяти, добавляется аннотация вложения файла на первую страницу и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотации вложения файлов в PDF из потока на Python
Abstract: Этот пример демонстрирует, как создать аннотацию вложения файла в PDF, используя поток файла с Aspose.PDF for Python via the Facades API. Он показывает, как указать позицию аннотации, задать описание, включить значение непрозрачности и сохранить изменённый документ.
---

Аннотации вложения файлов позволяют встраивать файлы в виде интерактивных значков на странице PDF. При использовании потокового подхода вы можете динамически прикреплять файлы без привязки к физическому пути файла. Этот метод также поддерживает настройку внешнего вида аннотации, включая непрозрачность.

1. Создайте объект PdfContentEditor.
1. Привяжите входной PDF.
1. Прочитайте файл вложения как поток.
1. Добавьте аннотацию вложения файла.
1. Сохраните обновлённый Document.

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
