---
title: Добавить текстовые аннотации
linktitle: Добавить текстовые аннотации
type: docs
weight: 50
url: /python-net/add-text-annotation/
description: Добавьте текстовые аннотации в PDF‑документ с помощью класса PdfContentEditor в Aspose.PDF for Python via .NET.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить текстовые аннотации в Python
Abstract: Узнайте, как добавить текстовые аннотации в PDF‑документ с помощью класса PdfContentEditor в Aspose.PDF for Python via .NET. Этот пример демонстрирует, как разместить текстовую аннотацию в определённом месте, задать её заголовок и содержимое, а также сохранить обновлённый PDF‑файл.
---

В этой статье показано, как добавить текстовую аннотацию в PDF‑документ с помощью [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) класса в Aspose.PDF.

Текстовые аннотации позволяют прикреплять комментарии, заметки или дополнительную информацию к определённым частям страницы PDF. Такие аннотации могут отображаться в виде значков и расширяться пользователями при просмотре документа.

В этом примере:

- PDF‑документ загружается в PdfContentEditor.
- Текстовая аннотация добавляется в определённую позицию на странице.
- Аннотация включает заголовок, содержимое, тип значка и настройки видимости.
- Изменённый документ сохраняется в новый файл.

1. Создайте объект PdfContentEditor.
1. Привяжите входной PDF Document.
1. Определите позицию аннотации.
1. Добавьте аннотацию Text.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
