---
title: Создание PDF документа
linktitle: Создать PDF
type: docs
weight: 10
url: ru/python-cpp/create-document/
description: Эта страница описывает, как создать PDF документ с нуля с помощью Aspose.PDF для Python через библиотеку C++.
---

Для разработчиков существует множество сценариев, когда становится необходимо программно генерировать PDF файлы. Возможно, вам потребуется программно генерировать PDF отчеты и другие PDF файлы в вашем программном обеспечении. Писать собственный код и функции с нуля довольно долго и неэффективно. Чтобы создать PDF файл с помощью Python, есть лучшее решение - **Aspose.PDF для Python через C++**.

## Создание PDF файла с использованием Python

Чтобы создать PDF файл с использованием Python, можно использовать следующие шаги.

* импортировать все классы и методы из библиотеки Aspose.PDF для Python через C++.
* Создать новый объект Document, представляющий пустой PDF документ, используя [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/)

* Получить объект [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/), содержащий все страницы в документе.
* Добавляет новую страницу в конец коллекции страниц [page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/) и возвращает объект Page, представляющий добавленную страницу.
* Сохраняет документ в файл с указанным именем в текущем рабочем каталоге.
* Закрывает дескриптор документа и освобождает все ресурсы, связанные с ним.

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```

## Создание PDF файла на основе DOM

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```