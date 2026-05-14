---
title: Экспорт в XFDF
linktitle: Экспорт в XFDF
type: docs
weight: 20
url: /ru/python-net/export-to-xfdf/
description: В этом примере показано, как экспортировать данные полей формы PDF в файл XFDF (XML Forms Data Format) с использованием Aspose.PDF for Python via .NET. Он демонстрирует, как загрузить форму PDF, получить доступ к её полям через фасад Form и сохранить извлечённые значения в поток XFDF.
lastmod: "2026-02-19"
---

XFDF — это XML-представление данных PDF-форм, позволяющее разработчикам передавать значения полей формы независимо от исходного документа. В этом примере объект [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) используется для привязки исходного PDF-файла и экспорта его данных в структурированный файл XFDF.

1. Инициализируйте pdf_facades.Form() для управления данными формы PDF.
1. Вызовите 'bind_pdf()', чтобы прикрепить исходный PDF‑документ.
1. Используйте 'open()', чтобы создать двоичный поток с возможностью записи.
1. Экспортируйте данные формы. Вызовите 'export_xfdf()', чтобы извлечь и сохранить значения полей формы в формате XFDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```

