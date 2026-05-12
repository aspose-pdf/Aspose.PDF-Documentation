---
title: Получить внешний вид поля
type: docs
weight: 20
url: /python-net/get-field-appearance/
description: В этой статье объясняется, как открыть PDF, получить доступ к полю формы, извлечь его настройки внешнего вида и отобразить их. Пример демонстрирует извлечение внешнего вида поля с именем "Last Name".
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить внешний вид поля формы PDF с использованием Python
Abstract: В этом примере показано, как получить свойства визуального оформления поля формы в PDF‑документе с помощью Aspose.PDF for Python. Код открывает существующий PDF, получает доступ к определённому полю формы и выводит детали его оформления, включая цвет фона, цвет текста, цвет рамки и выравнивание.
---

Поля формы в PDF‑документах имеют визуальные свойства, такие как цвет фона, цвет текста, цвет рамки и выравнивание. С помощью Aspose.PDF for Python разработчики могут программно проверять эти настройки оформления, используя [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) класс.

1. Откройте существующий PDF‑документ.
1. Создать объект FormEditor.
1. Получить информацию о внешнем виде конкретного поля.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))
```
