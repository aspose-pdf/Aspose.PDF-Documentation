---
title: Разделить PDF-файлы в Python
linktitle: Разделить PDF-файлы
type: docs
weight: 60
url: /ru/python-net/split-pdf-document/
description: Узнайте, как разделить страницы PDF на отдельные PDF-файлы в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделение страниц PDF с помощью Python
Abstract: В статье рассматривается процесс разделения страниц PDF на отдельные файлы с помощью Python, подчёркивая полезность такой функции для управления большими PDF‑документами. Упоминается Aspose.PDF Splitter, онлайн‑инструмент, предназначенный для демонстрации функции разделения PDF. Статья предоставляет подробный метод реализации этого в приложениях на Python, включающий перебор страниц PDF‑документа через `Document` object's `PageCollection`. Для каждой страницы создаётся новый объект `Document`, страница добавляется в него, и новый PDF‑файл сохраняется с помощью метода `save()`. Прилагаемый фрагмент кода на Python иллюстрирует этот процесс, показывая шаги, необходимые для разделения PDF‑документа на отдельные файлы путем перебора его страниц и сохранения каждой как отдельного PDF.
---

Разделение страниц PDF может быть полезной функцией для тех, кто хочет разбить большой файл на отдельные страницы или группы страниц

Используйте этот рабочий процесс, когда необходимо разбить большие PDF‑файлы на одностраничные файлы или меньшие наборы документов для распределения, проверки или последующей обработки.

## Онлайн пример

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) это бесплатное онлайн веб‑приложение, которое позволяет изучить, как работает функция разделения представлений.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

В этой теме показано, как разбить страницы PDF на отдельные PDF‑файлы в ваших приложениях на Python. Чтобы разбить страницы PDF на одностраничные PDF‑файлы с использованием Python, можно выполнить следующие шаги:

1. Переберите страницы PDF‑документа через [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) коллекция
1. Для каждой итерации создайте новый объект Document и добавьте отдельные [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) объект в пустой документ
1. Сохранить новый PDF с помощью [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод

## Разделить PDF на несколько файлов или отдельные PDF в Python

Следующий фрагмент кода Python показывает, как разбить страницы PDF на отдельные PDF‑файлы.

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

## Связанные темы документа

- [Работа с PDF‑документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Объединение PDF‑файлов в Python](/pdf/ru/python-net/merge-pdf-documents/)
- [Оптимизация PDF‑файлов в Python](/pdf/ru/python-net/optimize-pdf/)
- [Обрабатывать PDF‑документы в Python](/pdf/ru/python-net/manipulate-pdf-document/)

