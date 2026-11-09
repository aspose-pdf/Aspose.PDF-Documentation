---
title: إضافة خلفيات إلى PDF باستخدام Python
linktitle: إضافة الخلفيات
type: docs
weight: 20
url: /ar/python-net/add-backgrounds/
description: إضافة صورة أو لون موحّد إلى خلفية صفحة PDF وضبط عتامة صورة الخلفية باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة خلفيات إلى PDF في Python
Abstract: إضافة صورة أو لون موحّد إلى خلفية صفحة PDF وضبط عتامة صورة الخلفية.
---

استخدم الفئة `BackgroundArtifact` لوضع صورة أو لون موحّد خلف محتوى صفحة PDF. تعدّل هذه الأمثلة الصفحة الأولى.

## إضافة صورة خلفية إلى PDF

أسند دفق الصورة إلى الخاصية `background_image` وأضف العنصر إلى الصفحة.

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## إضافة صورة خلفية شبه شفافة

مرّر إلى الدالة نفسها قيمة عتامة بين 0 و1. استخدم `0.5` للحصول على صورة شبه شفافة.

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## إضافة لون خلفية إلى PDF

اضبط الخاصية `background_color` لتطبيق لون موحّد على الخلفية.

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## مواضيع ذات صلة

- [إزالة الخلفيات](/pdf/ar/python-net/remove-backgrounds/)
- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
