---
title: Заполнить поля штрихкода
linktitle: Заполнить поля штрихкода
type: docs
weight: 50
url: /python-net/fill-barcode-fields/
description: Этот пример демонстрирует, как программно заполнять поля штрихкода в PDF‑форме с использованием Aspose.PDF for Python via .NET. Он показывает, как привязать PDF‑документ, задать значение полю штрихкода и сохранить обновлённый файл.
lastmod: "2026-02-19"
---

Поля штрихкода в PDF‑формах позволяют сохранять закодированную информацию и визуально отображать её в виде штрихкодов. В этом примере [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуля используется для доступа к полям формы и назначениям штрихкода. После заполнения данных PDF сохраняется с обновлённым содержимым штрихкода.

1. Инициализируйте 'pdf_facades.Form()', чтобы управлять взаимодействиями с PDF‑формой.
1. Вызовите 'bind_pdf()', чтобы прикрепить PDF, содержащий поля штрих-кода.
1. Используйте 'fill_field()', чтобы назначить значение штрих-кода.
1. Сохраните обновлённый Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```
