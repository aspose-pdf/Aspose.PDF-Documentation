---
title: Создать поле ListBox
linktitle: Создать поле ListBox
type: docs
weight: 30
url: /ru/python-net/create-listbox-field/
description: Узнайте, как программно добавить поле формы ListBox в документ PDF с использованием Aspose.PDF for Python. Это руководство показывает, как вставить поле ListBox, определить выбираемые элементы и сохранить обновлённый файл PDF.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать поле ListBox в PDF с использованием Aspose.PDF for Python
Abstract: PDF‑формы позволяют пользователям взаимодействовать с документами, выбирая варианты, вводя данные и отправляя информацию в цифровом виде. Поле ListBox даёт возможность выбирать одно или несколько значений из видимого списка вариантов. В этом руководстве вы узнаете, как создать поле ListBox в PDF с помощью класса FormEditor в Aspose.PDF for Python и заполнить его предопределёнными элементами.
---

PDF‑формы часто используются в заявках, опросах и регистрационных документах. Поле ListBox отображает несколько вариантов одновременно, облегчая пользователям просмотр и выбор элементов из списка.

Следующий [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс предоставляет функциональность для добавления различных типов интерактивных полей, включая элементы ListBox.

1. Загрузите существующий PDF‑документ.
1. Определите список выбираемых вариантов.
1. Добавьте поле ListBox на конкретную страницу.
1. Установите значение по умолчанию.
1. Сохраните обновлённый PDF‑документ.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

