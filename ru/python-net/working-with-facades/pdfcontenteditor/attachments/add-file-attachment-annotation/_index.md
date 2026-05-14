---
title: Добавить аннотацию вложения файла
type: docs
weight: 30
url: /python-net/add-file-attachment-annotation/
description: В примере привязывается входной PDF, добавляется аннотация вложения файла на первую страницу с использованием пути к файлу и сохраняется обновлённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотации вложения файлов в PDF с использованием Python
Abstract: В этом примере демонстрируется, как создать аннотацию вложения файла в PDF, используя путь к файлу с Aspose.PDF for Python via the Facades API. Показано, как определить расположение аннотации, установить текст описания, выбрать тип значка и сохранить изменённый документ.
---

Аннотации вложения файлов позволяют встраивать внешние файлы в виде интерактивных значков на страницу PDF. Используя перегрузку с путём к файлу, вы можете прикреплять файлы непосредственно с диска без необходимости вручную открывать потоки. Этот метод также позволяет настроить значок аннотации и предоставить описание для пользователей.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) объект.
1. Привяжите входной PDF.
1. Определите прямоугольник аннотации.
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
