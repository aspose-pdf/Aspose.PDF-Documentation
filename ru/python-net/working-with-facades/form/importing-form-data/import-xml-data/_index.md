---
title: Импорт данных XML
type: docs
weight: 40
url: /python-net/import-xml-data/
description: В этом примере демонстрируется, как импортировать данные формы из XML‑файла в поля формы PDF с использованием Aspose.PDF for Python via .NET. Показано, как привязать документ PDF, прочитать структурированные XML‑данные через файловый поток и автоматически заполнить соответствующие поля формы.
lastmod: "2026-02-19"
---

XML часто используется для хранения структурированных данных формы, что делает его практичным форматом для передачи значений между системами. В этом примере [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) используется для загрузки формы PDF и применения значений полей непосредственно из XML‑файла. После импорта данных обновлённый PDF сохраняется как новый документ.

1. Инициализируйте pdf_facades.Form() для работы с полями PDF-формы.
1. Вызовите 'bind_pdf()' для присоединения шаблона PDF‑формы.
1. Используйте 'FileIO()' для доступа к XML‑файлу, содержащему данные формы.
1. Вызовите 'import_xml()' для заполнения полей PDF значениями из XML‑файла.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
