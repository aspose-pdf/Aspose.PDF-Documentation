---
title: إضافة علامات مائية إلى PDF باستخدام Python
linktitle: إضافة العلامات المائية
type: docs
weight: 30
url: /ar/python-net/add-watermarks/
description: إضافة علامات مائية نصية منسّقة إلى صفحات PDF باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة علامات مائية إلى PDF في Python
Abstract: إضافة علامات مائية نصية منسّقة إلى صفحات PDF.
---

استخدم الفئة `WatermarkArtifact` لإضافة علامة مائية نصية إلى الصفحة الأولى من ملف PDF.

## إضافة علامة مائية إلى PDF

اضبط النص وتنسيقه، ثم حدّد المحاذاة وزاوية الدوران والعتامة. اضبط الخاصية `is_background` لوضع العلامة المائية خلف محتوى الصفحة.

```python
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)
```

## مواضيع ذات صلة

- [استخراج تفاصيل العلامات المائية](/pdf/ar/python-net/extract-watermarks/)
- [إزالة العلامات المائية](/pdf/ar/python-net/remove-watermarks/)
- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
