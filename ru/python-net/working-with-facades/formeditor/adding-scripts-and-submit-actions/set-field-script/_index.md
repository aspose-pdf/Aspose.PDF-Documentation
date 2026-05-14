---
title: Установить скрипт поля
linktitle: Установить скрипт поля
type: docs
weight: 30
url: /ru/python-net/set-field-script/
description: Этот фрагмент кода показывает, как назначить действие JavaScript полю формы в PDF‑документе с использованием Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить действия JavaScript для полей формы PDF с использованием Python
Abstract: В этой статье объясняется, как открыть PDF‑документ, назначить код JavaScript полю формы, обновить скрипт с помощью класса FormEditor и сохранить изменённый файл. Пример демонстрирует, как существующие скрипты могут быть переопределены для изменения поведения полей формы.
---

Интерактивные PDF‑формы часто полагаются на JavaScript для выполнения таких задач, как отображение предупреждений, проверка ввода или запуск динамического поведения формы. С помощью Aspose.PDF for Python разработчики могут программно управлять этими скриптами.

В примере сначала добавляется действие JavaScript к полю, а затем оно заменяется другим скриптом с помощью метода 'set_field_script'. Такой подход позволяет разработчикам контролировать или обновлять интерактивное поведение элементов PDF‑формы, таких как кнопки или поля ввода.

Поле формы, используемое в этом примере, называется 'Script_Demo_Button', которое обычно представляет кнопку, выполняющую назначенный скрипт при срабатывании.

Используя [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуля, разработчики могут программно управлять действиями JavaScript, связанными с полями формы:

1. Откройте существующий документ PDF-формы.
1. Добавьте действие JavaScript к полю формы.
1. Установите (замените) действие JavaScript новым скриптом.
1. Сохраните изменённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```

