---
title: Удаление нумерации Бейтса из PDF на Python
linktitle: Удаление нумерации Бейтса
type: docs
weight: 100
url: /ru/python-net/remove-bates-numbering/
description: Удалить нумерацию Bates со всех страниц PDF в Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление нумерации Бейтса из PDF на Python
Abstract: Удалить нумерацию Bates со всех страниц PDF в Python.
---

Удалить нумерацию Bates со всех страниц PDF в Python.

## Удаление нумерации Бейтса

Передайте страницы документа в `PageCollectionExtensions.delete_bates_numbering` и сохраните PDF.

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## См. также

- [Добавление нумерации Бейтса](/pdf/ru/python-net/add-bates-numbering/)
- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
