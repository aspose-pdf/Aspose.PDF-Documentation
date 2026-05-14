---
title: Поля кнопок и изображения
linktitle: Поля кнопок и изображения
type: docs
weight: 40
url: /ru/python-net/button-fields-and-images/
description: В этом примере демонстрируется, как управлять полями кнопок в PDF‑форме с использованием API Aspose.PDF Facades.
lastmod: "2026-02-19"
TechArticle: true
AlternativeHeadline: Добавление изображения к полям кнопок и чтение флагов отправки
Abstract: PDF‑формы часто содержат интерактивные кнопки, которые либо вызывают действия JavaScript, либо отправляют данные формы. Вы можете визуально улучшить поля кнопок, добавив изображения в качестве их внешнего вида, и программно проверять их поведение при отправке.
---

## Добавление изображения к полям кнопок

Этот фрагмент кода объясняет, как добавить изображение в качестве внешнего вида к существующему полю кнопки в PDF‑форме. Операция улучшает визуальное представление PDF‑кнопки, заменяя её внешний вид по умолчанию пользовательским изображением.

1. Создайте объект Form.
1. Привяжите PDF‑файл к объекту Form.
1. Добавьте изображение в поле Button Field.
    - Определите путь к файлу изображения, связанному с PDF
    - Откройте изображение в бинарном режиме как image_stream.
    - Вызовите fill_image_field() с полностью квалифицированным именем поля кнопки.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## Получение флагов отправки

Библиотека Python помогает получить флаги отправки кнопки отправки в PDF‑форме, используя API Aspose.PDF Facades. Флаги отправки определяют поведение кнопки отправки, например, отправляет ли она всю форму, включает ли аннотации или отправляет данные в формате FDF, XFDF, PDF или HTML.

1. Создайте объект Form.
1. Вызовите get_submit_flags() у объекта формы, используя полностью квалифицированное имя кнопки отправки.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```

