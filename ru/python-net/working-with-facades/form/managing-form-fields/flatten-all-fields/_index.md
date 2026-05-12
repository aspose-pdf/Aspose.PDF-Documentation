---
title: Сгладить все поля
type: docs
weight: 10
url: /python-net/flatten-all-fields/
description: В этом примере демонстрируется, как сгладить все поля формы в PDF, используя Aspose.PDF for Python via .NET. Показано, как привязать PDF‑документ, преобразовать каждый интерактивный элемент формы в статическое содержимое страницы и сохранить окончательный файл.
lastmod: "2026-02-19"
---

Сглаживание удаляет интерактивность из PDF‑форм, объединяя значения полей напрямую в макет документа. В этом примере [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) используется для привязки исходного PDF и применения метода flatten_all_fields(), который преобразует все поля в не редактируемое содержимое.

1. Инициализируйте pdf_facades.Form() для работы с полями PDF-формы.
1. Вызовите 'bind_pdf()', чтобы присоединить исходный документ.
1. Вызовите 'flatten_all_fields()', чтобы преобразовать все интерактивные поля в статическое содержимое.
1. Сохраните обновлённый Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```
