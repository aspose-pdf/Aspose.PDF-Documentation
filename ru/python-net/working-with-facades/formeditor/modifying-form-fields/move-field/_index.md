---
title: Переместить поле
linktitle: Переместить поле
type: docs
weight: 50
url: /python-net/move-field/
description: Переместить существующее поле формы в другое место в PDF‑документе.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переместить поле формы PDF в новое положение с использованием Python
Abstract: В этом примере демонстрируется, как переместить существующее поле формы в другое место в PDF‑документе с использованием Aspose.PDF for Python. Код открывает существующий PDF, перемещает указанное поле формы к новым координатам и сохраняет обновленный документ.
---

PDF‑формы часто требуют корректировки макета после создания. С помощью Aspose.PDF for Python разработчики могут перемещать существующие поля формы в новое положение без их восстановления.

В этом примере показано, как переместить поле "Country", указав новые координаты его расположения на странице. Класс [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) предоставляет метод move_field для перемещения полей внутри страницы PDF.

1. Откройте существующую PDF-форму.
1. Создайте объект FormEditor.
1. Привяжите PDF‑документ к FormEditor.
1. Переместите поле 'Country' в новое положение, используя координаты.
1. Сохраните изменённый документ.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```
