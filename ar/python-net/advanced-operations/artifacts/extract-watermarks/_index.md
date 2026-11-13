---
title: استخراج تفاصيل العلامات المائية من PDF باستخدام Python
linktitle: استخراج تفاصيل العلامات المائية
type: docs
weight: 50
url: /ar/python-net/extract-watermarks/
description: قراءة النص والمستطيل المحيط بكل عنصر علامة مائية في الصفحة الأولى من ملف PDF باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج تفاصيل العلامات المائية من PDF في Python
Abstract: قراءة النص والمستطيل المحيط بكل عنصر علامة مائية في الصفحة الأولى من ملف PDF.
---

قراءة النص والمستطيل المحيط بكل عنصر علامة مائية في الصفحة الأولى من ملف PDF.

## قراءة نص العلامات المائية وحدودها

اطبع نص كل عنصر ترقيم من النوع الفرعي `WATERMARK` والمستطيل المحيط به.

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## مواضيع ذات صلة

- [إضافة العلامات المائية](/pdf/ar/python-net/add-watermarks/)
- [إزالة العلامات المائية](/pdf/ar/python-net/remove-watermarks/)
- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
