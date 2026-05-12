---
title: Создать PDF‑буклет
type: docs
weight: 20
url: /python-net/create-pdf-booklet/
description: Создать PDF‑буклет из существующего документа с использованием Aspose.PDF for Python
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать PDF‑буклет из существующего PDF с помощью Python
Abstract: Узнайте, как создать PDF‑буклет из существующего документа, используя Aspose.PDF for Python. В этом примере показано, как использовать класс PdfFileEditor для перестановки страниц, чтобы их можно было печатать и складывать в виде буклета. Метод автоматически упорядочивает страницы, создавая корректную компоновку буклета.
---

Создание документов в виде буклета является обычным требованием при подготовке PDF для печати. В макете буклета страницы переставляются таким образом, чтобы после печати и складывания они находились в правильном порядке.

С помощью Aspose.PDF for Python разработчики могут легко преобразовать обычный PDF в буклет, используя [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class. Метод 'make_booklet' автоматически переупорядочивает страницы входного документа и создает новый PDF, оптимизированный для печати в виде книжки.

1. Откройте существующий PDF‑документ.
1. Создайте экземпляр PdfFileEditor.
1. Используйте метод make_booklet для переупорядочивания страниц.
1. Сохраните результат как PDF‑файл, готовый к печати в виде книжки.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

Этот фрагмент кода показывает, как использовать метод 'try_make_booklet' [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) класса для перестановки страниц при печати буклета без генерации исключений, если операция завершится с ошибкой.

Макет буклета переставляет страницы так, что после печати и сгибания документ читается в правильном порядке. Автоматизация этого процесса обеспечивает постоянные результаты и устраняет необходимость ручного переставления страниц.

Метод 'try_make_booklet' работает аналогично 'make_booklet', но с важным отличием:

- 'make_booklet' генерирует исключение, если операция не удалась.
- 'try_make_booklet' возвращает True или False, позволяя разработчикам более безопасно обрабатывать ошибки.

1. Откройте существующий PDF‑документ.
1. Создайте экземпляр PdfFileEditor.
1. Попытка создать буклет.
1. Обработать результат.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
