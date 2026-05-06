---
title: Разделить PDF-файлы на Python
linktitle: Разделить PDF-файлы
type: docs
weight: 60
url: /ru/python-net/split-pdf-document/
description: Узнайте, как разделить страницы PDF на отдельные PDF‑файлы с помощью Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделение страниц PDF с использованием Python
Abstract: В статье рассматривается процесс разделения страниц PDF на отдельные файлы с использованием Python, подчеркивая полезность такой функции для управления крупными PDF‑документами. Упоминается Aspose.PDF Splitter — онлайн‑инструмент, предназначенный для демонстрации функции разделения PDF. В статье представлено подробное руководство по реализации этого в приложениях Python, включающее перебор страниц PDF‑документа через `Document` object's `PageCollection`. Для каждой страницы создаётся новый объект `Document`, страница добавляется к нему, и новый PDF‑файл сохраняется с помощью метода `save()`. Сопутствующий фрагмент кода на Python иллюстрирует процесс, показывая шаги, необходимые для разделения PDF‑документа на отдельные файлы путем перебора его страниц и сохранения каждой в виде отдельного PDF.
---

Разделение страниц PDF может быть полезной функцией для тех, кто хочет разделить большой файл на отдельные страницы или группы страниц.

Используйте этот рабочий процесс, когда вам нужно разбить большие PDF‑файлы на одностраничные файлы или более мелкие наборы документов для распределения, рецензирования или дальнейшей обработки.

## Рабочий пример

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) является бесплатным онлайн-приложением, которое позволяет исследовать, как работает функция разделения презентаций.

[![Aspose.PDF Splitter](splitter.png)](https://products.aspose.app/pdf/splitter)

В этой теме показано, как разделить страницы PDF на отдельные PDF‑файлы в ваших приложениях на Python. Чтобы разделить страницы PDF на одностраничные PDF‑файлы с помощью Python, можно выполнить следующие шаги:

1. Переберите страницы PDF‑документа [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объекта [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) коллекция
1. Для каждой итерации создавайте новый объект Document и добавляйте отдельный [Страница](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) объект в пустой документ
1. Сохраните новый PDF, используя [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод

## Разделить PDF на несколько файлов или отдельные PDF в Python

Следующий фрагмент кода на Python показывает, как разделить страницы PDF на отдельные PDF‑файлы.

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

1. Загрузите PDF-документ.
1. Определите общее количество страниц.
1. Вычислите середину.
1. Создайте первый выходной документ.
1. Удалите страницы второй половины из первого документа.
1. Сохраните первую часть.
1. Создайте второй документ вывода.
1. Удалите страницы первой половины из второго документа.
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

Разделите PDF‑документ на несколько более мелких файлов, основываясь на фиксированном количестве страниц, с помощью Aspose.PDF for Python.

1. Загрузите PDF-документ.
1. Определите общее количество страниц.
1. Определите количество страниц на часть.
1. Итерируйте документ по частям.
1. Вычислите диапазон страниц для каждой части.
1. Создайте новый документ для каждой части.
1. Скопируйте страницы в новый документ.
1. Сохраните разделенный документ.
1. Повторяйте, пока все страницы не будут обработаны.

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

Разделите PDF‑документ на несколько файлов на основе пользовательски заданных диапазонов страниц с использованием Aspose.PDF для Python.

1. Загрузите PDF-документ.
1. Определите общее количество страниц.
1. Создайте список кортежей, представляющих диапазоны (start_page, end_page).
1. Итерируйте по определённым диапазонам.
1. Проверьте начальную страницу.
1. Отрегулируйте конечную страницу.
1. Проверьте эффективный диапазон.
1. Создайте новый документ для каждого диапазона.
1. Скопируйте страницы в новый документ.
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

## Разделить PDF на первую страницу и оставшиеся страницы

Отделите первую страницу PDF‑документа от остальных страниц, используя Aspose.PDF for Python.

1. Загрузите PDF-документ.
1. Определите общее количество страниц.
1. Проверьте, пустой ли документ.
1. Создайте документ для первой страницы.
1. Добавьте первую страницу.
1. Сохраните документ первой страницы.
1. Проверьте, есть ли дополнительные страницы.
1. Создайте документ для оставшихся страниц.
1. Скопируйте оставшиеся страницы.
1. Сохраните документ оставшихся страниц.

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

Извлеките последнюю страницу PDF‑документа и отделите её от остальных страниц с помощью Aspose.PDF for Python.

1. Загрузите PDF-документ.
1. Определите общее количество страниц.
1. Проверьте, пустой ли документ.
1. Создайте документ для последней страницы.
1. Добавьте последнюю страницу.
1. Сохраните документ последней страницы.
1. Проверьте документы из одной страницы.
1. Удалите последнюю страницу из исходного документа.
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

Разделите PDF-документ на три отдельные части с помощью Aspose.PDF for Python.

1. Загрузите PDF-документ.
1. Определите общее количество страниц.
1. Проверьте, пустой ли документ.
1. Вычислите размер части.
1. Переберите три части.
1. Определите диапазон страниц для каждой части.
1. Проверьте диапазон страниц.
1. Создайте новый документ для каждой части.
1. Скопируйте страницы в часть документа.
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

## Разделение PDF на группы страниц

Разделите PDF-документ на несколько файлов на основе заданных групп страниц с помощью Aspose.PDF для Python.

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

## Разделение PDF-файла на отдельные страницы с сохранением стабильных имен файлов

Разделите PDF-документ на отдельные страницы и сохраните их с сохранением стабильных имен файлов, используя Aspose.PDF для Python.

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

## Разделение PDF-файла на четные и нечетные страницы

Разделите PDF-документ на два отдельных файла, содержащих соответственно нечетные и четные страницы, используя Aspose.PDF для Python.

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

## Связанные темы Document

- [Работа с PDF документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Объединить PDF файлы в Python](/pdf/ru/python-net/merge-pdf-documents/)
- [Оптимизировать PDF файлы в Python](/pdf/ru/python-net/optimize-pdf/)
- [Манипулировать PDF документами в Python](/pdf/ru/python-net/manipulate-pdf-document/)

