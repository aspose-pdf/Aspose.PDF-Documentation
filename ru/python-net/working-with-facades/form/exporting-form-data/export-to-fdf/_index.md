---
title: Экспорт в FDF
linktitle: Экспорт в FDF
type: docs
weight: 10
url: /ru/python-net/export-to-fdf/
description: Этот пример объясняет, как экспортировать данные полей формы PDF в файл FDF (Forms Data Format) с использованием Aspose.PDF for Python via .NET. Он демонстрирует, как получить доступ к интерактивным данным формы через фасад Form, привязать исходный PDF‑документ и сохранить извлечённые значения в поток FDF.
lastmod: "2026-02-19"
---

FDF — это облегченный формат, специально предназначенный для хранения и передачи данных формы PDF без включения полного документа. В этом примере, a [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) объект инициализируется из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуль, позволяющий разработчикам взаимодействовать с полями AcroForm и экспортировать их значения.

1. Создайте экземпляр pdf_facades.Form() для работы с полями формы PDF.
1. Вызовите 'bind_pdf()', чтобы присоединить PDF‑документ, содержащий форму.
1. Используйте 'open(')', чтобы создать двоичный поток с правом записи для файла FDF.
1. Экспортируйте данные формы. Вызовите 'export_fdf()', чтобы извлечь и сохранить все значения полей формы.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```

