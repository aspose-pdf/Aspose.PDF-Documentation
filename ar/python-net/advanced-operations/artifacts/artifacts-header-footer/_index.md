---
title: إضافة رؤوس الصفحات وتذييلاتها إلى PDF باستخدام Python
linktitle: إضافة الرؤوس والتذييلات
type: docs
weight: 70
url: /ar/python-net/artifacts-header-footer/
description: إنشاء عناصر رؤوس الصفحات وتذييلاتها وتنسيقها وإضافتها إلى صفحات PDF باستخدام Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة رؤوس الصفحات وتذييلاتها إلى PDF في Python
Abstract: إنشاء عناصر رؤوس الصفحات وتذييلاتها وتنسيقها وإضافتها إلى صفحات PDF.
---

استخدم الفئتين `HeaderArtifact` و`FooterArtifact` لإضافة نص متكرر في رؤوس الصفحات وتذييلاتها. تضيف هذه الأمثلة العناصر إلى الصفحة الأولى.

## إنشاء عناصر نصية منسّقة

عرّف الدالة المساعدة قبل تشغيل أي من مثالَي الإضافة. تستخدم الدالة الخط والحجم واللون والمحاذاة نفسها للرؤوس والتذييلات.

```python
import aspose.pdf as ap

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact
```

## إضافة رأس إلى صفحة PDF

مرّر الفئة `HeaderArtifact` إلى الدالة المساعدة وأضف العنصر الناتج إلى الصفحة.

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## إضافة تذييل إلى صفحة PDF

مرّر الفئة `FooterArtifact` إلى الدالة المساعدة وأضف العنصر الناتج إلى الصفحة.

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## مواضيع ذات صلة

- [إزالة الرؤوس والتذييلات](/pdf/ar/python-net/remove-headers-footers/)
- [العمل مع عناصر PDF](/pdf/ar/python-net/artifacts/)
