---
title: Создать поле RadioButton
type: docs
weight: 40
url: /python-net/create-radiobutton-field/
description: Узнайте, как программно добавить поле радиокнопки в PDF‑документ с помощью Aspose.PDF for Python. Этот пример демонстрирует, как создать группу радиокнопок, определить варианты выбора и сохранить обновлённый PDF‑файл.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать поле радиокнопки в PDF с использованием Aspose.PDF for Python
Abstract: Радиокнопки часто используются в PDF‑формах, позволяя пользователям выбирать одну опцию из предопределённой группы вариантов. В этом руководстве вы узнаете, как создать поле радиокнопки в PDF, используя класс FormEditor в Aspose.PDF for Python. Пример показывает, как определить элементы радиокнопок, установить выбор по умолчанию и сохранить обновлённый документ.
---

Интерактивные PDF‑формы позволяют пользователям предоставлять структурированные данные непосредственно в документе. Поле радиокнопки полезно, когда пользователям необходимо выбрать только одну опцию из нескольких, например, при выборе страны, пола или предпочтения.

Следующий [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс предоставляет методы для создания различных типов полей, включая текстовые поля, флажки, раскрывающиеся списки, списки и радиокнопки.

1. Загрузите существующий PDF‑документ.
1. Определите список вариантов переключателей.
1. Добавьте поле переключателя на определённую страницу.
1. Установите значение по умолчанию.
1. Сохраните изменённый PDF‑документ.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
