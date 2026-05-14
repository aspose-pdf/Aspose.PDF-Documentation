---
title: Переименовать поле
linktitle: Переименовать поле
type: docs
weight: 70
url: /python-net/rename-field/
description: Переименуйте существующее поле формы в PDF‑документе с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переименование поля PDF‑формы с использованием Python
Abstract: Этот пример демонстрирует, как переименовать существующее поле формы в PDF‑документе с помощью Aspose.PDF for Python. Код открывает входной PDF, изменяет имя указанного поля формы с использованием класса FormEditor и сохраняет обновлённый документ.
---

PDF‑формы часто полагаются на имена полей для скриптов, автоматизации и обработки данных. С помощью Aspose.PDF for Python разработчики могут переименовывать существующие поля без их воссоздания или изменения макета формы.

Класс [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) предоставляет метод 'rename_field', который позволяет разработчикам изменить имя существующего поля, сохраняя его позицию, значение и внешний вид.

1. Загрузите существующую PDF-форму.
1. Создайте экземпляр FormEditor.
1. Привяжите PDF‑документ к редактору.
1. Переименуйте целевое поле.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```

