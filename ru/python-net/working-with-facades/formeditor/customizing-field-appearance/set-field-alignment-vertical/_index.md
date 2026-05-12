---
title: Установить вертикальное выравнивание поля
type: docs
weight: 40
url: /python-net/set-field-alignment-vertical/
description: Этот пример демонстрирует, как установить вертикальное выравнивание поля формы в PDF‑документе с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить вертикальное выравнивание полей формы PDF с помощью Python
Abstract: В этой статье объясняется, как открыть PDF, установить вертикальное выравнивание поля с помощью класса FormEditor и сохранить обновлённый PDF. Пример устанавливает вертикальное выравнивание поля с именем "First Name" в нижнюю часть области поля.
---

PDF‑поля формы могут содержать текст, которому требуется правильное вертикальное выравнивание для согласованного и профессионального вида. С помощью Aspose.PDF for Python разработчики могут программно изменять вертикальное выравнивание полей формы.
Вертикальное выравнивание позволяет разработчикам контролировать, будет ли текст поля располагаться в верхней, центральной или нижней части ограничивающего поля, улучшая макет и читаемость данных формы.

Используя [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс и [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) константы, разработчики могут программно регулировать вертикальное выравнивание, чтобы достичь согласованного расположения формы:

1. Откройте существующий PDF‑документ.
1. Создать объект FormEditor.
1. Установите вертикальное выравнивание поля с именем "First Name" в нижнее положение.
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


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```
