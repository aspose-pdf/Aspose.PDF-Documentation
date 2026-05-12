---
title: Получить полные имена полей
type: docs
weight: 60
url: /python-net/resolve-full-field-names/
description: Этот пример демонстрирует, как получить полностью квалифицированные имена полей формы в PDF‑документе с использованием Aspose.PDF Facades API.
lastmod: "2026-02-19"
---

В PDF‑формах поля могут быть организованы иерархически, особенно когда используются подформы. Каждое поле имеет короткое имя и полностью квалифицированное имя. Полностью квалифицированное имя представляет собой полный путь поля внутри иерархии формы и требуется многими методами API, которые манипулируют или читают данные формы.

1. Создать объект Form.
1. Привязать PDF Document.
1. Получить все имена полей формы
1. Полностью квалифицированное имя каждого поля определяется с помощью get_full_field_name().

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```
