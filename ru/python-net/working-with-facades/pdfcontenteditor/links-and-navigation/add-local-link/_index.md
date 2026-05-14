---
title: Добавить локальную ссылку
linktitle: Добавить локальную ссылку
type: docs
weight: 40
url: /python-net/add-local-link/
description: В этом примере привязывается входной PDF, добавляется локальная ссылка красного цвета на странице 1 и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить локальную ссылку в PDF с помощью PdfContentEditor на Python
Abstract: В этом примере демонстрируется, как добавить локальную ссылку в PDF‑документ с использованием Aspose.PDF for Python через Facades API. Показано, как создать щелкаемую область, которая переходит на другую страницу внутри того же PDF, и сохранить обновлённый документ.
---

Локальные ссылки в PDF позволяют быстро перемещаться между страницами в рамках одного документа. С помощью [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), можно определить щелкаемый прямоугольник, который связывает одну страницу с другой, улучшая удобство использования и навигацию по документу.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольник для кликабельной локальной ссылки.
1. Укажите исходную страницу и страницу назначения.
1. Установите цвет ссылки.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
