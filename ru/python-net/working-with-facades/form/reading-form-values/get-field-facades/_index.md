---
title: Получить фасады полей
type: docs
weight: 10
url: /python-net/get-field-facades/
description: В этом примере демонстрируется, как считать значения конкретных полей формы из PDF‑документа с помощью Aspose.PDF Facades API.
lastmod: "2026-02-19"
---

PDF‑формы содержат поля, в которые пользователи могут вводить данные, например текстовые поля, флажки или переключатели. Для программной обработки этих форм часто необходимо получить текущие значения этих полей.

1. Создать объект Form.
1. Привяжите PDF‑документ к объекту формы.
1. Получить значения полей.

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