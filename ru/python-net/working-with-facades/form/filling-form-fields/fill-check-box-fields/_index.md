---
title: Заполнить поля флажков
type: docs
weight: 20
url: /python-net/fill-check-box-fields/
description: В этом примере демонстрируется, как программно заполнять поля флажков в PDF-форме с использованием Aspose.PDF for Python via .NET. Показано, как привязать PDF‑документ, обновить значения флажков по имени поля и сохранить изменённый файл.
lastmod: "2026-02-19"
---

Флажок часто используется в PDF-формах для представления бинарных выборов, таких как подписка или подтверждение согласия. В этом примере, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) используется для доступа к полям формы и установки их значений в выбранное состояние. После обновления флажков заполненный PDF сохраняется как новый документ.

1. Инициализируйте 'pdf_facades.Form()' для управления взаимодействиями с полями формы.
1. Используйте 'bind_pdf()', чтобы присоединить исходный PDF, содержащий поля флажков.
1. Вызовите 'fill_field()', чтобы отметить поля, такие как 'subscribe_newsletter' и 'accept_terms', как выбранные.
1. Сохраните обновлённый Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```
