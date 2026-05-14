---
title: Извлечь данные XFA
type: docs
weight: 50
url: /python-net/extract-xfa-data/
description: В этом примере объясняется, как извлечь данные форм XFA из PDF‑файла с использованием Aspose.PDF for Python via .NET. Он демонстрирует, как привязать PDF‑документ на основе XFA к фасаду Form и экспортировать его внутреннюю структуру данных в поток файла.
lastmod: "2026-02-19"
---

Формы XFA (XML Forms Architecture) отличаются от традиционных AcroForm, потому что их данные хранятся в виде XML внутри PDF. В этом примере [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) объект из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуля используется для привязки PDF и извлечения его данных XFA непосредственно в файл.

1. Создайте экземпляр pdf_facades.Form() для управления данными формы.
1. Вызовите 'bind_pdf()', чтобы присоединить исходный PDF, содержащий формы XFA.
1. Используйте 'FileIO()' для создания записываемого файлового потока.
1. Вызовите функцию 'extract_xfa_data()' для экспорта встроенных XML-данных XFA.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```
