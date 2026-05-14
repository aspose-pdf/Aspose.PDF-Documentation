---
title: Импортировать данные XFDF
linktitle: Импортировать данные XFDF
type: docs
weight: 20
url: /python-net/import-xfdf-data/
description: В этом примере демонстрируется, как импортировать данные формы из файла XFDF в форму PDF с использованием Aspose.PDF for Python via .NET. Показано, как привязать документ PDF, читать XML‑основанные данные XFDF через файловый поток и автоматически заполнять соответствующие поля формы. Импорт данных XFDF обеспечивает эффективный обмен данными форм и поддерживает автоматизированные рабочие процессы с документами, которые опираются на структурированные форматы XML.
lastmod: "2026-02-19"
---

XFDF (XML Forms Data Format) — это XML‑представление данных формы PDF, разработанное для совместимости и обмена данными. В этом примере [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуля используется для привязки формы PDF и импорта значений полей из внешнего файла XFDF. После импорта данных обновлённый PDF сохраняется как новый документ.

1. Инициализируйте pdf_facades.Form() для работы с полями PDF-формы.
1. Вызовите 'bind_pdf()' для присоединения шаблона PDF‑формы.
1. Используйте 'open()' для чтения файла XFDF.
1. Вызовите 'import_xfdf()', чтобы заполнить поля PDF значениями из файла XFDF.
1. Сохраните обновлённый Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
