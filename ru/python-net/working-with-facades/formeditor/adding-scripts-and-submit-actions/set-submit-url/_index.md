---
title: Установить URL отправки
linktitle: Установить URL отправки
type: docs
weight: 40
url: /ru/python-net/set-submit-url/
description: В этом примере показано, как настроить действие отправки для поля кнопки в PDF‑форме с использованием Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить URL отправки для кнопки PDF‑формы с помощью Python
Abstract: В этой статье объясняется, как открыть существующую PDF‑форму, определить URL отправки для поля кнопки с использованием класса FormEditor, проверить успешность операции и сохранить обновлённый PDF‑документ.
---

PDF‑формы могут быть спроектированы для отправки своих данных на веб‑сервер при нажатии пользователем кнопки отправки. С помощью Aspose.PDF for Python разработчики могут программно настроить действие отправки для полей формы.
Установив URL отправки, форма может отправлять введённые пользователем данные на сервер при нажатии кнопки. Эта функция полезна для рабочих процессов, когда PDF‑формы должны отправлять информацию в веб‑приложения, базы данных или службы обработки.

Используя [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуля, разработчики могут программно назначать URL-адрес отправки для поля кнопки в существующей PDF-форме.

1. Откройте существующую PDF-форму.
1. Найдите поле кнопки с именем Script_Demo_Button.
1. Назначьте URL-адрес, куда будут отправляться данные формы.
1. Проверьте, что действие было успешно применено.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```

