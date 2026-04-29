---
title: Открыть PDF‑документ программно
linktitle: Открыть PDF
type: docs
weight: 20
url: /python-net/open-pdf-document/
description: Узнайте, как открыть PDF‑файл в Python с помощью библиотеки Aspose.PDF for Python via .NET. Вы можете открыть существующий PDF, документ из потока и зашифрованный PDF‑документ.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Открытие PDF‑документов с использованием библиотеки Aspose.PDF в Python
Abstract: В этой статье представлено руководство по открытию существующих PDF‑документов с использованием библиотеки Aspose.PDF в Python. Описаны три способа достижения этого — открытие PDF путем указания имени файла, открытие PDF из потока и открытие зашифрованного PDF с предоставлением пароля. Каждый метод включает фрагмент кода, демонстрирующий, как использовать библиотеку Aspose.PDF для доступа к PDF и вывода количества страниц, которые он содержит. Эти примеры иллюстрируют гибкость и функциональность Aspose.PDF при работе с различными сценариями доступа к PDF‑файлам.
---

## Открыть существующий PDF‑документ

Существует несколько способов открыть документ. Самый простой — указать имя файла.

```python
import aspose.pdf as ap

def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))
```

## Открыть существующий PDF документ из потока

```python
import aspose.pdf as ap
import io

def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))
```

## Открыть зашифрованный PDF‑документ

```python
import aspose.pdf as ap

def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))
```
