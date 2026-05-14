---
title: Получить значения полей
linktitle: Получить значения полей
type: docs
weight: 50
url: /ru/python-net/get-field-values/
description: Извлечение значений полей из PDF-формы с помощью Aspose.PDF Facades, используя класс Form.
lastmod: "2026-02-19"
---

Этот фрагмент кода показывает, как получить текущие значения полей формы из PDF-документа с помощью API Aspose.PDF Facades. Следующий [get_field()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) метод позволяет программно получать доступ к данным, введённым в текстовые поля, флажки, переключатели и другие элементы AcroForm.

1. Привяжите PDF к объекту Form.
1. Укажите имена полей, которые вы хотите прочитать.
1. Получите значение каждого поля, используя get_field().

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```
