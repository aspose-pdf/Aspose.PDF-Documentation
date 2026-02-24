---
title: العمل مع الخلفيات ككائنات في بايثون
linktitle: إضافة خلفيات
type: docs
weight: 20
url: /ar/python-net/add-backgrounds/
description: أضف صورة خلفية إلى ملف PDF الخاص بك باستخدام بايثون. استخدم الفئة BackgroundArtifact.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة خلفية إلى PDF باستخدام بايثون
Abstract: تناقش هذه المقالة استخدام صور الخلفية في مستندات PDF باستخدام Aspose.PDF للبايثون عبر .NET. وتبرز القدرة على إضافة علامات مائية أو تصاميم دقيقة إلى المستندات من خلال الاستفادة من فئة `BackgroundArtifact`، التي تسمح بدمج صور الخلفية في كائنات الصفحات الفردية. تقدم المقالة مثالًا عمليًا على الشيفرة يوضح كيفية تنفيذ هذه الميزة. تتضمن العملية إنشاء مستند PDF جديد، إضافة صفحة، إنشاء كائن `BackgroundArtifact`، تعيين صورة خلفية، وإلحاق عنصر الخلفية بمجموعة القطع الأثرية للصفحة. أخيرًا، يتم حفظ المستند المعدل كملف PDF. تسمح هذه التقنية بتحسين العرض البصري لمستندات PDF.
---

يمكن استخدام صور الخلفية لإضافة علامة مائية، أو تصميم دقيق آخر، إلى المستندات. في Aspose.PDF للبايثون عبر .NET، كل مستند PDF هو مجموعة من الصفحات وتحتوي كل صفحة على مجموعة من القطع الأثرية. يمكن استخدام الفئة [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) لإضافة صورة خلفية إلى كائن صفحة.

يظهر الجزء البرمجي التالي كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact مع بايثون.

```python

import aspose.pdf as ap
import io

def add_background_image(input_image_file, output_pdf):
    # Create a new PDF document
    document = ap.Document()

    # Add a blank page to the document
    page = document.pages.add()

    # Create a BackgroundArtifact object
    background = ap.BackgroundArtifact()

    # Load the image as a binary stream
    with open(input_image_file, "rb") as image_stream:
        background.background_image = image_stream

        # Add the background artifact to the page
        page.artifacts.append(background)

    # Save the resulting PDF
    document.save(output_pdf)
```


