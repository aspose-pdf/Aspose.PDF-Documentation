---
title: Получить имена обязательных полей
type: docs
weight: 30
url: /python-net/get-required-field-names/
description: Этот пример демонстрирует, как идентифицировать и получить имена обязательных полей формы в PDF-документе с использованием API Aspose.PDF Facades.
lastmod: "2026-02-19"
---

PDF-формы могут содержать обязательные поля, которые пользователи должны заполнить перед отправкой. Эти поля обычно помечены как обязательные в свойствах формы.

1. Создайте объект Form.
1. Привяжите PDF Document.
1. Получите все имена полей можно с помощью 'pdf_form.field_names'.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")
```
