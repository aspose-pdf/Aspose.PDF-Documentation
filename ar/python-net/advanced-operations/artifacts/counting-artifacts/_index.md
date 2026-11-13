---
title: عدّ عناصر الترقيم في PDF باستخدام Python
linktitle: عدّ عناصر الترقيم
type: docs
weight: 40
url: /ar/python-net/counting-artifacts/
description: عدّ عناصر الترقيم في صفحة PDF بحسب النوع الفرعي للعلامة المائية أو الخلفية أو الرأس أو التذييل باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: عدّ عناصر الترقيم في PDF في Python
Abstract: عدّ عناصر الترقيم في صفحة PDF بحسب النوع الفرعي للعلامة المائية أو الخلفية أو الرأس أو التذييل.
---

يكشف عدّ عناصر الترقيم في صفحة PDF عن العلامات المائية والخلفيات والرؤوس والتذييلات.

## عدّ عناصر الترقيم بحسب النوع الفرعي

رشّح مجموعة `artifacts` في الصفحة الأولى بحسب النوع `PAGINATION`، ثم احسب عدد العناصر من كل نوع فرعي. يطبع المثال صفرًا عند غياب أحد الأنواع الفرعية.

```python
from collections import Counter
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## مواضيع ذات صلة

- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
- [استخراج تفاصيل العلامات المائية](/pdf/ar/python-net/extract-watermarks/)
- [إزالة العلامات المائية](/pdf/ar/python-net/remove-watermarks/)
- [إزالة الخلفيات](/pdf/ar/python-net/remove-backgrounds/)
- [إزالة الرؤوس والتذييلات](/pdf/ar/python-net/remove-headers-footers/)
