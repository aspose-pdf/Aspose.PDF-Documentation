---
title: Экспорт в JSON
linktitle: Экспорт в JSON
type: docs
weight: 30
url: /ru/python-net/export-to-json/
description: В этом примере демонстрируется, как экспортировать значения полей формы PDF в файл JSON с использованием Aspose.PDF for Python via .NET. Описывается, как загрузить форму PDF, получить доступ к её полям через фасад Form и сохранить извлечённые данные в структурированном формате JSON.
lastmod: "2026-02-19"
---

JSON — это широко используемый формат данных, обеспечивающий беспрепятственный обмен данными между приложениями и сервисами. В этом примере объект [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) из модуля [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) используется для привязки PDF-файла и экспорта значений полей формы в удобочитаемую структуру JSON.

1. Инициализируйте pdf_facades.Form() для работы с полями формы.
1. Используйте 'bind_pdf()' для прикрепления исходного PDF‑документа.
1. Создайте поток для записи, используя 'FileIO()'.
1. Вызовите 'export_json()', чтобы извлечь значения полей формы и сохранить их в отформатированном JSON.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```

