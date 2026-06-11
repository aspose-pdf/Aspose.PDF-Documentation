---
title: إدارة رؤوس وتذييلات PDF باستخدام Python
linktitle: إدارة رؤوس وتذييلات PDF
type: docs
weight: 70
url: /ar/python-net/artifacts-header-footer/
description: تعرف على كيفية إدارة الرؤوس والتذييلات في مستندات PDF باستخدام Python و Aspose.PDF.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة رؤوس وتذييلات PDF وتخصيصها وإزالتها باستخدام Python
Abstract: تعد إدارة الرؤوس والتذييلات مطلبًا شائعًا عند العمل مع مستندات PDF في عمليات سير العمل الخاصة بالأعمال والنشر والأتمتة. توضح هذه المقالة كيفية استخدام Aspose.PDF لـ Python لإضافة رؤوس وتذييلات ذات مظهر احترافي مع تصميم مخصص مثل الخط والحجم واللون والمحاذاة. كما يوضح أيضًا كيفية اكتشاف وإزالة عناصر ترقيم الصفحات الموجودة مثل الرؤوس والتذييلات من صفحة PDF. من خلال الوظائف القابلة لإعادة الاستخدام والأمثلة الواضحة، يمكن للمطورين دمج هذه الميزات بسرعة في أنظمة معالجة المستندات للعلامة التجارية أو إعداد التقارير أو تنظيف الملفات.
---

## إنشاء عناصر نصية ذات نمط

تشرح وظيفة الأداة المساعدة هذه كيفية إنشاء قطعة أثرية نصية قابلة لإعادة الاستخدام لصفحات PDF باستخدام Aspose.PDF لـ Python. تم تصميمه لإنشاء رؤوس أو تذييلات ذات نمط بتنسيق متسق، بما في ذلك إعدادات الخط واللون والحجم والمحاذاة. تقوم الوظيفة بتلخيص إنشاء القطع الأثرية بحيث يمكن إعادة استخدامها لزخارف نصية مختلفة على مستوى الصفحة.

1. قم بإنشاء مثيل لكائن القطع الأثرية.
1. قم بتعيين محتوى نص قطعة أثرية.
1. قم بتطبيق نمط النص.
1. اضبط المحاذاة.
1. قم بإرجاع قطعة أثرية تم تكوينها.

```python
from os import path
import aspose.pdf as ap
import sys

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

## إضافة رأس إلى PDF

1. افتح ملف PDF المُدخل.
1. قم بإنشاء HeaderArtifact بنص «نموذج رأس».
1. قم بإلحاقه بالصفحة الأولى.
1. احفظ ملف PDF المحدث.

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## إضافة تذييل إلى PDF

1. افتح ملف PDF المُدخل.
1. قم بإنشاء أداة تذييل تحتوي على نص «نموذج تذييل الصفحة».
1. قم بإلحاقه بالصفحة الأولى.
1. احفظ ملف الإخراج.

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## حذف عناصر رأس الصفحة أو تذييلها

1. افتح ملف PDF.
1. ابحث عن القطع الأثرية التي تم وضع علامة عليها كرؤوس أو تذييلات لترقيم الصفحات.
1. قم بإزالتها من الصفحة الأولى.
1. احفظ المستند الذي تم تنظيفه.

```python
from os import path
import aspose.pdf as ap
import sys

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

## موضوعات القطع الأثرية ذات الصلة

- [العمل مع مصنوعات PDF في بايثون](/pdf/ar/python-net/artifacts/)
- [إضافة خلفيات PDF في بايثون](/pdf/ar/python-net/add-backgrounds/)
- [إضافة ترقيم بيتس إلى PDF في بايثون](/pdf/ar/python-net/add-bates-numbering/)
- [عد أنواع القطع الأثرية في ملفات PDF](/pdf/ar/python-net/counting-artifacts/)