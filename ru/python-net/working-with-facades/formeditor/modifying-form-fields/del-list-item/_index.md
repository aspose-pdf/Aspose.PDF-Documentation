---
title: Удалить элемент списка
linktitle: Удалить элемент списка
type: docs
weight: 40
url: /python-net/del-list-item/
description:
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить элементы из полей списка PDF, используя Python
Abstract: В этом примере показано, как удалить элемент из поля списка формы в PDF‑документе с использованием Aspose.PDF for Python. Код открывает существующий PDF, удаляет определённый элемент из поля списка и сохраняет обновлённый документ.
---

Поля списка в PDF позволяют пользователям выбирать один или несколько предопределённых вариантов. С помощью Aspose.PDF for Python разработчики могут программно удалять элементы из этих полей.

В этой статье объясняется, как удалить элемент 'UK' из поля списка с именем 'Country', гарантируя, что поле содержит только необходимые варианты.

Класс [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) предоставляет метод 'del_list_item' для удаления конкретного элемента из поля списка.

1. Откройте существующую PDF-форму.
1. Создайте объект FormEditor.
1. Привяжите PDF‑документ к FormEditor.
1. Удалить элемент 'UK' из поля списка 'Country'.
1. Сохраните обновлённый документ.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```

