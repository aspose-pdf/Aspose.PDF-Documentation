---
title: إضافة ترقيم Bates إلى PDF باستخدام Python
linktitle: إضافة ترقيم Bates
type: docs
weight: 10
url: /ar/python-net/add-bates-numbering/
description: إضافة معرّفات Bates متسلسلة إلى صفحات PDF باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة ترقيم Bates إلى PDF في Python
Abstract: إضافة معرّفات Bates متسلسلة إلى صفحات PDF.
---

يعيّن ترقيم Bates معرّفات متسلسلة لصفحات مجموعة من المستندات. اضبط كائن `BatesNArtifact` لتحديد نطاق الصفحات ورقم البداية وعدد الخانات والبادئة واللاحقة والموضع.

## إضافة عنصر ترقيم Bates

مرّر العنصر بعد إعداده وصفحات المستند إلى الطريقة `PageCollectionExtensions.add_bates_numbering`. يضيف المثال إلى الصفحات الحالية معرّفات من ستة أرقام تبدأ بالقيمة `000001`.

```python
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact


def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## إضافة ترقيم Bates عبر عناصر الترقيم

أعد استخدام الدالة `_create_bates_artifact` من المثال السابق، ثم مرّر العنصر ضمن قائمة إلى الطريقة `PageCollectionExtensions.add_pagination`.

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## مواضيع ذات صلة

- [إزالة ترقيم Bates](/pdf/ar/python-net/remove-bates-numbering/)
- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
