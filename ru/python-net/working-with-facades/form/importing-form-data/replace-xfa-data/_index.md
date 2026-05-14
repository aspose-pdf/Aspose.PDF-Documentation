---
title: Заменить данные XFA
linktitle: Заменить данные XFA
type: docs
weight: 50
url: /ru/python-net/replace-xfa-data/
description: В этом примере показано, как заменить существующие данные формы XFA в PDF с использованием Aspose.PDF for Python via .NET. Он демонстрирует, как привязать PDF‑документ на основе XFA, загрузить новые данные из внешнего файла XFA и программно обновить содержимое формы.
lastmod: "2026-02-19"
---

Формы XFA (XML Forms Architecture) хранят свои данные в формате XML внутри структуры PDF. В этом примере, [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуля используется для привязки PDF и замены его существующего набора данных XFA с использованием внешнего XML‑потока. После применения новых данных обновлённый PDF сохраняется как отдельный файл.

1. Инициализируйте pdf_facades.Form() для управления данными формы XFA.
1. Вызовите функцию 'bind_pdf()', чтобы прикрепить PDF-файл, содержащий формы XFA.
1. Используйте 'FileIO()' для чтения XML‑файла XFA.
1. Вызовите 'set_xfa_data()' для обновления PDF новым содержимым XFA.
1. Сохраните обновлённый Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```

