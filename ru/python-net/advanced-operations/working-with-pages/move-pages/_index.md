---
title: Перемещение страниц PDF программным способом с помощью Python
linktitle: Перемещение страниц PDF
type: docs
weight: 100
url: /ru/python-net/move-pages/
description: Попробуйте переместить страницы в нужное место или в конец PDF‑файла с помощью Aspose.PDF для Python через .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Перемещение страниц между PDF‑документами с использованием Python
Abstract: Статья предоставляет подробное руководство по перемещению страниц между PDF‑документами или внутри одного PDF‑документа с использованием Python, в частности с применением библиотеки Aspose.PDF. В ней изложены пошаговые процедуры для трёх сценариев — перемещение одной страницы из одного PDF в другой, перенос нескольких страниц и перемещение страницы внутри того же документа. Каждый сценарий включает создание объектов класса `Document` для исходных и целевых PDF, манипулирование страницами через класс `PageCollection` и использование методов `add`, `delete` и `save` для достижения нужной реорганизации страниц. Предоставлены фрагменты кода для практической реализации, демонстрирующие, как эффективно перемещать страницы с помощью скриптов Python.
---

## Перемещение страницы из одного PDF‑документа в другой

Aspose.PDF для Python позволяет переместить страницу (а не просто скопировать её) из одного PDF в другой. Она удаляет выбранную страницу из оригинального документа и затем добавляет её в новый PDF‑файл.

Представьте, что вы вырезаете страницу из одной книги и вклеиваете её в другую — после перемещения страница больше не существует в оригинальном файле.

1. Откройте исходный PDF‑документ, используя класс [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Выберите конкретную страницу для перемещения (в данном случае, страницу 2) — это относится к объекту [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Создайте новый PDF‑документ (создайте экземпляр другого [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Добавьте выбранную страницу в новый PDF‑документ, используя [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) целевого документа (например, `another_document.pages.add(page)`).
1. Удалите страницу из оригинального документа через её [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (например, `document.pages.delete(index)`).
1. Сохраните оба документа.

Следующий фрагмент кода показывает, как переместить одну страницу.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## Перемещение группы страниц из одного PDF‑документа в другой

В отличие от копирования, эта операция переносит выбранные страницы — удаляя их из исходного файла и сохраняя в новом PDF.

1. Создайте новый пустой целевой документ (`Document`).
1. Выберите несколько страниц (в данном случае, страницы 1 и 3) из [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) исходного документа.
1. Пройдитесь по выбранным страницам и добавьте каждую в [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) целевого документа.
1. Сохраните целевой документ, содержащий перенесённые страницы.
1. Удалите перенесённые страницы из исходного документа, используя его [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните изменённый исходный документ под новым именем файла, чтобы сохранить обе версии.

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF‑файла.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## Перемещение страницы в новое место в текущем PDF‑документе

Показано, как переместить определённую страницу в другое положение в том же документе — часто требуется при реорганизации или редактировании макетов PDF.

1. Загрузите входной PDF‑документ, используя класс [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Выберите страницу, которую хотите переместить (страница 2) — это объект [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Добавьте её в конец документа, используя [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) документа.
1. Удалите оригинальную страницу из её прежнего места через [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните изменённый документ как новый файл.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```


