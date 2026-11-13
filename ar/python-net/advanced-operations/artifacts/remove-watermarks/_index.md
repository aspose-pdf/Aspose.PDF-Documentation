---
title: إزالة العلامات المائية من PDF باستخدام Python
linktitle: إزالة العلامات المائية
type: docs
weight: 90
url: /ar/python-net/remove-watermarks/
description: إزالة عناصر العلامات المائية من الصفحة الأولى من ملف PDF باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة العلامات المائية من PDF في Python
Abstract: إزالة عناصر العلامات المائية من الصفحة الأولى من ملف PDF.
---

إزالة عناصر العلامات المائية من الصفحة الأولى من ملف PDF.

## إزالة عناصر العلامات المائية

يحذف المثال من الصفحة الأولى عناصر النوع `PAGINATION` والنوع الفرعي `WATERMARK` فقط. وتبقى في ملف PDF العلامات المائية المرئية المخزّنة كنص عادي في الصفحة أو كصور أو تعليقات توضيحية.

```python
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## مواضيع ذات صلة

- [إضافة العلامات المائية](/pdf/ar/python-net/add-watermarks/)
- [استخراج تفاصيل العلامات المائية](/pdf/ar/python-net/extract-watermarks/)
- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
