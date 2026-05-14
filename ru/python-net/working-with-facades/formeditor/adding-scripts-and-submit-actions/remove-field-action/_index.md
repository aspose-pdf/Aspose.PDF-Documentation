---
title: Удалить действие поля
linktitle: Удалить действие поля
type: docs
weight: 20
url: /python-net/remove-field-action/
description: Удаление JavaScript из полей формы может быть полезным при изменении интерактивных PDF‑форм, отключении ранее назначенных действий или очистке документов, содержащих ненужные скрипты.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить действия JavaScript из полей PDF‑формы с помощью Python
Abstract: С помощью Aspose.PDF for Python разработчики могут программно удалять действия JavaScript, привязанные к полям формы. В этой статье объясняется, как открыть существующую PDF‑форму, удалить скрипт, связанный с конкретным полем, используя класс FormEditor, проверить операцию и сохранить изменённый документ.
---

PDF‑формы часто содержат действия JavaScript, которые выполняются, когда пользователи взаимодействуют с элементами формы, такими как кнопки или поля ввода. В некоторых случаях эти скрипты необходимо удалить, чтобы упростить поведение формы, повысить безопасность или обновить логику формы. Удалите действие JavaScript из поля формы в PDF‑документе с помощью Aspose.PDF for Python. Код открывает существующую PDF‑форму, находит конкретное поле, удаляет связанное с ним действие JavaScript и сохраняет обновлённый документ как новый PDF‑файл.

Используя [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/), вы можете удалить действия JavaScript из конкретных полей в существующей PDF‑форме:

1. Откройте существующую PDF-форму.
1. Найдите поле формы с именем 'Script_Demo_Button'.
1. Удалите действие JavaScript, связанное с этим полем.
1. Проверьте, было ли удаление успешным.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```
