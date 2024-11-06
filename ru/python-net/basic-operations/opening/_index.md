---
title: Открыть PDF документ программно
linktitle: Открыть PDF
type: docs
weight: 20
url: ru/python-net/open-pdf-document/
description: Узнайте, как открыть PDF файл в Python с помощью библиотеки Aspose.PDF для Python через .NET. Вы можете открыть существующий PDF, документ из потока, и зашифрованный PDF документ.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Открыть существующий PDF документ

Существует несколько способов открыть документ. Самый простой - указать имя файла.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    print("Страницы: " + str(len(document.pages)))
```

## Открыть существующий PDF документ из потока

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Открыть документ
    document = ap.Document(stream)
    print("Страницы: " + str(len(document.pages)))
```

## Открыть зашифрованный PDF документ

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf, password)
    print("Страницы: " + str(len(document.pages)))
```