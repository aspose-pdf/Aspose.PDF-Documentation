---
title: Разделение PDF программно на Python
linktitle: Разделить PDF-файлы
type: docs
weight: 60
url: /ru/python-net/split-pdf-document/
description: В этой теме показано, как разделять страницы PDF на отдельные PDF‑файлы в ваших Python‑приложениях.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделение страниц PDF с использованием Python
Abstract: В статье обсуждается процесс разделения страниц PDF на отдельные файлы с помощью Python, подчеркивая пользу такой функции для управления большими PDF‑документами. В ней упоминается Aspose.PDF Splitter — онлайн‑инструмент, предназначенный для демонстрации функции разделения PDF. Статья предоставляет подробный метод реализации этого в Python‑приложениях, включающий перебор страниц PDF‑документа через `Document` объект `PageCollection`. Для каждой страницы создаётся новый объект `Document`, страница добавляется в него, и новый PDF‑файл сохраняется с помощью метода `save()`. Сопутствующий фрагмент кода на Python иллюстрирует этот процесс, показывая шаги, необходимые для разделения PDF‑документа на отдельные файлы путём перебора его страниц и сохранения каждой в отдельный PDF.
---

Разделение страниц PDF может быть полезной функцией для тех, кто хочет разбить большой файл на отдельные страницы или группы страниц.

## Пример в реальном времени

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) — бесплатное онлайн‑веб‑приложение, которое позволяет изучать, как работает функция разделения презентаций.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

В этой теме показано, как разделять страницы PDF на отдельные PDF‑файлы в ваших Python‑приложениях. Чтобы разделить страницы PDF на отдельные PDF‑файлы по одной странице с помощью Python, можно выполнить следующие шаги:

1. Переберите страницы PDF‑документа через объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и его коллекцию [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Для каждой итерации создайте новый объект Document и добавьте отдельный объект [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в пустой документ.
1. Сохраните новый PDF, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

## Разделить PDF на несколько файлов или отдельные PDF в Python

Следующий фрагмент кода на Python показывает, как разделить страницы PDF на отдельные PDF‑файлы.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```


