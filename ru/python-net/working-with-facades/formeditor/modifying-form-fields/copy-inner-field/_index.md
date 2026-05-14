---
title: Скопировать внутреннее поле
linktitle: Скопировать внутреннее поле
type: docs
weight: 20
url: /python-net/copy-inner-field/
description: Скопировать поля формы PDF в новое положение с помощью Python, используя Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Скопировать поля формы PDF в новое положение с помощью Python
Abstract: В этом примере демонстрируется, как скопировать существующее поле формы в новое положение в PDF-документе с использованием Aspose.PDF for Python. Код открывает PDF, дублирует поле на указанную страницу и координаты и сохраняет обновлённый документ.
---

PDF-формы часто требуют дублирования полей при сохранении оригинального форматирования и поведения. С помощью Aspose.PDF for Python разработчики могут программно копировать существующее поле в новое положение на той же или другой странице.

В этой статье объясняется, как скопировать поле с именем 'First Name' в новое поле под названием 'First Name Copy' на странице 2 с конкретными координатами (x=200, y=600), создавая PDF с новым расположенным полем.

1. Откройте существующую PDF-форму.
1. Создайте объект FormEditor.
1. Привяжите PDF‑документ к FormEditor.
1. Скопируйте поле 'First Name' в новое поле 'First Name Copy' на странице 2 с координатами (200, 600).
1. Сохраните обновлённый документ.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Обратите внимание:**

Подпись метода 'copy_inner_field' выглядит так:

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – поле, которое вы хотите дублировать.
- 'new_field_name' – имя нового поля.
- 'page_number' – страница, на которой появится новое поле.
- x, y – координаты на этой странице.

Ожидается, что page_number будет положительным целым числом, соответствующим существующей странице в PDF (нумерация с 1).

Если передать отрицательный параметр, например:

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

Программа затем сбросит параметры к предыдущим.
