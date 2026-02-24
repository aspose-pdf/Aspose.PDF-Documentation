---
title: Открыть PDF документ программно
linktitle: Открыть PDF
type: docs
weight: 20
url: /ru/python-net/open-pdf-document/
description: Узнайте, как открыть PDF‑файл в Python с помощью библиотеки Aspose.PDF для Python через .NET. Вы можете открыть существующий PDF, документ из потока и зашифрованный PDF‑документ.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Открытие PDF документов с использованием библиотеки Aspose.PDF в Python
Abstract: В этой статье представлено руководство по открытию существующих PDF‑документов с помощью библиотеки Aspose.PDF в Python. Описаны три метода достижения этой цели — открытие PDF путем указания имени файла, открытие PDF из потока и открытие зашифрованного PDF с вводом пароля. Каждый метод включает фрагмент кода, демонстрирующий, как использовать библиотеку Aspose.PDF для доступа к PDF и вывода количества страниц в нём. Эти примеры иллюстрируют гибкость и функциональность Aspose.PDF при работе с различными сценариями доступа к PDF‑файлам.
---

## Открыть существующий PDF документ

Существует несколько способов открыть документ. Самый простой — указать имя файла.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## Открыть существующий PDF документ из потока

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## Открыть зашифрованный PDF документ

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```

