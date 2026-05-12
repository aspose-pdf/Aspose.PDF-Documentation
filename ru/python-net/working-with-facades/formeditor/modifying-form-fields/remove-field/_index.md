---
title: Удалить поле
type: docs
weight: 60
url: /python-net/remove-field/
description: Этот пример показывает, как удалить поле 'Country' из PDF-формы с помощью метода 'remove_field' класса 'FormEditor'.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить поле формы из PDF-документа с помощью Python
Abstract: Этот пример демонстрирует, как удалить существующее поле формы из PDF-документа с использованием Aspose.PDF for Python. Код загружает PDF-файл, удаляет указанное поле с помощью класса FormEditor и сохраняет обновлённый документ.
---

PDF-формы могут содержать поля, которые больше не нужны из‑за изменений дизайна или обновлений рабочего процесса. С Aspose.PDF for Python разработчики могут легко программно удалять отдельные поля формы.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Класс в Aspose.PDF предоставляет метод 'remove_field', который позволяет разработчикам удалять поле формы по его имени.

1. Загрузите PDF‑документ.
1. Создать объект FormEditor.
1. Привязать PDF к FormEditor.
1. Удалите указанное поле формы.
1. Сохраните обновлённый документ.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```
