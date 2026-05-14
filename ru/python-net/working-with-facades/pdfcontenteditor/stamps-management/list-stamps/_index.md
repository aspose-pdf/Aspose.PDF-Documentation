---
title: Список штампов
linktitle: Список штампов
type: docs
weight: 70
url: /ru/python-net/list-stamps/
description: Этот пример загружает PDF, извлекает все штампы со страницы 1, выводит их и отображает сообщение, если штампы не найдены.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Список аннотаций резиновых штампов в PDF с использованием PdfContentEditor в Python
Abstract: Этот пример демонстрирует, как извлечь и перечислить аннотации резиновых штампов из PDF‑документа с использованием Aspose.PDF for Python via the Facades API. Он показывает, как получить доступ к штампам на определенной странице и отобразить их детали.
---

При работе с аннотированными PDF вам может потребоваться проверить существующие резиновые штампы перед их изменением или удалением. Метод 'get_stamps()' позволяет получить все штампы, размещённые на конкретной странице. Затем вы можете пройтись по результатам и обработать их программно.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Извлеките все штампы со страницы 1.
1. Переберите коллекцию штампов.
1. Выведите каждый штамп.
1. Отобразите сообщение, если штампы отсутствуют.

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

