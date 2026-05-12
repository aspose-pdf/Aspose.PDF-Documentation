---
title: Список штампов
type: docs
weight: 70
url: /python-net/list-stamps/
description: В этом примере загружается PDF, извлекаются все штампы со страницы 1, они выводятся, и отображается сообщение, если штампы не найдены.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Список аннотаций резиновых штампов в PDF с использованием PdfContentEditor в Python
Abstract: В этом примере демонстрируется, как извлечь и перечислить аннотации резиновых штампов из PDF‑документа с помощью Aspose.PDF for Python через API фасадов. Показано, как получить доступ к штампам на конкретной странице и отобразить их детали.
---

При работе с аннотированными PDF может потребоваться проанализировать существующие резиновые штампы перед их изменением или удалением. Метод 'get_stamps()' позволяет получить все штампы, размещённые на конкретной странице. Затем вы можете перебрать результаты и обработать их программно.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Получить все штампы со страницы 1.
1. Перебрать коллекцию штампов.
1. Вывести каждый штамп.
1. Отобразить сообщение, если штампы отсутствуют.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```
