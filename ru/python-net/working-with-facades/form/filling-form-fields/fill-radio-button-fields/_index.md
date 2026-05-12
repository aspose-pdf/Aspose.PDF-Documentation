---
title: Заполнить поля радиокнопок
type: docs
weight: 30
url: /python-net/fill-radio-button-fields/
description: В этом примере демонстрируется, как программно заполнять поля радиокнопок в PDF‑форме с использованием Aspose.PDF for Python via .NET. Показано, как привязать PDF‑документ, выбрать вариант радиокнопки по индексу и сохранить обновлённый файл.
lastmod: "2026-02-19"
---

Переключатели позволяют пользователям выбрать один вариант из заранее определённой группы, например, поля пола или предпочтений. В этом примере [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуль используется для привязки исходного PDF и назначения выбранного варианта по его индексу. После выбора желаемого варианта изменённый документ сохраняется.

1. Инициализируйте pdf_facades.Form() для управления полями PDF‑формы.
1. Вызовите 'bind_pdf()', чтобы прикрепить PDF, содержащий поля радиокнопок.
1. Используйте 'fill_field()', чтобы выбрать первый вариант (индекс 0).
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```
