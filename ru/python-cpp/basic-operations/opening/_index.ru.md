---
title: Открыть PDF документ программно
linktitle: Открыть PDF
type: docs
weight: 20
url: /python-cpp/open-pdf-document/
description: Узнайте, как открыть PDF файл в Python с помощью библиотеки Aspose.PDF для Python через C++. Вы можете открыть существующий PDF, документ из потока и зашифрованный PDF документ.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Открыть существующий PDF документ

Существует несколько способов открыть документ. Самый простой — указать имя файла.

```python

    import AsposePDFPythonWrappers as ap
    # Открыть документ
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("Страницы: " + str(count))
```

## Открыть зашифрованный PDF документ

```python

    import AsposePDFPythonWrappers as ap
    # Открыть документ
    document = ap.Document("sample.pdf","password")
    count = document.pages.count()
    print("Страницы: " + str(count))
```