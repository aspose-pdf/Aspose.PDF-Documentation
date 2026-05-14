---
title: Заполнить List Box
linktitle: Заполнить List Box
type: docs
weight: 40
url: /python-net/fill-list-box/
description: В этом примере демонстрируется, как программно заполнять поля списка и множественного выбора в PDF‑форме с использованием Aspose.PDF for Python via .NET. Показано, как привязать PDF‑документ, выбрать значения в форме поля списка и сохранить обновлённый файл.
lastmod: "2026-02-19"
---

Поля List Box с множественным выбором позволяют пользователям выбирать одно или несколько значений из заранее заданного набора вариантов. В этом примере [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) используется для доступа к PDF‑форме и назначения выбранного значения полю favorite_colors. После выбора нужного варианта обновлённый документ сохраняется.

1. Инициализируйте 'pdf_facades.Form()' для управления и обновления полей формы.
1. Вызовите 'bind_pdf()' для привязки исходного PDF, содержащего поля list box или множественного выбора.
1. Используйте 'fill_field()' для выбора значения из доступных вариантов.
1. Сохраните обновлённый Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```
