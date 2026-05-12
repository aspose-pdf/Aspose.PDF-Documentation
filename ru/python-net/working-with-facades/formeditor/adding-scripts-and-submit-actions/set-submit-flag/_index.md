---
title: Установить флаг отправки
type: docs
weight: 50
url: /python-net/set-submit-flag/
description: Узнайте, как программно установить флаг отправки для кнопки формы PDF, используя Aspose.PDF for Python. Это позволяет кнопке отправлять данные формы в определённом формате, например XFDF, при нажатии пользователем.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить флаг отправки для кнопки формы PDF с помощью Aspose.PDF for Python
Abstract: Формы PDF можно настроить для отправки данных формы на сервер или конечную точку в разных форматах. Устанавливая флаг отправки у поля‑кнопки, разработчики могут определить способ отправки данных. В этом руководстве показано, как использовать класс FormEditor для установки флага отправки у существующей кнопки отправки в документе PDF и сохранить обновлённый файл.
---

Формы PDF часто включают кнопки отправки для передачи ввода пользователя на сервер. Флаг отправки определяет формат отправляемых данных (например, XFDF, FDF, HTML).

1. Привязать документ PDF.
1. Получить доступ к существующей кнопке отправки.
1. Установить флаг отправки для требуемого формата.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
