---
title: Объединить PDF‑формы с уникальным суффиксом
type: docs
weight: 50
url: /python-net/concatenate-pdf-forms/
description: Объедините несколько PDF‑форм, используя Aspose.PDF for Python, обеспечивая уникальность имён полей формы.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединяйте PDF‑формы в Python, избегая конфликтов имён полей.
Abstract: Узнайте, как объединять несколько PDF‑форм, используя Aspose.PDF for Python, обеспечивая уникальность имён полей формы. Этот пример демонстрирует, как задать пользовательский суффикс для предотвращения конфликтов имён при объединении PDF, содержащих интерактивные поля формы.
---

Объединение PDF‑форм может привести к конфликтам, если несколько файлов содержат поля с одинаковыми именами. С помощью Aspose.PDF for Python разработчики могут задавать уникальный суффикс полям формы во время объединения. Свойство unique_suffix в [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) класс автоматически переименовывает конфликтующие поля, сохраняя интерактивность и гарантируя, что все данные формы остаются работоспособными. Этот подход идеален для программного комбинирования опросов, заявок или любых интерактивных PDF‑документов.

1. Создайте объект PdfFileEditor и задайте уникальный суффикс.
1. Объединить PDF-формы.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_forms(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.unique_suffix = (
        "_xy_%NUM%"  # Set a unique suffix to avoid form field name conflicts
    )
    pdf_editor.concatenate(files_to_merge, output_file)
```
