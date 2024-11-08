---
title: Разделение PDF программно на языке Python
linktitle: Разделение PDF файлов
type: docs
weight: 20
url: /ru/python-cpp/split-pdf-document/
keywords: разделить pdf на несколько файлов, разделить pdf на отдельные pdf, разделить pdf python
description: Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы в ваших приложениях Python через C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Разделение страниц PDF может быть полезной функцией для тех, кто хочет разделить большой файл на отдельные страницы или группы страниц.

## Живой пример

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) это бесплатное веб-приложение, которое позволяет вам исследовать, как работает функция разбиения презентации.

[![Aspose Разделить PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы в ваших приложениях Python C++. Чтобы разделить страницы PDF на файлы PDF по одной странице с использованием Python, можно следовать следующим шагам:

Пример кода настраивает необходимые каталоги и пути к файлам, открывает PDF документ, а затем проходит через каждую страницу документа.
 Для каждой страницы создается новый документ, копируется текущая страница в новый документ и сохраняется новый документ как отдельный PDF файл с определенной системой именования.

1. Открыть входной документ
1. Инициализировать счетчик страниц
1. Перебрать все страницы документа

## Разделение PDF на несколько файлов или отдельных PDF в Python

Следующий фрагмент кода на Python показывает, как разделить страницы PDF на отдельные PDF файлы.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file = os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # Открыть документ
    document = apw.Document(inputFile)

    pageCount = 1

    # Перебрать все страницы

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```