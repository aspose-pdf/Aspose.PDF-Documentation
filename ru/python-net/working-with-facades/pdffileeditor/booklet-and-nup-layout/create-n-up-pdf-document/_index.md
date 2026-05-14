---
title: Создать N-Up PDF документ
type: docs
weight: 10
url: /python-net/create-n-up-pdf-document/
description: Узнайте, как создать N-Up PDF документ, безопасно обрабатывая потенциальные ошибки, используя Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать N-Up PDF Layout в Python
Abstract: Узнайте, как сгенерировать N-Up PDF layout, используя Aspose.PDF for Python. Этот пример демонстрирует, как объединить несколько страниц PDF‑документа на одну страницу, используя метод «make_n_up» или «try_make_n_up» класса PdfFileEditor.
---

N-Up layout размещает несколько страниц PDF‑документа на одной странице в виде сетки. Такой макет часто используется для печати презентаций, раздаточных материалов или отчётов, когда необходимо просмотреть сразу несколько страниц.

С помощью Aspose.PDF for Python разработчики могут быстро создать N-Up документ, указав количество строк и столбцов, определяющих, сколько оригинальных страниц будет размещено на каждой выходной странице.

В этом фрагменте кода метод 'make_n_up' класса [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) располагает страницы входного PDF в сетке 2 × 2, что означает, что четыре оригинальные страницы появляются на одной странице в выходном документе.

В показанном примере макет использует 2 строки и 2 столбца, получая четыре страницы на листе:

1. Откройте исходный PDF‑файл.
1. Создайте экземпляр PdfFileEditor.
1. Укажите количество строк и столбцов для компоновки N‑Up.
1. Создайте новый PDF с объединёнными страницами.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

Aspose.PDF for Python via .NET позволяет генерировать N-Up макеты с помощью класса PdfFileEditor. Метод 'try_make_n_up' работает аналогично make_n_up, но вместо того чтобы возбуждать исключение при неудачной операции, он возвращает логическое значение, указывающее, успешно ли процесс завершён.

Макет N-Up располагает несколько страниц PDF на одной странице, используя сетку, определённую строками и столбцами.

Метод 'try_make_n_up' предоставляет более безопасный способ выполнения этой операции, потому что:

- Он возвращает True, если макет успешно создан
- Он возвращает False, если операция не удалась
- Он не прерывает выполнение программы исключениями

В примере ниже документ располагается с использованием сетки 2 × 2, что размещает четыре оригинальные страницы на каждой выходной странице.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```
