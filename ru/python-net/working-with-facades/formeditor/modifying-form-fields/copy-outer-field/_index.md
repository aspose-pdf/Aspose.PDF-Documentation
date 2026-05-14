---
title: Копировать внешнее поле
linktitle: Копировать внешнее поле
type: docs
weight: 30
url: /ru/python-net/copy-outer-field/
description: В этом примере демонстрируется, как скопировать поле формы из одного PDF‑документа в другой, используя Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Копировать PDF‑поля формы из другого документа, используя Python
Abstract: В этой статье объясняется, как создать новый PDF‑документ, скопировать поле 'First Name' из исходного PDF на страницу 1 с координатами (200, 600) и сохранить обновлённый целевой документ.
---

Иногда PDF‑формы требуют повторного использования полей из одного документа в другом. С помощью Aspose.PDF for Python разработчики могут программно копировать поля формы из исходного PDF в целевой PDF.

Класс [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) предоставляет метод 'copy_outer_field', который копирует поле из исходного документа в целевой документ на указанной странице и координатах.

Код создает новый PDF (целевой), добавляет страницу, а затем копирует поле из существующего PDF (исходного) в целевой документ на заданных координатах.

1. Создайте новый целевой PDF‑документ.
1. Добавьте как минимум одну страницу в целевой PDF.
1. Сохраните пустой целевой документ.
1. Создайте объект FormEditor и привяжите его к целевому PDF.
1. Скопируйте поле 'First Name' из исходного PDF на страницу 1 в координаты (200, 600).
1. Сохраните обновлённый целевой PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Обратите внимание:**

Сигнатура метода 'copy_outer_field' выглядит так:

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – поле, которое вы хотите дублировать.
- 'new_field_name' – имя нового поля.
- 'page_number' – страница, на которой появится новое поле.
- x, y – координаты на этой странице.

Ожидается, что page_number будет положительным целым числом, соответствующим существующей странице в PDF (нумерация с 1).

Если передать отрицательный параметр, например:

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

Программа затем сбросит параметры к предыдущим.

