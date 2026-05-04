---
title: Добавить штампы страниц в PDF с помощью Python
linktitle: Добавление штампов страниц
type: docs
weight: 30
url: /python-net/page-stamps-in-the-pdf-file/
description: Узнайте, как добавить штампы страниц PDF в виде наложений или фонов с помощью Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить штампы страниц в PDF с использованием Python
Abstract: В этой статье объясняется, как добавить штамп страницы в документ PDF с использованием Aspose.PDF for Python. Штамп страницы позволяет накладывать или подложить содержимое — например, логотипы, водяные знаки или аннотации — на конкретную страницу в PDF. В примере показано, как открыть существующий PDF, создать объект PdfPageStamp из другой страницы PDF, настроить его как фоновой штамп и применить к определённой странице. Затем полученный PDF сохраняется как новый документ. Эта техника полезна для брендинга, создания водяных знаков или выделения содержимого на уровне страниц в автоматизированных PDF‑рабочих процессах.
---

Aspose.PDF for Python via .NET демонстрирует, как применить штамп страницы (водяной знак или наложение) к конкретной странице в PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Штамп страницы может быть существующей страницей PDF, используемой в качестве фонового или переднего слоя (см [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Это полезно для добавления логотипов, водяных знаков или другого повторяющегося содержимого страниц.

1. Откройте PDF‑документ, используя `ap.Document()` (см [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Создайте `PdfPageStamp` объект, использующий страницу PDF или файл в качестве штампа (см [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Установите свойства штампа, например, `background = True` разместить его за содержимым.
1. Добавьте штамп на конкретную страницу, используя `document.pages[page_number].add_stamp(page_stamp)` (см [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) и [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Сохраните изменённый PDF в указанный файл вывода, используя [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

## Связанные темы штампования

- [Нанести штамп на страницы PDF в Python](/pdf/ru/python-net/stamping/)
- [Добавить номера страниц в PDF с помощью Python](/pdf/ru/python-net/add-page-number/)
- [Добавить штампы изображений в PDF на Python](/pdf/ru/python-net/image-stamps-in-pdf-page/)
- [Добавить текстовые штампы в PDF на Python](/pdf/ru/python-net/text-stamps-in-the-pdf-file/)