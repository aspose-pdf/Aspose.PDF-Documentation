---
title: Импортировать JSON-данные
type: docs
weight: 30
url: /python-net/import-json-data/
description: В этом примере демонстрируется, как импортировать данные полей формы из файла JSON в PDF-форму, используя Aspose.PDF for Python via .NET. Показано, как привязать PDF-документ, прочитать структурированные JSON-данные через поток файла и автоматически заполнить соответствующие поля формы.
lastmod: "2026-02-19"
---

JSON широко используется для хранения и передачи структурированных данных между системами. В этом примере, [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуль используется для привязки PDF-формы и импорта значений полей из внешнего файла JSON. После процесса импорта обновлённый документ сохраняется как новый PDF.

1. Инициализируйте pdf_facades.Form() для работы с полями PDF-формы.
1. Вызовите 'bind_pdf()' для присоединения шаблона PDF‑формы.
1. Используйте 'FileIO()' для чтения файла JSON, содержащего значения полей формы.
1. Вызовите 'import_json()', чтобы заполнить поля PDF, используя пары ключ‑значение JSON.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```
