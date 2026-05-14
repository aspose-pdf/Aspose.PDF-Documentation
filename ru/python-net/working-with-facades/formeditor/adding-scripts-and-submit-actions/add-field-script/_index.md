---
title: Добавить скрипт поля
type: docs
weight: 10
url: /python-net/add-field-script/
description: Интерактивные PDF‑формы могут включать JavaScript для автоматизации действий, когда пользователи взаимодействуют с полями формы. С помощью Aspose.PDF for Python разработчики могут легко прикреплять скрипты к элементам формы, таким как кнопки или текстовые поля.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить действия JavaScript к полям PDF‑формы с помощью Python
Abstract: В этой статье объясняется, как открыть PDF‑форму, назначить код JavaScript конкретному полю формы, добавить дополнительные действия скрипта и сохранить обновленный документ. В примере используется класс FormEditor из API Aspose.PDF Facades для программного управления поведением формы.
---

## Добавить действия JavaScript к полям PDF‑формы с помощью Python

Этот фрагмент кода позволяет добавить действия JavaScript к существующему полю PDF‑формы с использованием библиотеки Aspose.PDF for Python. Он открывает PDF‑документ, назначает действие JavaScript полю формы и добавляет скрипт, который выполняется при срабатывании поля. В конце обновлённый PDF сохраняется в новый файл.
Используя [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуля, вы можете программно привязать JavaScript к существующим полям формы:

1. Откройте существующую PDF-форму.
1. Установите действие JavaScript для конкретного поля.
1. Добавьте другое действие JavaScript к тому же полю.
1. Сохраните изменённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
