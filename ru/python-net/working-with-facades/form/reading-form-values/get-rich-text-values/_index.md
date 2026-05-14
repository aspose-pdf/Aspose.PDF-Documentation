---
title: Получить значения Rich Text
linktitle: Получить значения Rich Text
type: docs
weight: 40
url: /python-net/get-rich-text-values/
description: Этот раздел объясняет, как получить содержимое Rich Text поля формы в PDF‑документе с помощью API Aspose.PDF Facades. В отличие от обычных текстовых полей, поля Rich Text могут содержать форматированный контент, такой как полужирный текст, различные шрифты, цвета и стили абзацев.
lastmod: "2026-02-19"
---

PDF‑формы могут включать текстовые поля, поддерживающие форматирование Rich Text. Эти поля могут хранить содержимое со стилевыми атрибутами в дополнение к обычным текстовым значениям.

1. Создайте объект Form.
1. Привяжите PDF Document.
1. Получите значения Rich Text.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```
