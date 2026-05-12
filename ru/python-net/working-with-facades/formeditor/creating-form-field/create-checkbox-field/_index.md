---
title: Создать поле CheckBox
type: docs
weight: 10
url: /python-net/create-checkbox-field/
description: Узнайте, как программно добавить поле формы‑чекбокс в документ PDF с помощью Aspose.PDF for Python. Это руководство демонстрирует, как использовать класс FormEditor для вставки интерактивного чекбокса в существующий файл PDF и сохранения обновлённого документа.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать поле Checkbox в PDF с использованием Aspose.PDF for Python
Abstract: Интерактивные поля формы позволяют пользователям заполнять и взаимодействовать с PDF‑документами в цифровом виде. В этом учебном руководстве вы узнаете, как добавить поле чекбокса в PDF с помощью Aspose.PDF Python API. Пример показывает, как привязать существующий PDF‑документ, создать поле формы‑чекбокс в указанных координатах и сохранить изменённый файл.
---

PDF‑формы широко используются для сбора пользовательских данных в документах, таких как заявки, опросы и соглашения. Поле чекбокса позволяет пользователям выбирать или снимать выбор варианта в форме.

С помощью Aspose.PDF for Python разработчики могут программно управлять PDF‑формами. Эта [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс предоставляет методы для добавления, редактирования и управления полями формы в PDF‑документе.

1. Загрузите существующий PDF‑файл.
1. Вызовите метод 'add_field()' с параметром 'FieldType.CHECK_BOX', чтобы создать флажок и указать его позицию.
1. Определите имя поля, подпись и позицию.
1. Сохраните обновлённый PDF‑документ.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
