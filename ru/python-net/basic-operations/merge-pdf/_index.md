---
title: Объединение PDF-файлов в Python
linktitle: Объединение PDF-файлов
type: docs
weight: 50
url: /python-net/merge-pdf-documents/
description: Узнайте, как объединить несколько PDF-файлов в один документ в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Объединение страниц PDF с помощью Python
Abstract: В этой статье рассматривается распространённая необходимость объединения нескольких PDF-файлов в один документ — процесс, ценный для организации и оптимизации хранения и передачи PDF-содержимого. В ней исследуется использование Aspose.PDF для Python через .NET для эффективного объединения PDF-файлов, признавая, что объединение PDF в Python может быть сложным без сторонних библиотек. Статья содержит пошаговое руководство по объединению PDF-файлов — создание нового документа, объединение файлов и сохранение объединённого документа. Фрагмент кода демонстрирует реализацию с помощью Aspose.PDF, подчёркивая способность библиотеки упростить процесс объединения. Кроме того, представлен онлайн-инструмент Aspose.PDF Merger для объединения PDF, позволяющий пользователям изучить функциональность в веб-среде.
---

## Объединение PDF-файлов с помощью Python и DOM

Для объединения двух PDF-файлов:

1. Создайте новый документ.
1. Объедините PDF-файлы.
1. Сохраните объединённый документ.

Объединение нескольких PDF-документов в один файл:

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Онлайн-пример

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) — это бесплатное веб-приложение, которое позволяет изучить, как работает функция объединения PDF.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)