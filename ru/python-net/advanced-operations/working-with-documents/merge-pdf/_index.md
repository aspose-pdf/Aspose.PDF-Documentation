---
title: Объединить PDF-файлы в Python
linktitle: Объединить PDF-файлы
type: docs
weight: 50
url: /ru/python-net/merge-pdf-documents/
description: Узнайте, как объединить несколько PDF‑файлов в один документ с помощью Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Объединяйте страницы PDF с помощью Python
Abstract: В этой статье рассматривается распространённая необходимость объединения нескольких PDF‑файлов в один документ, процесс, полезный для организации, оптимизации хранения и совместного использования PDF‑контента. Описывается использование Aspose.PDF for Python via .NET для эффективного сочетания PDF‑файлов, с учётом того, что объединение PDF в Python может быть сложным без сторонних библиотек. Статья представляет пошаговое руководство по конкатенации PDF‑файлов — создание нового документа, объединение файлов и сохранение объединённого документа. Фрагмент кода демонстрирует реализацию с использованием Aspose.PDF, подчёркивая возможность библиотеки упростить процесс объединения. Кроме того, представляется Aspose.PDF Merger — онлайн‑инструмент для объединения PDF, позволяющий пользователям исследовать функциональность в веб‑среде.
---

## Объединить или совместить несколько PDF в один PDF на Python

Объединение PDF‑файлов — очень популярный запрос среди пользователей. Это может быть полезно, когда у вас есть несколько PDF‑файлов, которые вы хотите объединить или хранить вместе как один документ.

Объединение PDF‑файлов может помочь вам упорядочить документы, освободить место для хранения на вашем ПК и поделиться несколькими PDF‑файлами с другими, объединив их в один документ.

Объединение PDF в Python через .NET не является простой задачей без использования сторонней библиотеки.
В этой статье показано, как объединить несколько PDF-файлов в один PDF‑документ с помощью Aspose.PDF for Python via .NET. 

## Объединение PDF-файлов с помощью Python и DOM

Для объединения двух PDF файлов:

1. Создайте новый документ.
1. Объедините PDF‑файлы
1. Сохраните объединённый документ

Объединение нескольких PDF‑документов в один файл:

```python
import sys
import aspose.pdf as ap
from os import path


def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Добавить диапазон страниц из одного PDF в другой

Скопировать и добавить определённый диапазон страниц из исходного PDF‑документа в целевой PDF‑документ с использованием Aspose.PDF for Python.

1. Откройте PDF‑файлы, используя класс Document.
1. Проверьте, есть ли у исходного документа страницы.
1. Проверьте диапазон страниц.
1. Пропустите операцию, если начальная страница больше конечной страницы.
1. Итерируйте диапазон страниц.
1. Добавьте страницы к целевому документу.

```python
import sys
import aspose.pdf as ap
from os import path


def _append_page_range(source_document, destination_document, start_page, end_page):
    total_pages = len(source_document.pages)
    if total_pages == 0:
        return

    start = max(1, start_page)
    end = min(end_page, total_pages)
    if start > end:
        return

    for page_number in range(start, end + 1):
        destination_document.pages.add(source_document.pages[page_number])
```

## Объединить несколько PDF‑документов в один

Этот фрагмент кода объясняет, как объединить несколько PDF‑файлов в один документ:

1. Создайте пустой выходной документ.
1. Переберите входные файлы.
1. Загрузите каждый исходный документ.
1. Определите диапазон страниц.
1. Добавьте страницы к выходному документу.
1. Повторите для всех документов.
1. Сохраните объединенный PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_multiple_documents(input_files, outfile):
    output_document = ap.Document()

    for input_file in input_files:
        source_document = ap.Document(input_file)
        _append_page_range(
            source_document, output_document, 1, len(source_document.pages)
        )

    output_document.save(outfile)
```

## Объединить выбранные диапазоны страниц из нескольких PDF

1. Загрузите исходные PDF‑документы.
1. Создайте выходной документ.
1. Определите диапазоны страниц для каждого документа.
1. Добавьте страницы из первого документа.
1. Добавьте страницы из второго документа.
1. Объедините страницы в нужном порядке.
1. Сохраните объединенный PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_selected_page_ranges(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    _append_page_range(document1, output_document, 1, 2)
    _append_page_range(document2, output_document, 2, 3)

    output_document.save(outfile)
```

## Вставить один PDF в другой в определённой позиции

1. Загрузите базу и вставьте документы.
1. Создайте выходной документ.
1. Определите общее количество страниц в базовом документе.
1. Проверьте индекс вставки.
1. Добавьте страницы перед точкой вставки.
1. Добавьте все страницы из вставляемого документа.
1. Добавьте оставшиеся страницы из базового документа.
1. Сохраните полученный PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_insert_document_at_position(infile1, infile2, insert_after_page, outfile):
    base_document = ap.Document(infile1)
    insert_document = ap.Document(infile2)
    output_document = ap.Document()

    base_total_pages = len(base_document.pages)
    insert_index = max(0, min(insert_after_page, base_total_pages))

    _append_page_range(base_document, output_document, 1, insert_index)
    _append_page_range(insert_document, output_document, 1, len(insert_document.pages))
    _append_page_range(
        base_document, output_document, insert_index + 1, base_total_pages
    )

    output_document.save(outfile)
```

## Объединить PDF‑файлы, чередуя страницы

В этом примере демонстрируется, как объединить два PDF‑документа, чередуя их страницы, используя Aspose.PDF for Python.

1. Загрузите входные PDF‑документы.
1. Создайте выходной документ.
1. Получите количество страниц в каждом документе.
1. Вычислите максимальное количество страниц.
1. Переберите номера страниц.
1. Добавляйте страницы попеременно.
1. Обработайте неравное количество страниц.
1. Сохраните объединенный PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_alternating_pages(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    document1_pages = len(document1.pages)
    document2_pages = len(document2.pages)
    max_pages = max(document1_pages, document2_pages)

    for page_number in range(1, max_pages + 1):
        if page_number <= document1_pages:
            output_document.pages.add(document1.pages[page_number])
        if page_number <= document2_pages:
            output_document.pages.add(document2.pages[page_number])

    output_document.save(outfile)
```

## Объединить PDF-файлы с разделителями секций и закладками

Объедините несколько PDF‑документов в один файл со структурированными разделами и навигационными закладками, используя Aspose.PDF for Python.

1. Создайте выходной документ.
1. Переберите входные файлы.
1. Загрузите исходный документ.
1. Добавьте страницу-разделитель.
1. Создайте закладку раздела.
1. Добавьте страницы исходного документа.
1. Отслеживайте первую страницу контента.
1. Добавьте вложенную закладку контента (по желанию).
1. Повторите для всех документов.
1. Сохраните объединенный PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_with_section_separators_and_bookmarks(input_files, outfile):
    output_document = ap.Document()

    for section_index, input_file in enumerate(input_files, start=1):
        source_document = ap.Document(input_file)
        source_page_count = len(source_document.pages)

        separator_page = output_document.pages.add()
        separator_page.paragraphs.add(
            ap.text.TextFragment(
                f"Section {section_index}: {path.basename(input_file)}"
            )
        )

        section_bookmark = ap.OutlineItemCollection(output_document.outlines)
        section_bookmark.title = f"Section {section_index}"
        section_bookmark.action = ap.annotations.GoToAction(separator_page)
        output_document.outlines.append(section_bookmark)

        first_content_page_number = len(output_document.pages) + 1
        _append_page_range(source_document, output_document, 1, source_page_count)

        if source_page_count > 0 and first_content_page_number <= len(
            output_document.pages
        ):
            content_bookmark = ap.OutlineItemCollection(output_document.outlines)
            content_bookmark.title = f"Section {section_index} Content"
            content_bookmark.action = ap.annotations.GoToAction(
                output_document.pages[first_content_page_number]
            )
            section_bookmark.append(content_bookmark)

    output_document.save(outfile)
```

## Рабочий пример

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) это онлайн бесплатное веб‑приложение, которое позволяет исследовать, как работает функция объединения презентаций.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Связанные темы Document

- [Работа с PDF документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Разделить PDF файлы в Python](/pdf/ru/python-net/split-document/)
- [Оптимизировать PDF файлы в Python](/pdf/ru/python-net/optimize-pdf/)
- [Манипулировать PDF документами в Python](/pdf/ru/python-net/manipulate-pdf-document/)

