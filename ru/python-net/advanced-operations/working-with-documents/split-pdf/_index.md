---
title: Разделить PDF-файлы в Python
linktitle: Разделить PDF-файлы
type: docs
weight: 60
url: /ru/python-net/split-pdf-document/
description: Узнайте, как разделить PDF‑файлы в Python на отдельные страницы, равные части, группы фиксированного размера, пользовательские диапазоны страниц, а также нечётные или чётные страницы.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделите PDF на страницы и диапазоны страниц с помощью Python.
Abstract: В этой статье показано, как разбивать PDF‑файлы с помощью Aspose.PDF for Python via .NET. Описывается разбиение PDF на отдельные страницы, две равные части, группы страниц фиксированного размера, пользовательские диапазоны страниц, именованные группы страниц, стабильные имена файлов, а также файлы с нечётными или чётными страницами.
---

Эта страница показывает, как **разделять PDF-файлы в Python** с помощью Aspose.PDF for Python via .NET.

Используйте эти примеры, когда вам нужно разбить большой PDF на одностраничные файлы, равные части, группы фиксированного размера, пользовательские диапазоны страниц или наборы нечётных и чётных страниц для распространения, проверки или последующей обработки.

## Пример онлайн-разделения PDF

[Aspose.PDF Разделитель](https://products.aspose.app/pdf/splitter) Это онлайн веб‑приложение, которое позволяет тестировать функцию разделения PDF.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Чтобы разбить страницы PDF на отдельные PDF‑файлы по одной странице в Python, выполните следующие действия:

1. Перебрать страницы PDF‑документа через [Документ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объекта [Коллекция страниц](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) коллекция
1. Для каждой итерации создайте новый объект Document и добавьте отдельный [Страница](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) объект в пустой документ
1. Сохраните новый PDF, используя [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод

## Разделить PDF на несколько файлов в Python

Следующий фрагмент кода Python показывает, как разделить страницы PDF на отдельные PDF‑файлы.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## Разделить PDF на две равные части

1. Загрузите PDF документ.
1. Определить общее количество страниц.
1. Вычислите середину.
1. Создайте первый документ вывода.
1. Удалите страницы второй половины из первого документа.
1. Сохраните первую часть.
1. Создайте второй выходной документ.
1. Удалите страницы первой половины второго документа.
1. Сохраните вторую часть.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## Разделить PDF на несколько файлов каждые N страниц

Разделите PDF‑документ на несколько более мелких файлов, основываясь на фиксированном количестве страниц, используя Aspose.PDF для Python.

1. Загрузите PDF документ.
1. Определить общее количество страниц.
1. Определите количество страниц на часть.
1. Итерируйте документ частями.
1. Вычислите диапазон страниц для каждой части.
1. Создайте новый документ для каждой части.
1. Скопировать страницы в новый документ.
1. Сохраните разделённый документ.
1. Повторяйте, пока не будут обработаны все страницы.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## Разделить PDF по пользовательским диапазонам страниц

Разделить PDF‑документ на несколько файлов на основе пользовательски определённых диапазонов страниц с использованием Aspose.PDF for Python.

1. Загрузите PDF документ.
1. Определить общее количество страниц.
1. Создайте список кортежей, представляющих диапазоны (start_page, end_page).
1. Итерировать по определённым диапазонам.
1. Проверьте стартовую страницу.
1. Отрегулировать конечную страницу.
1. Проверьте эффективный диапазон.
1. Создайте новый документ для каждого диапазона.
1. Скопировать страницы в новый документ.
1. Сохраните каждый разделённый документ.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## Разделить PDF на первую страницу и остальные страницы

Отделите первую страницу PDF‑документа от остальных страниц с помощью Aspose.PDF for Python.

1. Загрузите PDF документ.
1. Определить общее количество страниц.
1. Проверьте, пустой ли документ.
1. Создайте документ для первой страницы.
1. Добавьте первую страницу.
1. Сохраните документ первой страницы.
1. Проверьте, есть ли дополнительные страницы.
1. Создайте документ для оставшихся страниц.
1. Скопировать оставшиеся страницы.
1. Сохраните документ со оставшимися страницами.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## Разделить PDF на последнюю страницу и предыдущие страницы

Извлеките последнюю страницу PDF‑документа и отделите её от оставшихся страниц, используя Aspose.PDF for Python.

1. Загрузите PDF документ.
1. Определить общее количество страниц.
1. Проверьте, пустой ли документ.
1. Создайте документ для последней страницы.
1. Добавьте последнюю страницу.
1. Сохраните документ последней страницы.
1. Проверьте одностраничные документы.
1. Удалите последнюю страницу из оригинального документа.
1. Сохраните оставшиеся страницы.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## Разделить PDF на три части

Разделите документ PDF на три отдельные части, используя Aspose.PDF for Python.

1. Загрузите PDF документ.
1. Определить общее количество страниц.
1. Проверьте, пустой ли документ.
1. Вычислить размер части.
1. Перебрать три части.
1. Определите диапазон страниц для каждой части.
1. Проверьте диапазон страниц.
1. Создайте новый документ для каждой части.
1. Скопировать страницы в часть документа.
1. Сохраните каждую часть.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## Пользовательский разделитель страниц PDF

Разделить документ PDF на несколько файлов на основе пользовательски определённых групп страниц с использованием Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## Разделить PDF на отдельные страницы со стабильными именами файлов

Разделите PDF‑документ на отдельные страницы и сохраните их с устойчивыми именами файлов, используя Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## Разделить PDF на нечётные и чётные страницы

Разделите PDF‑документ на два отдельных файла, содержащих соответственно нечётные и чётные страницы, используя Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## Связанные темы документа

- [Работайте с PDF-документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Объединить PDF-файлы в Python](/pdf/ru/python-net/merge-pdf-documents/)
- [Оптимизировать PDF‑файлы в Python](/pdf/ru/python-net/optimize-pdf/)
- [Манипулировать PDF-документами в Python](/pdf/ru/python-net/manipulate-pdf-document/)

