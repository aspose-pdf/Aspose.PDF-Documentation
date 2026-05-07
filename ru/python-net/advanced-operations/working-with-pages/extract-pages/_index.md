---
title: Извлечение страниц PDF в Python
linktitle: Извлечение страниц PDF
type: docs
weight: 80
url: /ru/python-net/extract-pages/
description: Узнайте, как извлекать отдельные или несколько страниц PDF в новые файлы с помощью Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь страницы PDF с помощью Python
Abstract: В этой статье объясняется, как извлекать страницы из PDF‑файлов с помощью Aspose.PDF for Python via .NET. Узнайте, как копировать одну страницу или несколько страниц в новый документ, используя нумерацию страниц, начинающуюся с 1, и PageCollection API.
---

## Извлечение отдельной страницы из PDF

Извлеките определённую страницу из PDF‑документа и сохраните её как новый файл. С помощью библиотеки Aspose.PDF скрипт копирует нужную страницу в новый PDF, оставляя оригинальный документ неизменным. Это полезно для разделения PDF‑файлов или выделения важных страниц для распространения.

1. Загрузите исходный PDF с помощью [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Создайте новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) чтобы удержать извлечённую страницу.
1. Добавьте нужную [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) из исходного документа в новый PDF, используя документ назначения [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - В этом примере страница 2 извлекается (нумерация с 1).
1. Сохраните новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с извлечённой страницей в указанный файл вывода.

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## Извлечение нескольких страниц из PDF

Извлеките несколько конкретных страниц из PDF‑документа и сохраните их в новый файл. С помощью библиотеки Aspose.PDF выбранные страницы копируются в новый PDF, при этом исходный документ остаётся неизменным. Это полезно для создания более небольших PDF, содержащих только релевантные разделы большого документа.

1. Загрузите исходный PDF с помощью [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Создайте новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) для хранения извлечённых страниц.
1. Выберите страницы для извлечения (в этом примере страницы 2 и 3, используя индексацию с 1).
1. Добавьте каждую выбранную [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) из исходного документа в новый PDF, используя его [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с извлечёнными страницами в указанный файл вывода.

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## Связанные темы страницы

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Удалить страницы PDF в Python](/pdf/ru/python-net/delete-pages/)
- [Переместить страницы PDF в Python](/pdf/ru/python-net/move-pages/)
- [Разделить PDF-файлы в Python](/pdf/ru/python-net/split-document/)
