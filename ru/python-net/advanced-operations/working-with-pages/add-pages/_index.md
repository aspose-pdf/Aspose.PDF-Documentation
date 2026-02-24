---
title: Добавление страниц в PDF с помощью Python
linktitle: Добавление страниц
type: docs
weight: 10
url: /ru/python-net/add-pages/
description: Узнайте, как добавлять страницы в PDF‑документ на Python с помощью Aspose.PDF для гибкого создания и редактирования документов.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить страницы в PDF с помощью Python
Abstract: Статья представляет руководство по использованию Aspose.PDF for Python via .NET API для работы со страницами PDF‑документа. Она подчёркивает гибкость, предоставляемую API, особенно через класс `PageCollection`, который управляет всеми страницами в PDF. В документе подробно описаны процедуры добавления или вставки страниц в определённые места PDF‑файла. Рассмотрены две основные операции — вставка пустой страницы в нужное место документа и добавление пустой страницы в конец документа. Для обеих операций процесс включает создание объекта `Document`, использование методов `insert` или `add` класса `PageCollection` и сохранение изменённого документа. В статье содержатся фрагменты кода, демонстрирующие эти задачи, показывающие, насколько просто манипулировать PDF‑документами с помощью Python и этого API.
---

Aspose.PDF for Python via .NET API обеспечивает полную гибкость работы со страницами PDF‑документа на Python. Он хранит все страницы PDF‑документа в [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), которую можно использовать для работы со страницами PDF.
Aspose.PDF for Python via .NET позволяет вставлять страницу в [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в любом месте файла, а также добавлять страницы в конец PDF‑файла. В этом разделе показано, как добавлять страницы в PDF с помощью Python.

## Добавление или вставка страницы в PDF‑файл

Aspose.PDF for Python via .NET позволяет вставлять страницу в [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в любом месте файла, а также добавлять страницы в конец PDF‑файла.

### Вставка пустой страницы в PDF‑файл

Чтобы вставить пустую страницу в PDF‑файл:

1. Откройте существующий [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с помощью подходящих методов.
1. Вставьте новую пустую страницу в конкретный индекс, используя метод `insert()` класса [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните изменённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в требуемый путь вывода.

Вставьте пустую страницу в существующий PDF‑файл в указанную позицию:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Добавление пустой страницы в конец PDF‑файла

Иногда необходимо, чтобы документ завершался пустой страницей. Эта тема объясняет, как вставить пустую страницу в конец PDF‑документа.

Чтобы вставить пустую страницу в конец PDF‑файла:

1. Откройте существующий [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с помощью подходящих методов.
1. Добавьте новую пустую страницу в конец документа, используя метод `add()` класса [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните обновлённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF‑файла.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### Добавление страницы из другого PDF‑документа

С помощью библиотеки Aspose.PDF for Python вы создаёте новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), добавляете начальную страницу, а затем импортируете страницу из другого PDF‑файла.

1. Создайте новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Добавьте новую пустую [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) и напишите на ней текст, используя [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Откройте другой существующий [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Скопируйте [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) из этого документа.
1. Вставьте скопированную страницу в основной документ, используя [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните объединённый файл.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```
