---
title: إضافة علامات مائية إلى PDF في Python
linktitle: إضافة علامة مائية
type: docs
weight: 30
url: /ar/python-net/add-watermarks/
description: تعرف على كيفية إضافة عناصر العلامة المائية إلى ملفات PDF في Python باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة علامة مائية إلى PDF باستخدام Python
Abstract: تتناول المقالة استخدام Aspose.PDF لـ Python عبر .NET لإضافة علامات مائية إلى مستندات PDF من خلال إدارة القطع الأثرية. يقدم الفئات الرئيسية للتعامل مع القطع الأثرية - «Artifact» و «ArtifactCollection»، ويصف كيفية الوصول إليها عبر خاصية «Artifacts» لفئة «الصفحة». توضح المقالة خصائص فئة «القطع الأثرية»، بما في ذلك سمات مثل «المحتويات» و «النموذج» و «الصورة» و «النص» و «المستطيل» و «الدوران» و «العتامة»، والتي تتيح معالجة شاملة للقطع الأثرية داخل ملفات PDF. بالإضافة إلى ذلك، يتم تقديم مثال عملي يوضح كيفية إضافة علامة مائية برمجيًا إلى الصفحة الأولى من PDF باستخدام Python. يوضح مقتطف الشفرة إنشاء وتكوين «WatermarkArtifact»، وتعيين النص، والمحاذاة، والتدوير، والتعتيم، قبل إلحاقه بمستند PDF وحفظ التغييرات.
---

أضف قطعة أثرية للعلامة المائية إلى PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام Aspose.PDF لبيثون عبر.NET. العلامة المائية عبارة عن تراكب مرئي يتم تطبيقه على الصفحات لأغراض العلامة التجارية أو الأمان أو المعلومات. يوضح المثال كيفية التكوين [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) المظهر وتحديد المواقع مع [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) و [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/)والدوران والشفافية قبل تطبيق العلامة المائية على [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## استخراج العلامات المائية من PDF

1. قم بتحميل وثيقة PDF.
1. عناصر صفحة الوصول.
1. تصفية آثار العلامة المائية.
1. اجمع عناصر العلامة المائية.
1. استخراج خصائص العلامة المائية.
1. معلومات العلامة المائية الناتجة.

```python
from os import path
import sys
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

## إضافة علامة مائية إلى PDF

أضف علامة مائية نصية إلى مستند PDF باستخدام Aspose.PDF لـ Python:

1. قم بتحميل وثيقة PDF.
1. قم بإنشاء حالة نصية.
1. قم بإنشاء قطعة أثرية للعلامة المائية.
1. قم بتعيين نص العلامة المائية ونمطها.
1. تكوين تحديد المواقع والدوران.
1. قم بتعيين العتامة وسلوك الخلفية.
1. أرفق العلامة المائية بصفحة.
1. احفظ المستند المحدث.

```python
from os import path
import sys
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

## قم بإزالة آثار العلامة المائية من صفحة PDF 

قم بإزالة عناصر العلامة المائية من صفحة معينة في مستند PDF باستخدام Aspose.PDF لواجهة برمجة تطبيقات Python. يستهدف هذا الأسلوب عناصر العلامة المائية المخزنة كعناصر للصفحة (خاصة تلك المصنفة على أنها أنواع فرعية للعلامات المائية لترقيم الصفحات)، ويقوم بالتكرار من خلالها وحذفها قبل حفظ المستند المحدث.

1. قم بتحميل وثيقة PDF.
1. عناصر صفحة الوصول.
1. تصفية آثار العلامة المائية.
1. احذف عناصر العلامة المائية.
1. احفظ المستند المحدث.

```python
from os import path
import sys
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

## موضوعات القطع الأثرية ذات الصلة

- [العمل مع مصنوعات PDF في بايثون](/pdf/ar/python-net/artifacts/)
- [إضافة خلفيات PDF في بايثون](/pdf/ar/python-net/add-backgrounds/)
- [إضافة ترقيم بيتس إلى PDF في بايثون](/pdf/ar/python-net/add-bates-numbering/)
- [عد أنواع القطع الأثرية في ملفات PDF](/pdf/ar/python-net/counting-artifacts/)