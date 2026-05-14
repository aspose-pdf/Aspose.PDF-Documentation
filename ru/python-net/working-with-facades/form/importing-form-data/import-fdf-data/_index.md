---
title: Импортировать данные FDF
linktitle: Импортировать данные FDF
type: docs
weight: 10
url: /python-net/import-fdf-data/
description: В этом примере демонстрируется, как импортировать данные формы из файла FDF в PDF‑форму с использованием Aspose.PDF for Python via .NET. Показано, как привязать PDF‑документ, считать значения полей формы из потока FDF и автоматически заполнить соответствующие поля.
lastmod: "2026-02-19"
---

FDF (Forms Data Format) — это легковесный формат, используемый для хранения и передачи значений полей PDF‑формы без включения всего документа. В этом примере the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) используется для загрузки PDF‑формы и импорта данных полей из внешнего файла FDF. После процесса импорта обновлённый PDF сохраняется как новый файл.

1. Инициализируйте pdf_facades.Form() для работы с интерактивными полями PDF‑формы.
1. Вызовите 'bind_pdf()' для присоединения шаблона PDF‑формы.
1. Используйте 'open()' для чтения FDF‑файла в бинарном режиме.
1. Вызовите 'import_fdf()' для заполнения полей PDF данными из FDF‑файла.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
