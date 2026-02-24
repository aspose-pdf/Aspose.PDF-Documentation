---
title: إضافة علامة مائية إلى PDF باستخدام بايثون
linktitle: إضافة علامة مائية
type: docs
weight: 30
url: /ar/python-net/add-watermarks/
description: تشرح هذه المقالة ميزات العمل مع القطع الأثرية والحصول على علامات مائية في ملفات PDF باستخدام بايثون برمجيًا.
lastmod: "2025-11-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة علامة مائية إلى PDF باستخدام بايثون
Abstract: تناقش المقالة استخدام Aspose.PDF for Python عبر .NET لإضافة علامات مائية إلى مستندات PDF من خلال إدارة القطع الأثرية. تُعرّف الفئات الأساسية للتعامل مع القطع الأثرية - `Artifact` و `ArtifactCollection`، وتصف كيفية الوصول إليها عبر خاصية `Artifacts` في فئة `Page`. تُفصّل المقالة خصائص فئة `Artifact`، بما في ذلك السمات مثل `contents` و `form` و `image` و `text` و `rectangle` و `rotation` و `opacity`، والتي تتيح التلاعب الشامل بالقطع الأثرية داخل ملفات PDF. بالإضافة إلى ذلك، يتم تقديم مثال عملي يوضح كيفية إضافة علامة مائية برمجيًا إلى الصفحة الأولى من ملف PDF باستخدام بايثون. يوضح مقطع الشيفرة إنشاء وتكوين `WatermarkArtifact`، وتعيين نصه، ومحاذاته، ودورانه، وشفافيته، قبل إلحاقه بمستند PDF وحفظ التغييرات.
---

## عينات برمجية: كيفية إضافة علامة مائية على ملفات PDF

أضف قطعة أثرية للعلامة المائية إلى ملف PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام Aspose.PDF for Python عبر .NET. العلامة المائية هي طبقة بصرية تُطبق على الصفحات لأغراض العلامة التجارية أو الأمان أو المعلوماتية. يوضح المثال كيفية تكوين مظهر [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) وتحديد الموقع باستخدام [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) و [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/)، والدوران، والشفافية قبل تطبيق العلامة المائية على [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

1. إنشاء قطعة أثرية للعلامة المائية (انظر [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)).
1. تكوين حالة النص (انظر [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)).
1. ربط النص بالعلامة المائية.
1. تحديد الموضع والنمط باستخدام [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) و [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/).
1. إرفاق العلامة المائية بـ [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) عبر مجموعة [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) للصفحة (انظر [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)).
1. حفظ الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) المحدث باستخدام [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```


