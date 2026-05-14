---
title: Переименовать поля формы
type: docs
weight: 30
url: /python-net/rename-form-fields/
description: Это пример демонстрирует, как переименовать поля формы в PDF‑документе с помощью Aspose.PDF for Python via .NET. Показано, как привязать PDF‑форму, программно обновить существующие имена полей и сохранить изменённый файл. Переименование полей помогает стандартизировать структуру формы, улучшить сопоставление данных и упростить интеграцию с автоматизированными рабочими процессами или внешними системами.
lastmod: "2026-02-19"
---

Переименование полей формы полезно при согласовании PDF‑форм с внутренними правилами именования или подготовке документов для обработки структурированных данных. В этом примере, [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад из [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) модуля используется для привязки исходного PDF и применения сопоставления, которое заменяет старые имена полей новыми. После обновления идентификаторов полей документ сохраняется с применёнными изменениями.

1. Инициализируйте pdf_facades.Form() для работы с полями PDF-формы.
1. Вызовите 'bind_pdf()', чтобы присоединить PDF‑документ.
1. Создайте список кортежей, содержащих старые имена полей и их соответствующие новые имена.
1. Итерируйте по отображению и вызывайте 'rename_field()' для каждой записи.
1. Сохраните обновлённый Document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
