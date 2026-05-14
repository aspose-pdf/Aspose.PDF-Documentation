---
title: Заполнять поля по имени и значению
linktitle: Заполнять поля по имени и значению
type: docs
weight: 60
url: /python-net/fill-fields-by-name-and-value/
description: В этой статье демонстрируется, как динамически заполнять несколько полей формы PDF по имени и значению с использованием Aspose.PDF for Python via .NET. Вместо того чтобы задавать каждое поле отдельно, используется структура словаря для сопоставления имен полей со значениями и их заполнения в цикле.
lastmod: "2026-02-19"
---

Заполнение полей формы с использованием коллекции имя‑значение позволяет разработчикам создавать масштабируемые и гибкие решения для автоматизации форм PDF. В этом примере [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) используется для привязки PDF‑документа и перебора словаря данных полей. Каждая запись применяется с помощью метода ‘fill_field’, что обеспечивает эффективное обновление полей формы.

1. Инициализируйте 'pdf_facades.Form()', чтобы работать с интерактивными полями формы.
1. Используйте 'bind_pdf()' для прикрепления исходного PDF‑документа.
1. Создайте словарь, содержащий имена полей и значения, которые вы хотите вставить.
1. Итерируйте по словарю и вызывайте 'fill_field()' для каждой записи.
1. Сохраните обновлённый Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```
