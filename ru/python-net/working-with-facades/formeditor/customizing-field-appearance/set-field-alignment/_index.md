---
title: Установить выравнивание поля
type: docs
weight: 30
url: /python-net/set-field-alignment/
description: В этом примере показано, как установить выравнивание текста в поле формы в PDF‑документе с использованием Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить выравнивание текста для полей формы PDF с помощью Python
Abstract: В этой статье объясняется, как открыть PDF‑документ, установить выравнивание определённого поля с использованием класса FormEditor и сохранить обновлённый PDF. В примере выравнивание текста поля с именем "First Name" устанавливается по центру.
---

Полям формы PDF часто требуется пользовательское выравнивание текста для поддержания единообразного и профессионального оформления. С помощью Aspose.PDF for Python разработчики могут программно задавать выравнивание текстового содержимого поля формы.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс, в сочетании с [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) константы, позволяют разработчикам программно изменять выравнивание существующих полей формы.

1. Откройте существующий PDF‑документ.
1. Создать объект FormEditor.
1. Установите выравнивание поля с именем "First Name" по центру.
1. Сохраните изменённый документ.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```
