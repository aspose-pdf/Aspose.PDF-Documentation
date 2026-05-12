---
title: Однострочное поле в многострочное поле
type: docs
weight: 80
url: /python-net/single-to-multiple/
description: Преобразовать однострочное текстовое поле в многострочное поле в PDF‑документе с использованием Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Преобразовать однострочное текстовое поле в многострочное поле в PDF с использованием Python
Abstract: В этом примере демонстрируется, как преобразовать однострочное текстовое поле в многострочное поле в PDF‑документе с использованием Aspose.PDF for Python. Код загружает существующую PDF‑форму, изменяет указанное поле, позволяя вводить несколько строк текста, и сохраняет обновлённый документ.
---

PDF‑формы иногда содержат текстовые поля, предназначенные для ввода одной строки, что может быть недостаточно для некоторых типов данных. С помощью Aspose.PDF for Python разработчики могут легко преобразовать такие поля в многострочные текстовые поля без их воссоздания.

Используя [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class, разработчики могут изменять существующие текстовые поля, не влияя на их положение или другие свойства.

1. Загрузите существующий PDF-документ.
1. Создайте экземпляр FormEditor.
1. Привяжите PDF‑документ к редактору.
1. Преобразовать выбранное поле в многострочное.
1. Сохраните обновлённый документ.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```

