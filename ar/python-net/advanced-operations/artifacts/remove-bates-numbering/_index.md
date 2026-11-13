---
title: إزالة ترقيم Bates من PDF باستخدام Python
linktitle: إزالة ترقيم Bates
type: docs
weight: 100
url: /ar/python-net/remove-bates-numbering/
description: إزالة ترقيم Bates من جميع صفحات ملف PDF باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة ترقيم Bates من PDF في Python
Abstract: إزالة ترقيم Bates من جميع صفحات ملف PDF.
---

إزالة ترقيم Bates من جميع صفحات ملف PDF.

## حذف ترقيم Bates

مرّر صفحات المستند إلى الطريقة `PageCollectionExtensions.delete_bates_numbering` واحفظ ملف PDF.

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## مواضيع ذات صلة

- [إضافة ترقيم Bates](/pdf/ar/python-net/add-bates-numbering/)
- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
