---
title: Установить внешний вид поля
linktitle: Установить внешний вид поля
type: docs
weight: 50
url: /ru/python-net/set-field-appearance/
description: В этом примере показано, как изменить визуальный внешний вид поля формы PDF с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить внешний вид поля формы PDF с использованием Python
Abstract: В этой статье объясняется, как открыть PDF, установить внешний вид поля формы с использованием класса FormEditor и сохранить обновлённый документ. В примере внешний вид поля с именем 'First Name' задаётся как невидимый с помощью флага AnnotationFlags.INVISIBLE.
---

Поля формы PDF поддерживают флаги внешнего вида, которые контролируют видимость, печатаемость и интерактивность. С помощью Aspose.PDF for Python разработчики могут программно изменять эти флаги для конкретных полей формы.

Используя [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс, разработчики могут изменять флаги, чтобы скрывать, показывать или настраивать поведение полей формы в интерактивном PDF.

1. Откройте существующий PDF‑документ.
1. Создайте объект FormEditor.
1. Установите внешний вид поля с именем 'First Name' в невидимое.
1. Сохраните обновлённый документ.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to invisible
    if not form_editor.set_field_appearance(
        "First Name", ap.annotations.AnnotationFlags.INVISIBLE
    ):
        raise Exception(
            "Failed to set field appearance. Field may not support appearance flags."
        )

    # Save updated document
    form_editor.save(outfile)
```

