---
title: Создать поле ComboBox
linktitle: Создать поле ComboBox
type: docs
weight: 20
url: /ru/python-net/create-combobox-field/
description: Проверьте, как программно добавить поле ComboBox (выпадающий список) в документ PDF с помощью Aspose.PDF for Python. Этот пример демонстрирует, как вставить поле ComboBox, добавить выбираемые элементы и сохранить обновлённый файл PDF.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать поле ComboBox в PDF с использованием Aspose.PDF for Python
Abstract: Интерактивные поля формы делают PDF более динамичными и удобными для пользователя. Поле ComboBox позволяет пользователям выбирать вариант из заранее определённого выпадающего списка. В этом учебном пособии вы узнаете, как создать ComboBox в PDF с помощью класса FormEditor в Aspose.PDF for Python, заполнить его вариантами и сохранить изменённый документ.
---

PDF-формы широко используются для сбора структурированной информации в цифровых документах, таких как заявки, опросы и регистрационные формы. Поле ComboBox предоставляет удобный способ для пользователей выбирать из списка заранее определённых значений, одновременно сохраняя форму компактной и организованной.

Следующий [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс позволяет создавать и управлять различными типами полей, включая текстовые поля, флажки, переключатели и раскрывающиеся списки.

1. Загрузите существующий PDF‑документ.
1. Добавьте поле ComboBox с помощью метода 'add_field()' и параметра 'FieldType.COMBO_BOX'.
1. Используйте метод 'add_list_item()', чтобы вставить варианты выбора в раскрывающийся список.
1. Сохраните обновлённый PDF‑документ.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514
    )
    pdf_form_editor.add_list_item("combobox1", ["Australia", "Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand", "New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

