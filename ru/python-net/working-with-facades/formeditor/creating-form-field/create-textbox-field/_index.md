---
title: Создать поле TextBox
type: docs
weight: 60
url: /python-net/create-textbox-field/
description: Узнайте, как программно добавить поля TextBox в документ PDF с помощью Aspose.PDF for Python. Этот учебник показывает, как вставить несколько текстовых полей, задать значения по умолчанию и сохранить обновлённый документ PDF.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать поля TextBox в PDF с использованием Aspose.PDF for Python
Abstract: Поля TextBox в формах PDF позволяют пользователям вводить и редактировать текст, делая документы интерактивными и удобными. В этом учебнике вы узнаете, как создавать поля формы TextBox в PDF с помощью класса FormEditor в Aspose.PDF for Python. Пример демонстрирует добавление нескольких полей, указание значений по умолчанию и сохранение изменённого PDF.
---

Формы PDF часто требуют ввода текста от пользователей, например имён, адресов или комментариев. Поля TextBox обеспечивают эту функциональность, предоставляя редактируемые поля непосредственно в документе PDF.
Класс [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) позволяет добавлять текстовые поля, флажки, переключатели, списковые поля, комбинированные поля и кнопки, упрощая создание интерактивных PDF.

1. Загрузите существующий PDF‑документ.
1. Добавьте несколько полей TextBox для ввода пользователем.
1. Установите значения по умолчанию для каждого поля.
1. Сохраните обновлённый PDF‑документ.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
