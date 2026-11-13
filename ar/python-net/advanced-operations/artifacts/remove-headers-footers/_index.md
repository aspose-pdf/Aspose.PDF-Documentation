---
title: إزالة رؤوس الصفحات وتذييلاتها من PDF باستخدام Python
linktitle: إزالة الرؤوس والتذييلات
type: docs
weight: 110
url: /ar/python-net/remove-headers-footers/
description: إزالة عناصر الرؤوس والتذييلات من الصفحة الأولى من ملف PDF باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة رؤوس الصفحات وتذييلاتها من PDF في Python
Abstract: إزالة عناصر الرؤوس والتذييلات من الصفحة الأولى من ملف PDF.
---

إزالة عناصر الرؤوس والتذييلات من الصفحة الأولى من ملف PDF.

## إزالة عناصر الرؤوس والتذييلات

اجمع عناصر الترقيم من النوع الفرعي `HEADER` أو `FOOTER` قبل حذفها من الصفحة.

```python
import aspose.pdf as ap

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## مواضيع ذات صلة

- [إضافة الرؤوس والتذييلات](/pdf/ar/python-net/artifacts-header-footer/)
- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
