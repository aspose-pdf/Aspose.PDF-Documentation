---
title: Экспорт в XML
linktitle: Экспорт в XML
type: docs
weight: 40
url: /ru/python-net/export-to-xml/
description: В этом примере демонстрируется, как экспортировать данные формы PDF в файл XML с использованием Aspose.PDF for Python via .NET. Показано, как загрузить PDF‑документ, получить доступ к полям формы через фасад Form и сохранить извлечённые данные в виде структурированного XML с использованием класса Form.
lastmod: "2026-02-19"
---

Экспорт данных формы позволяет разработчикам повторно использовать информацию, хранящуюся в PDF AcroForms, без ручного копирования значений полей. В этом примере, a [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) объект создаётся из aspose.pdf. В модуле facades исходный PDF привязывается к нему, и данные формы записываются в поток XML.

1. Создайте объект Form. Инициализируйте pdf_facades.Form() для доступа и управления полями формы.
1. Используйте 'bind_pdf()' для привязки исходного PDF‑документа к экземпляру Form.
1. Создайте поток записываемого файла, используя 'FileIO()'.
1. Вызовите 'export_xml()', чтобы извлечь все значения полей формы и записать их в XML‑файл.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```

