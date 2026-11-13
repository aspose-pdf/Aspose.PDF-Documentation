---
title: إزالة الخلفيات من PDF باستخدام Python
linktitle: إزالة الخلفيات
type: docs
weight: 80
url: /ar/python-net/remove-backgrounds/
description: إزالة عناصر الخلفية من الصفحة الأولى من ملف PDF باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة الخلفيات من PDF في Python
Abstract: إزالة عناصر الخلفية من الصفحة الأولى من ملف PDF.
---

إزالة عناصر الخلفية من الصفحة الأولى من ملف PDF.

## إزالة عناصر الخلفية

اجمع عناصر الترقيم من النوع الفرعي `BACKGROUND` قبل حذفها من الصفحة.

```python
import aspose.pdf as ap

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## مواضيع ذات صلة

- [إضافة الخلفيات](/pdf/ar/python-net/add-backgrounds/)
- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
