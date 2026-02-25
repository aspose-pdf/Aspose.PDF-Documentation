---
title: Добавление штампов страниц в PDF с помощью Python
linktitle: Добавление штампов страниц
type: docs
weight: 30
url: /ru/python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF для Python через .NET позволяет добавить штамп страницы в ваш PDF-файл.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить штампы страниц в PDF с использованием Python
Abstract: В этой статье объясняется, как добавить штамп страницы в PDF‑документ с использованием Aspose.PDF для Python. Штамп страницы позволяет накладывать или подложить содержимое — такие как логотипы, водяные знаки или аннотации — на конкретную страницу в PDF. В примере показано, как открыть существующий PDF, создать объект PdfPageStamp из другой страницы PDF, настроить его как фоновой штамп и применить к определённой странице. Затем штампованный PDF сохраняется как новый документ. Эта техника полезна для брендинга, водяных знаков или выделения содержимого на уровне страниц в автоматизированных PDF‑рабочих процессах.
---

Aspose.PDF для Python через .NET показывает, как применить штамп страницы (водяной знак или наложение) к конкретной странице в PDF [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Штамп страницы может быть существующей страницей PDF, использованной в качестве фонового или переднего слоя (см. [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Это полезно для добавления логотипов, водяных знаков или другого повторяющегося содержимого страниц.

1. Откройте PDF‑документ, используя `ap.Document()` (см. [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Создайте объект `PdfPageStamp`, используя страницу PDF или файл, который будет использоваться в качестве штампа (см. [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Установите свойства штампа, например, `background = True`, чтобы разместить его за содержимым.
1. Добавьте штамп на конкретную страницу, используя `document.pages[page_number].add_stamp(page_stamp)` (см. [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) и [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Сохраните изменённый PDF в указанный выходной файл с помощью [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

