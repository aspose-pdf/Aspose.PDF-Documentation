---
title: Создать кнопку отправки
linktitle: Создать кнопку отправки
type: docs
weight: 50
url: /python-net/create-submit-button/
description: Узнайте, как программно добавить кнопку отправки в документ PDF с помощью Aspose.PDF for Python. Этот учебный материал демонстрирует, как создать кнопку, которая отправляет данные формы на указанный URL, и сохранить обновлённый PDF.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать кнопку отправки в PDF с использованием Aspose.PDF for Python
Abstract: Кнопки отправки в PDF-формах позволяют пользователям отправлять данные формы непосредственно на сервер или конечную точку. В этом руководстве вы узнаете, как добавить поле кнопки отправки в PDF с помощью класса FormEditor в Aspose.PDF for Python. Пример показывает, как настроить имя кнопки, её подпись, целевой URL и позицию, а затем сохранить обновлённый документ PDF.
---

Интерактивные PDF-формы часто требуют от пользователей отправки их ввода для обработки, например, отправки результатов опросов, заявок или отзывов. Поле кнопки отправки предоставляет эту функцию, связывая кнопку с веб‑конечной точкой.

Класс [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) позволяет добавлять кнопки, флажки, переключатели, текстовые поля и другие элементы управления формой.

1. Загрузите существующий PDF‑документ.
1. Добавьте поле кнопки Submit на конкретную страницу.
1. Установите метку кнопки и целевой URL-адрес отправки.
1. Сохраните обновлённый PDF с новой кнопкой.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
