---
title: Базовое извлечение текста с помощью Python
linktitle: Базовое извлечение текста
type: docs
weight: 10
url: /ru/python-net/basic-text-extraction/
description: Эта секция содержит статьи об базовом извлечении текста из PDF-документов с использованием Aspose.PDF в Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF‑документа

Aspose.PDF for Python учит вас, как извлекать текст с каждой страницы PDF‑документа. Он использует класс TextAbsorber для захвата всего текстового содержимого всего документа и сохраняет его в отдельный текстовый файл.
Идеально подходит для преобразования PDF‑файлов в поисковый текст, выполнения анализа содержимого или экспорта текста для задач индексации и обработки.

1. Загрузите PDF‑файл.
1. Создайте объект 'TextAbsorber'.
1. Вызовите 'document.pages.accept(text_absorber)', чтобы он просканировал все страницы.
1. Получите полный текст через 'text_absorber.text'.
1. Запишите результат в текстовый файл.

```python

import os
import aspose.pdf as ap

def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    try:
        # Create a TextAbsorber to extract text
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber for all pages
        document.pages.accept(text_absorber)
        # Get extracted text
        extracted_text = text_absorber.text
        # Write the text to an output file
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Извлечение текста с конкретной страницы

Извлеките текст с одной страницы PDF‑документа. Применяя TextAbsorber только к указанной странице, вы можете изолировать и сохранить текст из конкретного раздела многостраничного PDF.

Полезно, когда вам нужен контент только с одной страницы — например, извлечение текста со страницы счета, раздела отчёта или сводки полей формы.

1. Откройте PDF.
1. Создайте TextAbsorber.
1. Примите только назначенную страницу (pages[page_number]).
1. Извлеките текст и запишите его в файл.

```python

import os
import aspose.pdf as ap

def extract_text_from_page(infile, page_number, outfile):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based page index to extract.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber on only the specified page
        document.pages[page_number].accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

