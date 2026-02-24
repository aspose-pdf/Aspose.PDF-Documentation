---
title: Программное извлечение страниц на Python
linktitle: Извлечение страниц PDF
type: docs
weight: 80
url: /ru/python-net/extract-pages/
description: Вы можете извлекать страницы из вашего PDF‑файла с помощью библиотеки Aspose.PDF для Python через .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь страницы PDF с помощью Python
Abstract: В этой статье показано, как извлекать страницы из PDF‑документа с помощью библиотеки Aspose.PDF для Python. Описаны методы как одностраничного извлечения, так и многостраничного, позволяющие разработчикам создавать новые PDF‑файлы, содержащие только выбранные страницы. Примеры демонстрируют, как получить доступ к конкретным страницам по индексу, начиная с 1, скопировать их в новый PDF‑документ и сохранить результат, оставив исходный документ неизменным. Эти методы полезны для разбиения больших документов, обмена выбранными разделами или создания кастомных наборов PDF для распространения или анализа.
---

## Извлечение одной страницы из PDF

Извлеките конкретную страницу из PDF‑документа и сохраните её как новый файл. С помощью библиотеки Aspose.PDF скрипт копирует нужную страницу в новый PDF, оставляя оригинальный документ без изменений. Это удобно для разделения PDF‑файлов или выделения важных страниц для распространения.

1. Загрузите исходный PDF, используя API [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Создайте новый [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) для хранения извлечённой страницы.
1. Добавьте нужную [`Страница`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) из исходного документа в новый PDF, используя [`КоллекцияСтраниц`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) целевого документа (`dst_document.pages.add(...)`).
- В этом примере извлекается страница 2 (нумерация с 1).
1. Сохраните новый [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с извлечённой страницой в указанный файл вывода.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function extracts page 2 from the input
    document and saves it as a new file containing only that page.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the extracted page will be saved.

    Returns:
        None: The function creates a new PDF containing the extracted page and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    # Open source PDF as Document
    src_document = ap.Document(input_file_name)
    # Create destination Document to hold extracted pages
    dst_document = ap.Document()
    # Add a Page from source to destination using PageCollection API
    dst_document.pages.add(src_document.pages[2])
    # Save destination Document
    dst_document.save(output_file_name)
```

## Извлечение нескольких страниц из PDF

Извлеките несколько конкретных страниц из PDF‑документа и сохраните их в новый файл. С помощью библиотеки Aspose.PDF выбранные страницы копируются в новый PDF, при этом оригинальный документ остаётся нетронутым. Это полезно для создания меньших PDF‑файлов, содержащих лишь нужные разделы большого документа.

1. Загрузите исходный PDF, используя API [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Создайте новый [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) для хранения извлечённых страниц.
1. Выберите страницы для извлечения (в этом примере — страницы 2 и 3, нумерация с 1).
1. Добавьте каждую выбранную [`Страница`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) из исходного документа в новый PDF, используя её [`КоллекцияСтраниц`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните новый [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с извлечёнными страницами в указанный файл вывода.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_bunch_pages(input_file_name, output_file_name):
    """
    Extract specific pages from a PDF document and save them to a new file.

    This function reads a PDF document, extracts pages 2 and 3 (1-indexed),
    and saves them to a new PDF file.

    Args:
        input_file_name (str): Path to the input PDF file to extract pages from.
        output_file_name (str): Path where the new PDF file with extracted pages will be saved.

    Returns:
        None

    Note:
        The function specifically extracts pages 2 and 3 from the source document.
        Page indexing appears to be 1-based in this implementation.
    """
    # Open source Document
    document = ap.Document(input_file_name)
    pages = [2,3]
    # Create destination Document
    another_document = ap.Document()
    # Copy selected Page objects via PageCollection API
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    # Save destination Document
    another_document.save(output_file_name)
```
