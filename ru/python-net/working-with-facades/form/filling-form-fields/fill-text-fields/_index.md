---
title: Заполнить текстовые поля
linktitle: Заполнить текстовые поля
type: docs
weight: 10
url: /ru/python-net/fill-text-fields/
description: Этот пример демонстрирует, как автоматически заполнять текстовые поля в PDF‑форме, используя Aspose.PDF for Python via .NET. Он показывает, как загрузить PDF‑документ, заполнить конкретные поля формы по имени и сохранить обновлённый файл.
lastmod: "2026-02-19"
---

Программное заполнение текстовых полей позволяет приложениям повторно использовать PDF‑шаблоны и вставлять динамический контент без ручного редактирования. В этом примере [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) используется для привязки PDF‑формы и обновления нескольких полей, таких как имя, адрес и электронная почта. После чего изменённый PDF сохраняется как новый документ.

1. Инициализируйте 'pdf_facades.Form()' для управления операциями с полями формы.
1. Используйте 'bind_pdf()' для прикрепления входного PDF, содержащего текстовые поля.
1. Вызовите 'fill_field()', чтобы вставить данные в поля, такие как имя, адрес и электронная почта.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```

