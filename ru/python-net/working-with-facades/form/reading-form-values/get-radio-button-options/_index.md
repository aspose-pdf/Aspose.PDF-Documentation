---
title: Получить варианты радиокнопок
linktitle: Получить варианты радиокнопок
type: docs
weight: 20
url: /ru/python-net/get-radio-button-options/
description: В этой статье демонстрируется, как получить текущее выбранное значение поля радиокнопки в PDF‑документе с помощью API Aspose.PDF Facades.
lastmod: "2026-02-19"
---

Поля радиокнопок в PDF‑формах являются сгруппированными элементами управления, где одновременно может быть выбрана только одна опция. Каждая группа имеет имя поля, а каждая опция имеет соответствующее значение.

1. Создайте объект Form.
1. Привяжите PDF Document.
1. Получите выбранную опцию радиокнопки.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```

