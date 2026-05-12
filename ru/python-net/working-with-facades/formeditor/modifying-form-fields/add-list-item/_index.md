---
title: Добавить элемент списка
type: docs
weight: 10
url: /python-net/add-list-item/
description: В этом примере демонстрируется, как добавить элементы в поле списка формы в PDF‑документе с использованием Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление элементов в поля списка PDF с использованием Python
Abstract: В этой статье показано, как открыть PDF‑документ, добавить элементы в поле списка с именем "Country" и сохранить обновлённый документ.
---

Поля списка в PDF позволяют пользователям выбирать одну или несколько опций из предопределённого набора. С помощью Aspose.PDF for Python разработчики могут программно добавлять новые элементы в эти поля. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс предоставляет метод ‘add_list_item’ для добавления элементов в существующее поле списка.

1. Откройте существующую PDF-форму.
1. Создать объект FormEditor.
1. Привязать PDF к FormEditor.
1. Добавить элементы в поле списка "Country".
1. Сохраните обновлённый документ.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```
