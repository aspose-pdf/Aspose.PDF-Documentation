---
title: Установить ограничение поля
type: docs
weight: 80
url: /python-net/set-field-limit/
description: Этот пример показывает, как установить максимальное ограничение количества символов для поля формы в PDF-документе с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить максимальное ограничение символов для полей формы PDF с использованием Python
Abstract: Этот пример демонстрирует установку ограничения символов для поля с именем 'Last Name' до 10 символов, гарантируя, что пользователи не смогут ввести более указанного лимита.
---

Поля формы в PDF-документах могут потребовать ограничений ввода для поддержания правильного форматирования. С помощью Aspose.PDF for Python разработчики могут программно задать максимальное количество символов для поля.

Класс [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) предоставляет метод 'set_field_limit' для определения максимальной длины ввода для поля.

1. Откройте существующую PDF-форму.
1. Создайте объект FormEditor.
1. Установите максимальный лимит символов для поля 'Last Name'.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```
