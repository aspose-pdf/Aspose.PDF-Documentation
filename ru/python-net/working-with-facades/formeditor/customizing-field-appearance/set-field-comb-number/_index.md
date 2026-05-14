---
title: Установить количество ячеек поля
type: docs
weight: 70
url: /python-net/set-field-comb-number/
description: В этом примере демонстрируется, как установить количество ячеек (comb number) для поля формы PDF с использованием Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить количество ячеек (comb number) для полей формы PDF с использованием Python
Abstract: С помощью Aspose.PDF for Python разработчики могут программно установить количество ячеек (comb number) для поля формы, чтобы обеспечить ввод фиксированной длины. В этой статье демонстрируется установка количества ячеек для поля с именем "PIN".
---

Количество ячеек определяет, как содержимое поля разбивается на равномерно расположенные ячейки, часто используется для PIN‑кодов, серийных номеров или других полей ввода фиксированной длины. Код открывает существующий PDF, устанавливает количество ячеек для поля и сохраняет изменённый документ.

Класс [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) предоставляет метод ‘set_field_comb_number’, позволяющий задать количество ячеек (символов) в поле формы.

1. Откройте существующую PDF-форму.
1. Создайте объект FormEditor.
1. Установите число comb поля с именем "PIN" равным 5.
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


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```
